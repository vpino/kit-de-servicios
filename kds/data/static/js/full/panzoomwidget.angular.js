angular.module('ngPanzoomwidget', [])
.directive('panzoomwidget', ['$document', function($document) {
	return {
		restrict: 'E',
		transclude: true,
		scope: {
			config: '=',
			model: '='
		},
		controller: ['$scope', function($scope) {
			//var zoomSliderWidget = $element.find('.zoom-slider-widget');
			var zoomSliderWidget = angular.element('.zoom-slider-widget');

			var isDragging = false;

			var sliderWidgetTopFromZoomLevel = function(zoomLevel) {
				return (($scope.config.zoomLevels - zoomLevel - 1) * $scope.widgetConfig.zoomLevelHeight);
			};

			var zoomLevelFromSliderWidgetTop = function(sliderWidgetTop) {
				return $scope.config.zoomLevels - 1 - sliderWidgetTop/$scope.widgetConfig.zoomLevelHeight;
			};

			var getZoomLevelForMousePoint = function($event) {
				//var sliderWidgetTop = $event.pageY - $element.find('.zoom-slider').offset().top - $scope.widgetConfig.zoomLevelHeight/2;
				var sliderWidgetTop = $event.pageY - angular.element('.zoom-slider').offset().top - $scope.widgetConfig.zoomLevelHeight/2;
				return zoomLevelFromSliderWidgetTop(sliderWidgetTop);
			};

			$scope.getZoomLevels = function() {
				var zoomLevels = [];
				for (var i = $scope.config.zoomLevels - 1; i >= 0; i--) {
					zoomLevels.push(i);
				}
				return zoomLevels;
			};

			$scope.widgetConfig = {
				zoomLevelHeight : 10
			};

			$scope.zoomIn = function() {
				$scope.model.zoomIn();
			};

			$scope.zoomOut = function() {
				$scope.model.zoomOut();
			};

			$scope.onClick = function($event) {
				var zoomLevel = getZoomLevelForMousePoint($event);
				$scope.model.changeZoomLevel(zoomLevel);
			};

			$scope.onMousedown = function() {
				isDragging = true;

				$document.on('mousemove', $scope.onMousemove);
				$document.on('mouseup', $scope.onMouseup);
			};

			$scope.onMousemove = function($event) {
				$event.preventDefault();
				var zoomLevel = getZoomLevelForMousePoint($event);
				$scope.model.changeZoomLevel(zoomLevel);
			};

			$scope.onMouseup = function() {
				isDragging = false;

				$document.off('mousemove', $scope.onMousemove);
				$document.off('mouseup', $scope.onMouseup);
			};

			$scope.onMouseleave = function() {
				isDragging = false;
			};

			// $watch is not fast enough so we set up our own polling
			setInterval(function() {
				zoomSliderWidget.css('top', sliderWidgetTopFromZoomLevel($scope.model.zoomLevel) + 'px');
			}, 25);
		}],
		template:
			'<div class="panzoomwidget">' +
				'<div ng-click="zoomIn()" ng-mouseenter="zoomToLevelIfDragging(config.zoomLevels - 1)" class="zoom-button zoom-button-in">+</div>' +
				'<div class="zoom-slider" ng-mousedown="onMousedown()" ' +
						'ng-click="onClick($event)">' +
					'<div class="zoom-slider-widget" style="height:{{widgetConfig.zoomLevelHeight - 2}}px"></div>' +
					'<div ng-repeat="zoomLevel in getZoomLevels()" "' +
					' class="zoom-level zoom-level-{{zoomLevel}}" style="height:{{widgetConfig.zoomLevelHeight}}px"></div>' +
				'</div>' +
				'<div ng-click="zoomOut()" ng-mouseenter="zoomToLevelIfDragging(0)" class="zoom-button zoom-button-out">-</div>' +
				'<div ng-transclude></div>' +
			'</div>',
		replace: true
	};
}]);
