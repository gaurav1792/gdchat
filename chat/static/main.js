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

 function doAjax3() {
    $.ajax({
            method:'post',
            url: 'test11',
            dataType: 'html',
            success: display2,
            complete: function () {
                    setTimeout(doAjax3, interval);
            },
            async: true
    });
}

function callAjax() {
    setTimeout(doAjax, interval);
    setTimeout(doAjax1, interval);
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