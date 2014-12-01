// Declare use of strict javascript
'use strict';

function kitController($scope, CharmsList, CharmMetadata, $modal, $log){
	//Drag Drop         
    $scope.addText = "";

    $scope.serviceinstall = [''];

    var result = CharmsList.query({}, function (){
        
        var ruta_base = 'tribus/tribus/data/charms/';
        var icon = '/icon.svg'
        
        $scope.serviciolist = result[0].charms;
        //$scope.serviciolist = result[0].services;
        $scope.charms = [];

        for(var i = 0; i < $scope.serviciolist.length; i++){
            CharmMetadata.query({name: $scope.serviciolist[i]}, function(results){
                //console.log(results);
                $scope.charms.push({
                    name : results[0].name,
                    description : results[0].description,
                    maintainer : results[0].maintainer,
                    icon : ruta_base + results[0].name + icon,
                    summary : results[0].summary
                });
                //console.log($scope.charms);
            }); 
        }
    });
	           
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

    //MODAL

    $scope.datos = [];
  	
  	$scope.open = function (size, name) {
	    var modalInstance = $modal.open({ 
	      	templateUrl: 'myModalContent.html',
	      	controller: 'ModalController',   
	      	size: size,
	      	resolve: {
	        	data: function () {
	    			var data = CharmMetadata.query({name: name});
					return data
	        	}
	      	}
	    });

    // modalInstance.result.then(function (selectedItem) {
    //   $scope.selected = selectedItem;
    // }, function () {
    //   $log.info('Modal dismissed at: ' + new Date());
    // 	});
  	};	 	
}

function ModalController($scope, $modalInstance, data){
	
	$scope.data = data

	$scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  	};

  	// $scope.ok = function () {
   //  $modalInstance.close($scope.selected.item);
  	// };

}