'use strict';

/* Controllers */

/* Declaro el modulo ManageCOntrollers*/
var ManageControllers = angular.module('ManageControllers', []);

/**
* @name recipeController
* @desc Controlador que manejara las acciones de los servicios
*/
ManageControllers.controller('recipeController', ['$scope', '$location', '$routeParams', 'Recipe', 'WSService', 'dataService', '$window', recipeController]);

    function recipeController($scope, $location, $routeParams, Recipe, WSService, dataService, $window){
        
        /** 
		* Variable que controla cuando mostrar el 
		* div de autorizacion de operaciones 
		*/
		$scope.authorization = true;

		/**
		* Varaible que controla cuando mostrar el 
		* boton para ejecutar el update del servicio 
		*/
		$scope.deploy = true;

		/**
		* Varaible que controla cuando mostrar el 
		* log de las operaciones
		*/
		$scope.log = false;

		/**
		* Varaible que controla cuando finaliza el 
		* el despliegue de la receta 
		*/
		$scope.finnish = false;

        /**
	    * @desc Funcion que retorna al home cuando se oprime el boton de atras y siguiente
        * @param {event} popstate Evento
	    */
        $window.addEventListener("popstate", function(event){
      		$location.path('/');
      		$scope = $scope.$new(true);
      	});

        $scope.datos = dataService.getData()

		if ('{}' === JSON.stringify($scope.datos) ){
			$location.path('/');
		}

		/**
	    * @name Recipe
	    * @desc Funcion para obetener los parametros de la receta 
        * @param {string} name Nombre de la receta
        * @param {string} action Accion que se debe ejecutar
	    */
        Recipe.get({name:$scope.datos.recipe, action:$scope.datos.action})
        .$promise.then(recipeSuccess, recipeError);

        	/**
			* @name recipeSuccess
			* @desc Funcion que retorna la data de la receta
    		*/ 
        	function recipeSuccess(data, status, headers, config) { 
				$scope.Params = data;
        		$scope.Params.ipadd = $scope.datos.ip;
        		$scope.Params.username = "victor"; 
			}

			/**
			* @name recipeError
			* @desc Funcion que retorna el error de la peticion
    		*/
			function recipeError(data, status, headers, config){

				console.log(data.message);
			}
      			
	    /**
	    * @name deployService
	    * @desc Funcion para desplegar el servicio 
        * @param {Diccionario} config La configuracion de la receta con todos sus parametros
        * @param {string} action Accion que se debe ejecutar
	    */
		$scope.deployService = function(config, action) {

			$scope.logger = '';
        
        	/**
		    * @name deployService
		    * @desc Funcion para implementar el log
		    */
        	WSService.logplay().then(connectSuccess, closetSuccess, notifySucces);

        		/**
				* @name connectSuccess
				* @desc Funcion que retorna el inicio de la conexion con el socket
        		*/ 
				function connectSuccess(evt) { 
					console.log('resolve : ' + evt); 
				}

				/**
				* @name closetSuccess
				* @desc Funcion que retorna el inicio de la conexion con el socket
        		*/ 
				function closetSuccess(evt) { 
					console.log('reject : ' + evt); 
				}
                    
                /**
				* @name notifySucces
				* @desc Funcion que retorna las notificaciones del socket
        		*/ 
				function notifySucces(evt) {
					
					$scope.logger = $scope.logger.concat(evt);
				     
				}

			config.campos[0]['action'] = action;
				        
			/**
			* @desc ForEach para reeconstruir la lista de campos que recibe el Runner 
			* @param {Diccionario} config.campos Lista de los parametros del recipe
    		*/ 
			angular.forEach(config.campos, function(campos) {

				config.campos[0][campos.name] =  campos.default;

			});

			$scope.log = true;
			$scope.authorization = false;
	    	$scope.deploy = false;

			/**
			* @name save
			* @desc Funcion para ejecutar un playbook
			* @param {Diccionario} config Diccionario con toda la data para ejecutar un playbook
    		*/ 
	        Recipe.save({config: config}).$promise.then(saveSuccess, saveError);
	        
	        /**
			* @name saveSuccess
			* @desc Funcion 
			* @param {string} resp Data que retorna la ejecucion correcta
    		*/
	        function saveSuccess(resp, headers){

				$scope.respuesta = resp;
				$scope.finnish = true;

	        }

	        /**
			* @name saveError
			* @desc Funcion que retorna los errores de la ejecución
			* @param {string} err Error
    		*/
	        function saveError(err){

				$scope.respuesta = err;
				$scope.finnish = true;

	        }
	    }
    }

