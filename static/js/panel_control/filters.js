'use strict';

var ManageFilters = angular.module('ManageFilters', []);

ManageFilters.filter('spaceless', spaceless);

    /* Funcion que sustituye espacio por guiones */
    function spaceless() {

	    return function(input) {
        
	        if (input) {
	            return input.replace(/\s+/g, '-');    
	        }
	        
	    }

    }
