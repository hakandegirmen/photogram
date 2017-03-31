$('button').on('click', function(event){ 
    event.preventDefault();
    var element = $(this);
    $.ajax({
        url : '/like_photograph/',
        type : 'GET',
        data : { photograph_id : element.attr("data-id")},

        success : function(response){
            element.html(' ' + response);
        }
    });
});