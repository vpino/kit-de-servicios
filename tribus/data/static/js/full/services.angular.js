// Declare use of strict javascript
'use strict';

// Services --------------------------------------------------------------------

angular.module('CharmsList', ['ngResource'])
.factory('CharmsList',  function($resource){
    return $resource('/api/0.1/charms/list/',{}, {
            query: {
                method: 'GET',
                isArray: true,
                transformResponse: function(data){
                    return angular.fromJson(data).objects;
                },
            },
        });
});

angular.module('CharmMetadata', ['ngResource'])
.factory('CharmMetadata',  function($resource){
    return $resource('/api/0.1/charms/metadata/',
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
    //return $resource('/api/0.1/services/deploy/:user:pw',
    return $resource('/api/0.1/services/deploy/',
        { user: '@user', pw: '@pw'}, {
        save: {
            method: 'POST',
            headers: {
                'X-CSRFToken': angular.element(document.querySelector('input[name=csrfmiddlewaretoken]')).val()
            },
        }
    });
});
