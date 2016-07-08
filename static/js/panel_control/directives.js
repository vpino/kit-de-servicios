'use strict';

var ManageDirectives = angular.module('ManageDirectives', []);

ManageDirectives.directive('passwordMatch', ['', passwordMatch]);

	function passwordMatch(){

		return {
            restrict: 'A',
            scope: true,
            require: 'ngModel',
            link: function (scope, elem, attrs, ctrl) {
                var check = function () {
                    var passMatchValue = scope.$eval(attrs.ngModel);
                    var passValue = scope.$eval(attrs.passwordMatch);
                    
                    //validar que al menos se haya escrito algo en cada campo
                    if (passMatchValue && passValue)
                        return passMatchValue === passValue;
                    return true;
                };

                //disparar al ingresarse un valor SÓLO en el input de confirmación de password
                elem.bind('keyup', function () {
                    scope.$apply(function () {
                        ctrl.$setValidity('passwordMatch', check());
                    });
                });
            }
        };

	}

