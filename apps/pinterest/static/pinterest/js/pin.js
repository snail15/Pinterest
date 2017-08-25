function activateMasonary(){

    var $grid = $('.grid').imagesLoaded( function() {
        $grid.masonry({
            itemSelector: '.grid-item',
            columnWidth: '.grid-sizer',
            percentPosition: true,
            horizontalOrder: true,
            gutter: '.gutter-sizer',
        });
    });

}
function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

function activateSearch(selector) {
     $(selector).keyup(function(){
         $.ajax({
            url: 'search',
            method: 'POST',
            data: $(selector).parent().serialize(),
            success: function(serverResponse) {
                $('.pin-row').html(serverResponse)
                if (selector === '#search-bar'){
                    activateMasonary();
                }
            }
        })
    })
}

$(document).ready(function () {
   
    activateMasonary();

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    activateSearch('#search-bar');
    activateSearch('#search-user');

});