(function($){
    tile = function() {
        $("body").append('it works!');
    };

    logData = function() {
        $.get('logs/', function(data) {
            $('#logs').append(data + "<br><br>");
        });
    };

    
})(jQuery);