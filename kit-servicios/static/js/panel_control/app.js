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
      templateUrl: 'static/partials/manager_panel.html',
      controller: 'statusServiceController'
    }).
    when('/recipe/', {
      templateUrl: 'static/partials/install_recipe.html',
      controller: 'recipeController'
    }).
    when('/update/', {
      templateUrl: 'static/partials/update_recipe.html',
      controller: 'recipeUpdateController'
    }).
    when('/query/', {
      templateUrl: 'static/partials/query_recipe.html',
      controller: 'queryServiceController'
    }).
    when('/delete/', {
      templateUrl: 'static/partials/delete_recipe.html',
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

