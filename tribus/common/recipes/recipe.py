#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013-2014 Tribus Developers
#
# This file is part of Tribus.
#
# Tribus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tribus is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
import yaml
from tribus.common import serializer
from tribus.common.charms.errors import MetaDataError
from tribus.common.errors import FileNotFound
from tribus.common.format import is_valid_charm_format
from tribus.common.schema import (
    SchemaError, Bool, Constant, Dict, Int,
    KeyDict, OneOf, UnicodeOrString)

class Recipe(object):

    """Abstract base class for charm implementations."""

    _sha256 = None

    def _unsupported(self, attr):
        raise NotImplementedError("%s.%s not supported" %
                                  (self.__class__.__name__, attr))


    def compute_sha256(self):
        """

        Compute the sha256 for this charm.

        Every charm subclass must implement this.

        """
        self._unsupported("compute_sha256()")

    def get_sha256(self):
        """

        Return the cached sha256, or compute it if necessary.

        If the sha256 value for this charm is not yet cached,
        the compute_sha256() method will be called to compute it.

        """
        if self._sha256 is None:
            self._sha256 = self.compute_sha256()
        return self._sha256


class InterfaceExpander(object):
    """Schema coercer that expands the interface shorthand notation.

    We need this class because our charm shorthand is difficult to
    work with (unfortunately). So we coerce shorthand and then store
    the desired format in ZK.

    Supports the following variants::

      provides:
        server: riak
        admin: http
        foobar:
          interface: blah

      provides:
        server:
          interface: mysql
          limit:
          optional: false

    In all input cases, the output is the fully specified interface
    representation as seen in the mysql interface description above.
    """

    def __init__(self, limit):
        """Create relation interface reshaper.

        @limit: the limit for this relation. Used to provide defaults
            for a given kind of relation role (peer, provider, consumer)
        """
        self.limit = limit

    def coerce(self, value, path):
        """Coerce `value` into an expanded interface.

        Helper method to support each of the variants, either the
        charm does not specify limit and optional, such as foobar in
        the above example; or the interface spec is just a string,
        such as the ``server: riak`` example.
        """

        if not isinstance(value, dict):
            # A LOT HACKY!
            #return {
                #"interface": UTF8_SCHEMA.coerce(value, path),
                #"limit": self.limit,
                #"scope": SCOPE_GLOBAL,
                #"optional": False
            #    }
            return value
        else:
            # Optional values are context-sensitive and/or have
            # defaults, which is different than what KeyDict can
            # readily support. So just do it here first, then
            # coerce.
            #if "limit" not in value:
            #    value["limit"] = self.limit
            #if "optional" not in value:
            #    value["optional"] = False
            #value["scope"] = value.get("scope", SCOPE_GLOBAL)
            return INTERFACE_SCHEMA.coerce(value, path)

UTF8_SCHEMA = UnicodeOrString("utf-8")
SCOPE_GLOBAL = "global"
SCOPE_CONTAINER = "container"

# Para cada estrucutra de datos puedo crear un esquema personalizado,
# adaptable a las configuraciones especificas de cada receta
INTERFACE_SCHEMA = KeyDict({"interface": UTF8_SCHEMA },optional=["scope"])

SCHEMA = KeyDict({
    "name": UTF8_SCHEMA,
    "revision": Int(),
    "summary": UTF8_SCHEMA,
    "description": UTF8_SCHEMA,
    "format": Int(),
    "components" : Dict(Int(), InterfaceExpander(limit=1)),
    }, optional=set(["format", "components", "revision"]))


class MetaData(object):
    """Represents the charm info file.

    The main metadata for a charm (name, revision, etc) is maintained
    in the charm's info file.  This class is able to parse,
    validate, and provide access to data in the info file.
    """

    def __init__(self, path=None):
        self._data = {}
        if path is not None:
            self.load(path)

    @property
    def name(self):
        """The charm name."""
        return self._data.get("name")

    @property
    def summary(self):
        """The charm summary."""
        return self._data.get("summary")

    @property
    def maintainer(self):
        """The charm maintainer."""
        return self._data.get("maintainer")

    @property
    def description(self):
        """The charm description."""
        return self._data.get("description")

    @property
    def components(self):
        """The charm description."""
        return self._data.get("components")

    @property
    def format(self):
        """Optional charm format, defaults to 1"""
        return self._data.get("format", 1)

    def get_serialization_data(self):
        """Get internal dictionary representing the state of this instance.

        This is useful to embed this information inside other storage-related
        dictionaries.
        """
        return dict(self._data)

    def load(self, path):
        """Load and parse the info file.

        @param path: Path of the file to load.

        Internally, this function will pass the content of the file to
        the C{parse()} method.
        """
        if not os.path.isfile(path):
            raise FileNotFound(path)
        with open(path) as f:
            self.parse(f.read(), path)

    def parse(self, content, path=None):
        """Parse the info file described by the given content.

        @param content: Content of the info file to parse.
        @param path: Optional path of the loaded file.  Used when raising
            errors.

        @raise MetaDataError: When errors are found in the info data.
        """
        try:
            self.parse_serialization_data(
                serializer.yaml_load(content), path)
        except yaml.MarkedYAMLError, e:
            # Capture the path name on the error if present.
            if path is not None:
                e.problem_mark = serializer.yaml_mark_with_path(
                    path, e.problem_mark)
            raise

        if not is_valid_charm_format(self.format):
            raise MetaDataError("Charm %s uses an unknown format: %s" % (
                    self.name, self.format))

    def parse_serialization_data(self, serialization_data, path=None):
        """Parse the unprocessed serialization data and load in this instance.

        @param serialization_data: Unprocessed data matching the
            metadata schema.
        @param path: Optional path of the loaded file.  Used when
            raising errors.

        @raise MetaDataError: When errors are found in the info data.
        """
        try:
            self._data = SCHEMA.coerce(serialization_data, [])
        except SchemaError, error:
            if path:
                path_info = " %s:" % path
            else:
                path_info = ""
            raise MetaDataError("Bad data in charm info:%s %s" %
                                (path_info, error))


class RecipeDir(Recipe):

    type = "dir"

    def __init__(self, path):
        """Set initial values and parse configuration files from the recipe."""
        self.path = path
        self.metadata = MetaData(os.path.join(path, 'metadata.yaml'))