/**
* @name statusServiceController
* @desc Controlador que manejara el status de los servicios
*/
ManageControllers.controller('statusServiceController', ['$scope', '$location', '$routeParams', 'Status', 'dataService', '$window', statusServiceController]);

	function statusServiceController($scope, $location, $routeParams, Status, dataService, $window){

		/**
	    * @desc Funcion que retorna al home cuando se oprime el boton de atras y siguiente
        * @param {event} popstate Evento
	    */
		$window.addEventListener("popstate", function(event){
      		$location.path('/');
      		$scope = $scope.$new(true);
      	});

       	$scope.ip = '';

       	/**
       	* Variable que controla el mensaje de "confirmando status"
       	*/
       	$scope.confirm_status = false;

       	/**
       	* Variable que controla si esta instalado o no el servicio
       	*/
       	$scope.status_service = false;

       	/**
       	* Variable que controla cuando mostrar las operaciones disponibles
       	*/
       	$scope.operations = false;

       	/**
       	* $scope.name Nombre del servicio a instalar, actualizar etc.
       	*/
       	$scope.name = $routeParams.name;

       	/**
       	* $scope.servicioStatus {Diccionario} Que contiene la data del estado del servicio
       	*/
       	$scope.servicioStatus = {};

       	/**
       	* @name queryState
	    * @desc Funcion para consultar el estado del servicio en un host
	    */
        $scope.queryState = function() {
        	
        	$scope.operations = false;
        	$scope.status_service = false;
        	$scope.confirm_status = true;
        	$scope.servicioStatus.error = '';

        	/**
			* @name save
			* @desc Funcion para consultar el status del servicio
			* @param {string} name El nombre del servicio.
    		* @param {string} ip La ip de la maquina.
    		*/ 
        	Status.get({name:$routeParams.name, host:$scope.ip})
        	.$promise.then(statusSuccess, statusError);

        	function statusSuccess(data){

				$scope.servicioStatus = data;

				$scope.servicioStatus.recipe = $routeParams.name;

				$scope.servicioStatus.ip = $scope.ip;

				/**
				* @name setData
				* @desc Funcion para setear el status del host
				* @param {Diccionario} servicioStatus Diccionario con la data del host 
	    		*/ 
				dataService.setData($scope.servicioStatus);

				/**
				* @name forEach
				* @desc Funcion Hacemos una validacion para saber que botones (instalar, desintalar etc) 
				mostrar en la interfaz
				* @param {Diccionario} servicioStatus Diccionario con los servicios. 
	    		*/ 
				angular.forEach($scope.servicioStatus.services, function(services) {

					if(services.status == 'Instalado'){

						$scope.status_service = true;


					} else {

						$scope.status_service = false;
					}

				});

				$scope.confirm_status = false;
				$scope.operations = true;

        	}

        	/**
			* @name statusError
			* @desc Funcion que retorna los errores de la ejecución
			* @param {string} err Error
    		*/
        	function statusError(err){

        		$scope.servicioStatus.error = err;

        	}
      
        }

        /**
		* @name routeState
		* @desc Funcion que redirecciona a la pagina indicada
		* @param {string} route  
		* @param {string} ip Direccion ip del host donde sea desea realizar la acción 
		* @param {string} action Accion que se quiere realizar
		*/
        $scope.routeState = function(route, name, ip, action){

        	$scope.servicioStatus.action = action;

       		dataService.setData($scope.servicioStatus);

       		switch (route) {
			    case 'recipe':
			        $location.path('/recipe/');
			        break;
			    case 'update':
			        $location.path('/update/');
			        break;
			    case 'delete':
			        $location.path('/delete/');
			        break;
			    case 'query':
			        $location.path('/query/');
			        break;
			    default:
        			$location.path('/');
			} 

    	}

	}

