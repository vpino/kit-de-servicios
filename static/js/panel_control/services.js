'use strict';

/* Services */

var ManageServices = angular.module('ManageServices', ['ngResource']);

ManageServices.factory('Recipe', ['$resource',
  function($resource){
    return $resource('/ServiceConfigResource/', {}, {
      
      query: {
        params: {name: '@name'},
      	method:'GET',  
      	isArray:true,
        transformResponse: function(data){
               return angular.fromJson(data).objects;
           }
      	}

    });
  }]);

