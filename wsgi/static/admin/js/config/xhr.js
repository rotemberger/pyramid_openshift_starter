/**
 * Created by rotem on 7/11/15.
 */
/*global angular*/
(function () {
  'use strict';
  angular.module('admin')
    .config(
      ['$httpProvider',
        function ($httpProvider) {
          $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        }]
    );
}())

