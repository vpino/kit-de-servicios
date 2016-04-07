'use strict';

/* Controllers */

/* Declaro el modulo ManageCOntrollers*/
var ManageControllers = angular.module('ManageControllers', []);

/* Declaro un controlador que manejara las acciones de los servicios*/
ManageControllers.controller('recipeController', ['$scope', '$location', '$routeParams', 'Recipe', recipeController]);

    function recipeController($scope, $location, $routeParams, Recipe){
        
    	/* Hacemo una consulta y le pasamos el nombre de la receta */
        $scope.Params = Recipe.get({name:$routeParams.name});
 
	    /* Funcion para desplegar el servicio */
		$scope.deployService = function(config) {
	        
	        /* Ejecutamos la funcion save del servicio pasandole la lista
	           de parametros */
	        Recipe.save({
	            config: config
	        },
	        function(resp, headers){
	          //success callback
	          console.log(resp);
	          $location.path('/');
	        },
	        function(err){
	          // error callback
	          console.log(err);
	        });
	    }; 

          
    }

