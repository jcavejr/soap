var change = angular.module('change', ['ngRoute']);
change.controller('MainCtrl', function($scope){

})

.config(function($routeProvider){
$routeProvider.
when('/', {
  controller:'MainCtrl'
  templateURL: 'login.html'
});
$routeProvider.
when('/landing',{
  templateURL: 'landing.html'
});
$routeProvider.
when('/createacc',{
  templateURL: 'newacc.html'
});
$routeProvider.otherwise({
  redirectTo: '/'
  controller: 'MainCtrl'
});}
