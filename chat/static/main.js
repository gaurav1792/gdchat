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
function callAjax() {
    setTimeout(doAjax, interval);
}
function display(data, textStatus, jqXHR)
{
    $('#chat_result').html(data);
}