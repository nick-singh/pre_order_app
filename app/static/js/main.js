(function(){

	'use strict';


	angular.module('pre',
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