/**
* @name queryServiceController
* @desc Controlador que maneja el reinicio de los servicios.
*/
ManageControllers.controller('queryServiceController', ['$scope', '$location', '$routeParams', 'Status', 'dataService', '$window', queryServiceController]);

	function queryServiceController($scope, $location, $routeParams, Status, dataService, $window){

		/**
	    * @desc Funcion que retorna al home cuando se oprime el boton de atras y siguiente
        * @param {event} popstate Evento
	    */
		$window.addEventListener("popstate", function(event){
      		$location.path('/');
      		$scope = $scope.$new(true);
      	});

		/**
		* @desc Function que nos devuelve toda la data de la receta a consultar
		*/
		$scope.data = dataService.getData()

		$scope.Params = {};

		$scope.Params.passwd = '';
		$scope.Params.username = 'victor';

		$scope.confirmPassword = '';

		/**
		* @desc Variable que controla cuando mostrar la autorizacion de las operaciones.
		*/
		$scope.authorization = true;

		/**
		* @desc Variable que controla el exito de la operacion
		*/
		$scope.success = false;

		/**
		* @desc Variable que controla el mensaje de ejecutando el reinicio
		*/
		$scope.execution = false;

		/**
        * @desc Funcion que te retorna al home, si la variable datos viene vacía.
        */
		if ('{}' === JSON.stringify($scope.data) ){
			$location.path('/');
		}
		
		
		/**
		* @name queryService
		* @desc Funcion para consultar los servicios
		*/
    	$scope.queryService = function() {

    		$scope.execution = true;

    		$scope.success = false;
    		$scope.data.error = '';

    		$scope.data.passwd = $scope.Params.passwd;
 
        	/**
			* @name save
			* @desc Funcion para consultar los servicios
			* @param {Diccionario} data Diccionario con toda la data para consultar los servicios
    		*/ 
	        Status.save({config: $scope.data})
	        .$promise.then(saveSuccess, saveError);
	        
	        /**
			* @name saveSuccess
			* @desc Funcion 
			* @param {string} resp Data que retorna la ejecucion correcta
    		*/
	        function saveSuccess(resp, headers){

	        	$scope.data = resp;
				$scope.success = true;
				$scope.execution = false;
				$scope.Params.passwd = '';
				$scope.confirmPassword = '';

	        }

	        /**
			* @name saveError
			* @desc Funcion que retorna los errores de la ejecución
			* @param {string} err Error
    		*/
	        function saveError(err){

				$scope.data.eror = err;
				$scope.execution = false;
				$scope.Params.passwd = '';
				$scope.confirmPassword = '';

	        }

	        

    	}

    }

/**
* @name keyController
* @desc Controlador que maneja las llaves ssh.
*/
ManageControllers.controller('keyController', ['$scope', 'Roles', keyController]);

	function keyController($scope, Roles){

		/**
		* @name get
		* @desc Funcion para consultar la llave ssh del servidor
		* @param {string} resp Data que retorna la llave ssh
		*/
    	Roles.get().$promise.then(RolesSuccess, RolesError);

		/**
		* @name RolesSuccess
		* @desc Funcion que retorna la llave ssh
		* @param {string} resp Data que retorna la llave ssh
		*/
		function RolesSuccess(resp, headers){

			$scope.key = data;

		}

		/**
		* @name RolesError
		* @desc Funcion que retorna los errores de la consulta
		* @param {string} err Error
		*/
		function RolesError(err){

			$scope.error = err;

		}
    	
    }

/**
* @name RolController
* @desc Controlador la lista de las recetas
*/
ManageControllers.controller('RolController', ['$scope', 'Roles', RolController]);

	function RolController($scope, Roles){

		/**
		* @name get
		* @desc Funcion para consultar las recetas 
		* @param {string} resp Data que retorna las recetas
		*/
    	Roles.get().$promise.then(RolesSuccess, RolesError);

		/**
		* @name RolesSuccess
		* @desc Funcion que retorna la receta
		* @param {string} resp Data que retorna la llave ssh
		*/
		function RolesSuccess(resp, headers){

			$scope.roles = resp;

		}

		/**
		* @name RolesError
		* @desc Funcion que retorna los errores de la consulta
		* @param {string} err Error
		*/
		function RolesError(err){

			$scope.error = err;

		}
    	
    }


