// Declare use of strict javascript
'use strict';

//function kitController($scope, ServicesList, ServicesMetadata, ConsulNodes, Deploy, $modal, $log){
function kitController($scope, ServicesList, ServicesMetadata, Deploy, $modal, $log){
    $scope.servicios = [''];

    //var nodes = ConsulNodes.query({});

    //console.log(nodes);

    var result = ServicesList.query({}, function (){
        var ruta_base = 'tribus/tribus/data/services/';
        var icon = '/icon.svg'
        
        $scope.serviciolist = result[0].services;
        $scope.services = [];

        for(var i = 0; i < $scope.serviciolist.length; i++){
            ServicesMetadata.query({name: $scope.serviciolist[i]}, function(results){
                $scope.services.push({
                    name : results[0].name,
                    description : results[0].description,
                    maintainer : results[0].maintainer,
                    icon : ruta_base + results[0].name + icon,
                    summary : results[0].summary
                });
            }); 
        }
    });
	
    $scope.dropSuccessHandler = function($event, index, servicios){
        servicios.splice(index, 1);
    };
    
    $scope.onDrop = function($event, $data, servicios){
        servicios.push($data);
    };

    // Menu Toggle Script -->
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });

    //PAN ZOOM Controller
    var shark = { x : 391, y: 371, width: 206, height: 136 };
    var chopper = { x : -200, y: 180, width: 850, height: 500 };
    var ladder = { x : 333, y: 325, width: 75, height: 200 };

    $scope.rects = [chopper, shark, ladder];

    // Instantiate models which will be passed to <panzoom> and <panzoomwidget>

    // The panzoom config model can be used to override default configuration values
    $scope.panzoomConfig = {
        zoomLevels: 7,
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

    //MODAL INFORMACION DE SERVICIO
  	$scope.open = function (size, name) {
	    var modalInstance = $modal.open({
            templateUrl: 'serviceInfo.html',
	      	controller: 'ServiceInfoController',   
	      	size: size,
	      	resolve: {
	        	servicedata: function () {
	    			var data = ServicesMetadata.query({name: name});
					return data
	        	}
	      	}
	    });
  	};

    //MODAL DESPLIEGUE DE SERVICIO
  	$scope.opendeploy = function (name) {
	    var modalInstance = $modal.open({ 
	      	templateUrl: 'serviceDeploy.html',
	      	controller: 'ServiceDeployController',   
	      	resolve: {
	        	servicedata: function () {
	    			var data = ServicesMetadata.query({name: name});
					return data
	        	},

	        	id : function() {
	        		return $('#'+name);
	        	}
	      	}
	    });
  	};	 	
}

function ServiceInfoController($scope, $modalInstance, servicedata){
	$scope.servicedata = servicedata;
	$scope.cancel = function () {
        $modalInstance.dismiss('cancel');
  	};
}

function ServiceDeployController($scope, $modalInstance, Deploy, servicedata, id){

	$scope.servicedata = servicedata
	$scope.serviceid = id

    $scope.ok = function(user) {
        Deploy.save({user: user.name, pw: user.password, name: $scope.servicedata[0].name});
        $modalInstance.dismiss('ok');
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

    $scope.remove = function() {
        $scope.serviceid.remove();
        $modalInstance.dismiss('delete');
    };
}
