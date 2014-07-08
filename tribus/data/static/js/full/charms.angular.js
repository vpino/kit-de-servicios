// Declare use of strict javascript
'use strict';

// Application -----------------------------------------------------------------

var tribus = angular.module('tribus', ['ngDragDrop', 'ngSanitize', 'Search', 'ui.bootstrap','CharmsList']);

// Controllers -----------------------------------------------------------------

tribus.controller('CharmsController', ['$scope','CharmsList', CharmsController]);
