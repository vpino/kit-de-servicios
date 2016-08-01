'use strict';

/* App Module */

var panelApp = angular.module('panelApp', [
  'ngRoute',
  'ManageServices',
  'ManageControllers',
  'ManageDirectives',
  'ManageFilters'
  ]);

panelApp.config(['$resourceProvider', function($resourceProvider) {
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);

panelApp.config(['$routeProvider', '$locationProvider',
function($routeProvider, $locationProvider) {
  $routeProvider.
    when('/panel/:name', {
      templateUrl: 'static/partials/panel.html',
      controller: 'statusServiceController'
    }).
    when('/recipe/:name/:host/:action', {
      templateUrl: 'static/partials/recipe.html',
      controller: 'recipeController'
    }).
    when('/update/:name/:host/:action', {
      templateUrl: 'static/partials/update.html',
      controller: 'recipeController'
    }).
    when('/query/:name/:host', {
      templateUrl: 'static/partials/query.html',
      controller: 'queryServiceController'
    }).
    when('/delete/:name/:host/:action', {
      templateUrl: 'static/partials/delete.html',
      controller: 'recipeController'
    }).
     when('/key/', {
      templateUrl: 'static/partials/key.html',
      controller: 'keyController'
    }).
    otherwise({
      redirectTo: '/'
    });

    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');

}]);



/*
  panelApp.run(run);

  run.$inject = ['$http'];

  /**
  * @name run
  * @desc Update xsrf $http headers to align with Django's defaults
  */
  /*
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
  */