'use strict';
(function($){
    var $contentDiv = $('.contents'),
        $getListButton = $('#getList'),
        $clearListButton = $("#clearList");

    $getListButton.on('click', function(e){
        getPosts(e);
    });

    $clearListButton.on('click', function(){
        $contentDiv.html("");
    });

    function getPosts(e){
        e.preventDefault();
        $.get('/posts/json-list', function(data){
            response(data);
        })
    }

    function response(data){
        data.forEach(function(post){
            $contentDiv.append("<h3><a href=/posts/" + post.pk +">"+ post.fields.title +"</a></h3>");
            for (var key in post.fields){ 
                $contentDiv.append("<p>"+ key + ": " + post.fields[key] + "</p>");
            }
            $contentDiv.append("<br>");
        });
    }
}(jQuery));