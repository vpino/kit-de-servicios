'use strict';

/* Controllers */

/* Declaro el modulo ManageCOntrollers*/
var ManageControllers = angular.module('ManageControllers', []);

/* Declaro un controlador que manejara las acciones de los servicios */
ManageControllers.controller('recipeController', ['$scope', '$location', '$routeParams', 'Recipe', 'WSService', recipeController]);

    function recipeController($scope, $location, $routeParams, Recipe, WSService){
        
        $scope.status = true;
        $scope.msj = true;
        $scope.respuesta = '';
        $scope.band = false;
        $scope.msj_logger = true;
  
    	/* Funcion que retorna los parametros de una receta

			1. Recibe como parametro el nombre de la receta
			   a consultar.
    	 
    	 */
        Recipe.get({name:$routeParams.name, action:$routeParams.action})
        .$promise.then(function(data) {

        		$scope.Params = data;
        		$scope.Params.ipadd = $routeParams.host
      			
    	});
        	
	    /* Funcion para desplegar el servicio */
		$scope.deployService = function(config, action) {

			$scope.logger = ''
        
        	var promise = WSService.logplay();

        	promise.then(

        		 /* Funcion que retorna la conexion con el socket */
				function(evt) { 
					console.log('resolve : ' + evt); 
				}, 

				 /* Funcion que retorna el cierre del socket */
				function(evt) { 
					console.log('reject : ' + evt); 
				}, 
                    
                /* Funcion que retorna las notificaciones del socket */ 
				function(evt) {
					
					//Update the scope
					$scope.logger = $scope.logger.concat(evt);
				     
				}

        	);
	       
			config.campos[0]['action'] = action;
				        
			angular.forEach(config.campos, function(campos) {

			config.campos[0][campos.field_name] =  campos.default;

			});

			console.log(config.campos[0])

			$scope.status = false;
			$scope.msj = false;
			$scope.msj_logger = false;

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

ManageControllers.controller('statusServiceController', ['$scope', '$location', '$routeParams', 'Status', 'dataService', statusServiceController]);

	function statusServiceController($scope, $location, $routeParams, Status, dataService){

       	$scope.ip = '';

       	$scope.name = $routeParams.name;

       	$scope.servicioStatus = {};
       	$scope.servicioStatus.error = '';

		/* Funcion para consultar el estado del servicio en un host*/
        $scope.queryState = function() {

        	/* Le pasamos 2 parametros:
				1. El nombre del servicio.
				2. La ip de la maquina.
        	*/
        	$scope.instalado = false;
        	$scope.desintalado = false;

        	/* Consultamos el status del servicio en la ip especificada*/
        	Status.get({name:$routeParams.name, host:$scope.ip})
        	.$promise.then(function(data) {

        		$scope.servicioStatus = data;

        		$scope.servicioStatus.recipe = $routeParams.name;

        		$scope.servicioStatus.ip = $scope.ip;

        		console.log($scope.servicioStatus)

        		dataService.setData($scope.servicioStatus);
  
  				/* Hacemos una validacion para saber que botones (instalar, desintalar etc) 
  				    mostrar en la interfaz*/
        		angular.forEach($scope.servicioStatus.services, function(services) {
				
			  		if(services.status == 'Instalado'){

			  			$scope.instalado = true;
			  			$scope.desintalado = false;

			  		} else {

			  			$scope.desintalado = true;
			  			$scope.instalado = false;
			  		}

				});
			
    		});
        	
        }

	}

ManageControllers.controller('queryServiceController', ['$scope', '$location', '$routeParams', 'Status', 'dataService', queryServiceController]);

	function queryServiceController($scope, $location, $routeParams, Status, dataService){

		$scope.name = $routeParams.name;
		
		$scope.servicioStatus = dataService.getData();

		$scope.servicioStatus.error = '';

    	/* Funcion para reiniciar los servicios */
    	$scope.restartService = function() {

			/* Ejecutamos la funcion save del servicio pasandole la lista
	           de parametros */
	       Status.save({
	            data: $scope.servicioStatus
	        },
	        function(resp, headers){
				/* success callback */
				console.log(resp);
	        
	        	$scope.servicioStatus = resp;
	        	//$location.path('/');

	        },
	        function(err){
				/* error callback */
				console.log(err);

				$scope.servicioStatus = err;

	        });

    	}

    }

ManageControllers.controller('keyController', ['$scope', 'Keyssh', keyController]);

	function keyController($scope, Keyssh){

    	/* Consultamos La llave ssh */
    	Keyssh.get().$promise.then(function(data) {

    		$scope.key = data;

    		console.log($scope.key)
		
		});
    	
    }

	