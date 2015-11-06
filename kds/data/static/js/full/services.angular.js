// Declare use of strict javascript
'use strict';

// Services --------------------------------------------------------------------

angular.module('ServicesList', ['ngResource'])
.factory('ServicesList', function($resource){
    return $resource('/api/0.1/services/list/',{}, {
            query: {
                method: 'GET',
                isArray: true,
                transformResponse: function(data){
                    return angular.fromJson(data).objects;
                },
            },
        });
});

angular.module('ServicesMetadata', ['ngResource'])
.factory('ServicesMetadata', function($resource){
    return $resource('/api/0.1/service/metadata/',
        {}, {
            query: {
                method: 'GET',
                isArray: true,
                transformResponse: function(data){
                    return angular.fromJson(data).objects;
                },
            },
        });
});

angular.module('ServicesConfig', ['ngResource'])
.factory('ServicesConfig', function($resource){
    return $resource('/api/0.1/service/config/',
        {}, {
            query: {
                method: 'GET',
                isArray: true,
                transformResponse: function(data){
                    var objects = angular.fromJson(data).objects;
                    return objects;
                },
            },
        });
});

angular.module('Deploy', ['ngResource'])
.factory('Deploy',  function($resource){
    return $resource('/api/0.1/service/deploy/',
        {config: '@config'}, {
        save: {
            method: 'POST',
            headers: {
                'X-CSRFToken': angular.element(document.querySelector('input[name=csrfmiddlewaretoken]')).val()
            },
        }
    });
});
