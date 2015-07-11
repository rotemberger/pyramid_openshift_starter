/**
 * Created by rotem on 7/11/15.
 */
/*global angular*/
(function () {
  'use strict';
  angular.module('admin')
    .controller('logoutCtrl',
      ['$scope', '$http', '$window',
        function ($scope, $http, $window) {
          $scope.logout = function () {
            $http.post('logout').then(function (){
              $window.location.replace('/');
            });
          };
        }]
      );
}())