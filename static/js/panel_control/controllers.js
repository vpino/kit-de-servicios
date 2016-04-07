'use strict';

/* Controllers */

var ManageControllers = angular.module('ManageControllers', []);

ManageControllers.controller('recipeController', ['$scope', '$location', '$routeParams', 'Recipe', recipeController]);

    function recipeController($scope, $location, $routeParams, Recipe){
        
        console.log($routeParams);

        $scope.Params = Recipe.get({name:$routeParams.name});

        console.log($scope.Params);     

          
    }
