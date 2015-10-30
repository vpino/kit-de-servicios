// Declare use of strict javascript
'use strict';

// Application -----------------------------------------------------------------

// var tribus = angular.module('tribus', ['ui.bootstrap', 'ngDragDrop', 'ngPanzoom', 'ngPanzoomwidget',
//                                        'ServicesList', 'ServicesMetadata', 'ConsulNodes', 'Deploy']);

var tribus = angular.module('tribus', ['ui.bootstrap', 'ngDragDrop', 'ngPanzoom', 'ngPanzoomwidget',
                                       'ServicesList', 'ServicesMetadata', 'ServicesConfig', 'Deploy']);

// Controllers -----------------------------------------------------------------

// tribus.controller('kitController', ['$scope', 'ServicesList', 'ServicesMetadata', 'ConsulNodes',
//                                     'Deploy', '$modal', '$log', kitController]);

tribus.controller('kitController', ['$scope', 'ServicesList', 'ServicesMetadata', 'ServicesConfig',
                                    'Deploy', '$modal', '$log', kitController]);

// Directive -------------------------------------------------------------------

tribus.directive('backImg', function(){
    return function(scope, element, attrs){
        var url = attrs.backImg;
        element.css({
            'background-image': 'url(' + url +')'
        });
    };
});

tribus.directive('myDraggable', ['$document', function($document) {
      return function(scope, element, attr) {
        var startX = 0, startY = 0, x = 0, y = 0;

        element.css({
         position: 'relative',
         /*border: '1px solid red',
         backgroundColor: 'lightgrey',*/
         cursor: 'pointer'
        });

        element.on('mousedown', function(event) {
          // Prevent default dragging of selected content
          event.preventDefault();
          startX = event.pageX - x;
          startY = event.pageY - y;
          $document.on('mousemove', mousemove);
          $document.on('mouseup', mouseup);
        });

        function mousemove(event) {
          y = event.pageY - startY;
          x = event.pageX - startX;
          element.css({
            top: y * 2 + 'px',
            left: x * 2 + 'px'
          });
        }

        function mouseup() {
          $document.off('mousemove', mousemove);
          $document.off('mouseup', mouseup);
        }
      };
    }]);

tribus.directive('removeMe', function() {
      return {
            link:function($scope,element)
            {
                $scope.remove = function() {
                element.remove();
                };
            }
      }
});