var app = angular.module('crawlerApp', ['ngCookie']);

app.controller('MainCtrl', ['$scope', '$location', '$window', 'cookies', function($scope, $location, $window, cookies) {
    // word validation
    $scope.sample = {
        word: /^\s*\w*\s*$/
    };

    // add the cookieStore array to the scope to view on page
    if(cookies.get('cookieStore')){

    	$scope.entries = [];
    	var storedArray = JSON.parse(cookies.get('cookieStore'));
    	$scope.entries = storedArray;

    }

    // cookie reset 
    $scope.cookiereset = function(){
    	cookies.set('cookieStore', "");
    	// temporary page reload
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
        if(cookies.get('cookieStore')){

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

    
        /*
        $.ajax({
            type: "POST",
            url: "~/keywordSearch/scrapy crawl keyword_search -a start_url=http://www.reddit.com -a find_word=hello -s CLOSESPIDER_PAGECOUNT=10 -o testoutput.JSON -t json",
            data: { param: "text" }
        }).done(function(o) {
            console.log("data returned");
        });

        */
        $window.location.href = $location.path();
        //$location.path('/viewer');
        //$location.replace();
        //$window.location.href = $location.path();
    };

}]);