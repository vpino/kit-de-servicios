// Declare use of strict javascript
'use strict';

function kitController($scope){
	//Drag Drop
	$scope.men = [
    	'John',
      	'Jack',
      	'Mark',
      	'Ernie'
    ];
      
    $scope.women = [
    	'Jane',
      	'Jill',
      	'Betty',
      	'Mary'
    ];
          
    $scope.addText = "";
            
    $scope.dropSuccessHandler = function($event,index,array){
        array.splice(index,1);
    };
      
    $scope.onDrop = function($event,$data,array){
        array.push($data);
    };

    // Menu Toggle Script -->
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });

     //PAN ZOOM Controller
    var shark = { x : 391, y: 371, width: 206, height: 136 };
    var chopper = { x : -200, y: 180, width: 660, height: 144 };
    var ladder = { x : 333, y: 325, width: 75, height: 200 };

    $scope.rects = [ chopper, shark, ladder ];

    // Instantiate models which will be passed to <panzoom> and <panzoomwidget>

    // The panzoom config model can be used to override default configuration values
    $scope.panzoomConfig = {
        zoomLevels: 8,
        neutralZoomLevel: 3,
        scalePerZoomLevel: 1.5,
        initialZoomToFit: chopper
    };

    // The panzoom model should initialle be empty; it is initialized by the <panzoom>
    // directive. It can be used to read the current state of pan and zoom. Also, it will
    // contain methods for manipulating this state.
    $scope.panzoomModel = {};

    $scope.zoomToShark = function() {
        $scope.panzoomModel.zoomToFit(shark);
    };

    $scope.zoomToChopper = function() {
        $scope.panzoomModel.zoomToFit(chopper);
    };

    $scope.zoomToLadder = function() {
        $scope.panzoomModel.zoomToFit(ladder);
    };


    $scope.mouseover = function(){
        //console.log("true");
        //$cookieStore.put('over', true);
        localStorage.setItem("over", "true");
        //console.log($cookieStore.get('over'));
    };

    $scope.mouseleave = function(){
        //console.log("false");
        //$cookieStore.put('over', false);
        localStorage.setItem("over", "false");
        //console.log($cookieStore);
        //console.log($cookieStore.get('over'));
    };
}