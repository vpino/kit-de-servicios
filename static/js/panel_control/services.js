'use strict';

/* Services */

/* Declaramos el modulo que gestionara los servicios */
var ManageServices = angular.module('ManageServices', ['ngResource']);

/* Declaramos una factory que se encargara del CRUD de una Receta*/
ManageServices.factory('Recipe', ['$resource',
  function($resource){
    return $resource('/ServiceConfigResource/', {}, {
      
      /* Funcion que retorna un json con los parametros que 
         necesita una receta*/
      query: {
        params: {name: '@name'},
      	method:'GET',  
      	isArray:true,
        transformResponse: function(data){
               return angular.fromJson(data).objects;
           }
      	},

      /* Funcion que despliega una Receta */
      save: {
            params: {config: '@config'},
            method: 'POST'
        }


    });
  }]);


/* Declaramos una factory que se encargara de la consulta de servicios */
ManageServices.factory('Status', ['$resource',
  function($resource){
    return $resource('/ServiceStatus/', {}, {
      
      /* Funcion que consulta si un servicio
         esta o no instalado */
      query: {
        params: {name: '@name', host: '@host'},
        method:'GET',  
        isArray:true,
        transformResponse: function(data){
               return angular.fromJson(data).objects;
           }
        },

      


    });
  }]);

