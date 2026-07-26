// Wait for Angular to be ready
angular.element(document).ready(function() {
    // Ensure the CodexCP module exists
    if (typeof angular.module('CodexCP') === 'undefined') {
        console.error('CodexCP module not found!');
        return;
    }
    
    // Bootstrap Angular manually if needed
    var element = document.querySelector('[ng-controller="ListDockersitecontainer"]');
    if (element && !angular.element(element).data('$scope')) {
        console.log('Manually bootstrapping Angular for Docker container page');
        angular.bootstrap(element, ['CodexCP']);
    }
});