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



  function send_data()
  {
      console.log("send data worked..!");
      var msg= $('#sent_msg').val();
      console.log( msg);
      $.ajax({
        url : "create_post",
        type : 'GET',
        data : {message: msg},
        success: function(data, textStatus, jqXHR) {
            $('#sent_msg').val('');
            console.log(data);
        },
        async: false

    });

  }



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
                    setTimeout(set_online, interval+1000);
            },
            async: true
    });
}

 function set_counter()
{
     $.ajax({
            //method:'post',
            url: 'setcounter',
            dataType: 'html',
            success: setTimeout(callAjax3,interval)
    });
}
 function set_counter1()
{
     $.ajax({
            //method:'post',
            url: 'setcounter',
            dataType: 'html',
            success: setTimeout(callAjax4,interval)
    });
}

 function callAjax1() {
     set_online();
     set_counter();
 }
 function callAjax3(){
    setTimeout(doAjax, interval);
    setTimeout(doAjax1, interval);
    setTimeout(doAjax4, interval);

}

 function callAjax2() {
     set_online();
     set_counter1();
    setTimeout(doAjax2, interval);
}

 function callAjax4() {
    setTimeout(doAjax2, interval);
}

function display(data, textStatus, jqXHR)
{
    console.log(data);
    $('#chat_result').append(data);
    var d = document.getElementById('right');
    if(d.scrollHeight > d.clientHeight)
    d.scrollTop = d.scrollHeight - d.clientHeight;
}

 function display1(data, textStatus, jqXHR)
{
    $('#chat_result1').html(data);
}

 function display2(data, textStatus, jqXHR)
{   console.log(data);
    $('#chat_result2').append(data);
    var d = document.getElementById('right');
    if(d.scrollHeight > d.clientHeight)
    d.scrollTop = d.scrollHeight - d.clientHeight;
}

 function display4(data, textStatus, jqXHR)
{
    $('#allusers').html(data);
}