/**
* @name recipeUpdateController
* @desc Controlador que gestiona las acciones de actualizacion de una receta
*/
ManageControllers.controller('recipeUpdateController', ['$scope', '$location', '$routeParams', 'Recipe', 'WSService', 'dataService', '$window', '$filter', recipeUpdateController]);

	function recipeUpdateController($scope, $location, $routeParams, Recipe, WSService, dataService, $window, $filter){

		$scope.Params = '';

		/** 
		* Variable que controla cuando mostrar el 
		* div de autorizacion de operaciones 
		*/
		$scope.authorization = false;

		/**
		* Varaible que controla cuando mostrar el 
		* boton para ejecutar el update del servicio 
		*/
		$scope.deploy = false;

		/**
		* Varaible que controla cuando mostrar el 
		* log de las operaciones
		*/
		$scope.log = false;

		/**
		* Varaible que controla cuando finaliza el 
		* el despliegue de la receta 
		*/
		$scope.finnish = false;



	 	/**
	    * @desc Funcion que retorna al home cuando se oprime el boton de atras y siguiente
        * @param {event} popstate Evento
	    */
        $window.addEventListener("popstate", function(event){
      		$location.path('/');
      		$scope = $scope.$new(true);
      	});

        /**
		* @desc Con el metodo getData del objeto dataService, obtenemos los parametros pasados
		* por la vista de panel, donde se pasan la ip, el nombre de la receta y la acción.
        */
        $scope.datos = dataService.getData()

        /**
        * @desc Funcion que te retorna al home, si la variable datos viene vacía.
        */
		if ('{}' === JSON.stringify($scope.datos) ){
			$location.path('/');
		}

		/**
	    * @name Recipe
	    * @desc Funcion para obetener los parametros de la receta 
        * @param {string} name Nombre de la receta
        * @param {string} action Accion que se debe ejecutar
	    */
        Recipe.get({name:$scope.datos.recipe, action:$scope.datos.action})
        .$promise.then(recipeSuccess, recipeError);

        	/**
			* @name recipeSuccess
			* @desc Funcion que retorna la data de la receta
    		*/ 
        	function recipeSuccess(data, status, headers, config) { 
				$scope.Params = data;
        		$scope.Params.ipadd = $scope.datos.ip;
        		$scope.Params.username = "victor"; 
			}

			/**
			* @name recipeError
			* @desc Funcion que retorna el error de la peticion
    		*/
			function recipeError(data, status, headers, config){

				console.log(data.message);
			}
      			

      	/**
		* @name moduleData
		* @desc Funcion que retorna la data exacta del module clickeado
		* @param {string} key Valor de la llave del modulo seleccionada
		*/
        $scope.moduleData = function(key_module){

        	$scope.module_index = $scope.Params.campos[0].modules;

        	angular.forEach($scope.module_index, function(value) {

		        if (value[key_module]){

		            	$scope.module = value[key_module];

		        	}

	    	});

	    	$scope.authorization = true;
	    	$scope.deploy = true;

    	}

    	/**
	    * @name deployService
	    * @desc Funcion para desplegar el servicio 
        * @param {Diccionario} config La configuracion de la receta con todos sus parametros
        * @param {string} action Accion que se debe ejecutar
	    */
		$scope.deployService = function(config, action) {

			/**
			* Variable donde se guardara la data
			* del log.
			*/
			$scope.logger = '';
        
        	/**
		    * @name deployService
		    * @desc Funcion para implementar el log
		    */
        	WSService.logplay().then(connectSuccess, closetSuccess, notifySucces);

        		/**
				* @name connectSuccess
				* @desc Funcion que retorna el inicio de la conexion con el socket
        		*/ 
				function connectSuccess(evt) { 
					console.log('resolve : ' + evt); 
				}

				/**
				* @name closetSuccess
				* @desc Funcion que retorna el inicio de la conexion con el socket
        		*/ 
				function closetSuccess(evt) { 
					console.log('reject : ' + evt); 
				}
                    
                /**
				* @name notifySucces
				* @desc Funcion que retorna las notificaciones del socket
        		*/ 
				function notifySucces(evt) {
					
					$scope.logger = $scope.logger.concat(evt);
				     
				}

			$scope.log = true;
			$scope.authorization = false;
	    	$scope.deploy = false;

			config.campos[0]['action'] = action;
				        
			/**
			* @desc ForEach para reeconstruir la lista de campos que recibe el Runner 
			* @param {Diccionario} config.campo Lista de las variables que recibe el recipe
    		*/ 
    		angular.forEach($scope.module, function(campo) {

				config.campos[0][campo.name] =  campo.default;

			});
			
			/**
			* @name save
			* @desc Funcion para ejecutar un playbook
			* @param {Diccionario} config Diccionario con toda la data para ejecutar un playbook
    		*/ 
	        Recipe.save({config: config}).$promise.then(saveSuccess, saveError);
	        
		        /**
				* @name saveSuccess
				* @desc Funcion 
				* @param {string} resp Data que retorna la ejecucion correcta
	    		*/
		        function saveSuccess(resp, headers){

					$scope.respuesta = resp;
					$scope.finnish = true;

		        }

		        /**
				* @name saveError
				* @desc Funcion que retorna los errores de la ejecución
				* @param {string} err Error
	    		*/
		        function saveError(err){

					$scope.respuesta = err;
					$scope.finnish = true;

		        }
	    }

    }