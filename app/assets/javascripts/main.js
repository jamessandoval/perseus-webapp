var app = angular.module('crawlerApp', []);

app.controller('MainCtrl', ['$scope', '$location', '$window', '$cookies'function($scope, $location, $window, $cookies) {
    // word validation
    $scope.sample = {
        word: /^\s*\w*\s*$/
    };

    // Submit Button handler
    var self = this;

    self.submit = function($scope) {
        console.log("User clicked submit with ", self.entry.url);
        console.log("User clicked submit with ", self.entry.keyword);
        console.log("User clicked submit with ", self.entry.max);
        console.log("User clicked submit with ", self.entry.crawloption);

        $cookies.putObject('myCookieArray', { 'url': self.entry.url, 'keyword': self.entry.keyword, 
        'max': });

        getmycookiesback = $cookies.get('myCookieArray');
        console.log(getmycookiesback.key1);

        $location.path('/viewer');
        $location.replace();
        $window.location.href = $location.path();
    };

}]);