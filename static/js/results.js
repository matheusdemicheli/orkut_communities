function calculate_container_img_size(){

    var i, container_img, container_result_height, container_result;
    var containers = $('div.result:not(.checked)');
    var containers_img = containers.find('.container-img');

    for(i=0; i<containers_img.length; i++){

            container_img = containers_img[i];
            container_result = container_img.parentElement
            container_result_height = '';

            while(container_result_height != $(container_result).height()){

                container_result_height = $(container_result).height()
                container_img.style.height = container_result_height + "px";
            }
    }

    containers.addClass('checked');
}


function loadResults(){

    obj = $('#find-input');

    $.ajax({
        type: "GET",
        url: "results/" + obj.val(),

        success:function(data) {
             document.getElementById("results").innerHTML = data;
        }
    })

    $('#find-input-bottom').val(obj.value);
}


window.onload = function() {

    $(document).ajaxComplete(function() {
        calculate_container_img_size();
    });

    var obj_input = $('#find-input');

    var typingTimer;
    var doneTypingInterval = 1000;

    obj_input.keyup(function(){
        clearTimeout(typingTimer);
        typingTimer = setTimeout(loadResults, doneTypingInterval);
    });

    obj_input.keydown(function(){
        clearTimeout(typingTimer);
    });

    obj_input.keypress(function(e) {
        if(e.which == 13) {
            clearTimeout(typingTimer);
            loadResults();
        }
    });

    var check_scroll = true;
    var focus_first = true;

    var more = function(){
        $(this).animate({ width: "30%" }, 'slow');
    }

    var less = function(){
        $(this).animate({ width: "10%" }, 'slow');
    }

    $(window).scroll(function (event) {

        var scroll = $(window).scrollTop();
        var obj = $('#find-input');

        if (check_scroll && scroll > 434){
            check_scroll = false;

            obj.css('width', '');
            obj.blur();
            obj.addClass('fixed-search');
            obj.bind('blur', less);
            obj.bind('focus', more);


            if (focus_first){

                focus_first = false;
                obj.focus();
            }
        }
        else if (scroll < 434){
            check_scroll = true;

            obj.unbind('focus', more);
            obj.unbind('blur', less);
            obj.css('width', '100%');
            obj.removeClass('fixed-search');
        }
    });

};
