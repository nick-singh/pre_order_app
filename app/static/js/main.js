(function(){

	'use strict';


	angular.module('REB',
	[
		'ngRoute',
		'ui.bootstrap'
	])

	.controller("ApplicationController", function($scope, $window){
		console.log('main controller');
	})

	.config(['$routeProvider',
		function($routeProvider){
			
		}
	])



}());