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
.factory('ServicesMetadata',  function($resource){
    return $resource('/api/0.1/services/metadata/',
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

angular.module('Deploy', ['ngResource'])
.factory('Deploy',  function($resource){
    return $resource('/api/0.1/services/deploy/',
        {user: '@user', pw: '@pw', name: '@name'}, {
        save: {
            method: 'POST',
            headers: {
                'X-CSRFToken': angular.element(document.querySelector('input[name=csrfmiddlewaretoken]')).val()
            },
        }
    });
});
