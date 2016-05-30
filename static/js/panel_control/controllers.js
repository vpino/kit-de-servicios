'use strict';

/* Controllers */

/* Declaro el modulo ManageCOntrollers*/
var ManageControllers = angular.module('ManageControllers', []);

/* Declaro un controlador que manejara las acciones de los servicios*/
ManageControllers.controller('recipeController', ['$scope', '$location', '$routeParams', 'Recipe', recipeController]);

    function recipeController($scope, $location, $routeParams, Recipe){
        
        $scope.status = true;
        $scope.msj = true;
        $scope.respuesta = '';


    	/* Hacemo una consulta y le pasamos el nombre de la receta */
        $scope.Params = Recipe.get({name:$routeParams.name});
 
	    /* Funcion para desplegar el servicio */
		$scope.deployService = function(config, action) {
	       
			config['action'] = action;

			$scope.status = false;
			$scope.msj = false;
	        
	        //console.log(config.campos);

	        /* Ejecutamos la funcion save del servicio pasandole la lista
	           de parametros */
	        Recipe.save({
	            config: config
	        },
	        function(resp, headers){
	          //success callback
	          console.log(resp);
	          $scope.msj = true;
	          $scope.respuesta = resp;
	          //$location.path('/');

	        },
	        function(err){
	          // error callback
	          console.log(err);
        	  $scope.msj = true;
        	  $scope.respuesta = resp;


	        });
	    }; 

          
    }

