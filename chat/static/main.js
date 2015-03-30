 /**
 * Created by gd on 29-03-2015.
 */

var interval = 1000;  // 1000 = 1 second, 3000 = 3 seconds
function doAjax() {
    $.ajax({
            //method:'post',
            url: '/test12',
            dataType: 'html',
            success: display,
            complete: function () {
                    setTimeout(doAjax, interval);
            },
            async: true
    });
}
 function doAjax1() {
    $.ajax({
            //method:'post',
            url: '/test13',
            dataType: 'html',
            success: display1,
            complete: function () {
                    setTimeout(doAjax1, interval);
            },
            async: true
    });
}
 function doAjax2() {
    $.ajax({
            //method:'post',
            url: 'test11',
            dataType: 'html',
            success: display2,
            complete: function () {
                    setTimeout(doAjax2, interval);
            },
            async: true
    });
}

  function doAjax4() {
    $.ajax({
            url: 'chkstatus',
            dataType: 'html',
            success: display4,
            complete: function () {
                    setTimeout(doAjax4, interval+1000);
            },
            async: true
    });
}

 $('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});

 function create_post() {
    console.log("create post is working!")
    $.ajax({
        url : "create_post",
        type : 'post',
        data : {message: $('#post-text').val()},
        success: function() {
            $('#post-text').val('');
            console.log(data);
        }

    });
};


/* $(function(){
     $('#message').keyup(function(e){
         if(e.keyCode == 13) {
             $.ajax({
                 type: "POST",
                 url: 'send_message',
                 data: {
                     'message': $('#message').val(),
                     'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
                 }

             });
         }
     });
 });
*/


function setoffline()
{
 if(window.close())
 {
     $.ajax({url:"logout", async:true})
 }


}
 function set_online()
{
     $.ajax({
            //method:'post',
            url: 'set_online',
            dataType: 'html',
            success: display,
            complete: function () {
                    setTimeout(doAjax, interval);
            },
            async: true
    });
}
function callAjax1() {
    set_online();
    setTimeout(doAjax, interval);
    setTimeout(doAjax1, interval);
    setTimeout(doAjax4, interval);

}

 function callAjax2() {
     set_online();
    setTimeout(doAjax2, interval);
}

function display(data, textStatus, jqXHR)
{
    $('#chat_result').html(data);
}
 function display1(data, textStatus, jqXHR)
{
    $('#chat_result1').html(data);
}
 function display2(data, textStatus, jqXHR)
{
    $('#chat_result2').html(data);
}

 function display4(data, textStatus, jqXHR)
{
    $('#allusers').html(data);
}