/**
 * Created by rotem on 7/11/15.
 */
/*global angular*/
(function () {
  'use strict';
  angular.module('login')
    .controller('loginCtrl',
      ['$scope', '$http', '$window',
        function ($scope, $http, $window) {
          $scope.username = null;
          $scope.password = null;

          $scope.submit = function () {
            console.log($scope.username, $scope.password)
            $http.post('login', {username: $scope.username, password: $scope.password}).then(
              function (response) {
                if (response.data.status === 'success') {
                  $window.location.replace('/admin');
                } else {
                  $scope.error = response.data.msg;
                }
              },
              function (error) {
                $scope.error =  error.statusText;
              }
            );
          };
        }]);
}());
