// Declare use of strict javascript
'use strict';

// Application -----------------------------------------------------------------

var tribus = angular.module('tribus', ['ngDragDrop', 'ngSanitize', 'Search', 'ui.bootstrap']);

// Controllers -----------------------------------------------------------------

tribus.controller('CharmsController', ['$scope', CharmsController]);
