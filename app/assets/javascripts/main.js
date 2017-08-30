var app = angular.module('crawlerApp', ['ngCookie']);

app.controller('MainCtrl', ['$scope', '$location', '$window', 'cookies', '$http', function($scope, $location, $window, cookies, $http) {

    // scrapy crawl keyword_search -a start_url=http://www.reddit.com -a find_word=hello -s CLOSESPIDER_PAGECOUNT=10 -o breadth_example.JSON -t json

    // single word validation
    $scope.sample = {
        word: /^\s*\w*\s*$/
    };

    $scope.entries = {};

    // add the cookieStore array to the scope to view on page
    if (cookies.get('cookieStore')) {
        //$scope.entries = [];
        var storedArray = JSON.parse(cookies.get('cookieStore'));
        $scope.entries = storedArray;
    }

    // cookie reset 
    $scope.cookiereset = function() {
        cookies.set('cookieStore', "");
        $window.location.href = $location.path();

    }

    // Submit Button handler
    var self = this;

    self.submit = function() {
        console.log("User clicked submit with ", self.entry.url);
        console.log("User clicked submit with ", self.entry.keyword);
        console.log("User clicked submit with ", self.entry.max);
        console.log("User clicked submit with ", self.entry.crawloption);

        var entryStore = {
            url: self.entry.url,
            keyword: self.entry.keyword,
            type: self.entry.crawloption
        };

        // if a cookie value is set get it
        if (cookies.get('cookieStore')) {

            // take old value 
            var cookieUpdate = JSON.parse(cookies.get('cookieStore'));
            cookieUpdate.push(entryStore);
            cookies.set('cookieStore', JSON.stringify(cookieUpdate));

            // New cookie - > store it.
        } else {

            $scope.entries = [];
            $scope.entries.push(entryStore);
            cookies.set('cookieStore', JSON.stringify($scope.entries));
        }

        //127.0.0.1:33507/breadth/url/http://www.reddit.com/max/10/keyword/earth
        //127.0.0.1:33507/depth/url/http://www.reddit.com/max/10/keyword/earth


        var url = self.entry.url;
        var keyword = self.entry.keyword;
        var max = self.entry.max;
        var type = self.entry.crawloption;

        $location.path('/viewer?type='+type+'&url='+url+'&keyword='+keyword+'&max='+max+'');
        $location.replace();
        $window.location.href = $location.path();

    };

    //$scope.restart = function() {

    //}


}]);