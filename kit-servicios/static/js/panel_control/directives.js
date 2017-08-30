'use strict';

var ManageDirectives = angular.module('ManageDirectives', []);

ManageDirectives.directive('compareTo', compareTo);

    /* Funcion para validar las contraseñas */
    function compareTo() {

    return {
        require: "ngModel",
        scope: {
            otherModelValue: "=compareTo"
        },
        link: function(scope, element, attributes, ngModel) {

                ngModel.$validators.compareTo = function(modelValue) {
                    return modelValue == scope.otherModelValue;
                };

                scope.$watch("otherModelValue", function() {
                    ngModel.$validate();
                });

            }
        };

    }

ManageDirectives.directive('ngConfirmClick', ngConfirmClick);

    /* Funcion para confirmar acciones */
    function ngConfirmClick() {

        return {
            priority: -1,
            restrict: 'A',
            link: function(scope, element, attrs){

                element.bind('click', function(e){
                var message = attrs.ngConfirmClick;

                    // confirm() requires jQuery
                    if(message && !confirm(message)){
                        e.stopImmediatePropagation();
                        e.preventDefault();
                    }

                });
                    
            }

        }

    }

