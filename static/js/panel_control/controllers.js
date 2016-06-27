'use strict';

/* Controllers */

/* Declaro el modulo ManageCOntrollers*/
var ManageControllers = angular.module('ManageControllers', []);

/* Declaro un controlador que manejara las acciones de los servicios */
ManageControllers.controller('recipeController', ['$scope', '$location', '$routeParams', 'Recipe', 'Status', '$q', 'WSService', recipeController]);

    function recipeController($scope, $location, $routeParams, Recipe, Status, WSService, $q){
        
        var promise = WSService.promise($q);

        	promise.then(

				function(evt) { 
					console.log('resolve : ' + evt); 
				}, 

				function(evt) { 
					console.log('reject : ' + evt); 
				}, 
                     
				function(evt) {
					console.log('notify: ' + evt);

					//Update the scope
					$scope.logger = evt;
				     
				    }

        		);

        $scope.status = true;
        $scope.msj = true;
        $scope.respuesta = '';
        $scope.band = false;

    	/* Hacemo una consulta y le pasamos el nombre de la receta */
        $scope.Params = Recipe.get({name:$routeParams.name});

        /* Funcion para consultar el estado del servicio en un host*/
        $scope.consultState = function() {

        	/* Le pasamos 2 parametros:
				1. El nombre del servicio.
				2. La ip de la maquina.
        	*/
        	$scope.servicioStatus = Status.get({name:$routeParams.name, host:$scope.Params.ipadd});

        	if ($scope.servicioStatus.status == 'Instalado'){

        		$scope.instalado = true;

        	} else {

        		$scope.desintalado = true;
        	}
        }
 
	    /* Funcion para desplegar el servicio */
		$scope.deployService = function(config, action) {
	       
	        config.campos[0]['action'] = action;
	        
	        angular.forEach(config.campos, function(campos) {
		    
		    config.campos[0][campos.field_name] =  campos.default;

		  	});

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
	          $scope.band = true;
	          $scope.respuesta = resp;
	          //$location.path('/');

	        },
	        function(err){
	          // error callback
	          console.log(err);
        	  $scope.msj = true;
        	  $scope.band = true;
        	  $scope.respuesta = err;


	        });
	    }; 

	    /* Funcion para consultar el WebSocket */
		$scope.WSServiceConsult = function() {
	       
			var promise = WSService.promise($q);

        	promise.then(

				function(evt) { 
					console.log('resolve : ' + evt); 
				}, 

				function(evt) { 
					console.log('reject : ' + evt); 
				}, 
                     
				function(evt) {
					console.log('notify: ' + evt);

					//Update the scope
					$scope.logger = evt;
				     
				    }

        		);

		};
          
    }

