// chrome.runtime.sendMessage("hola");






//1(Getting names of Notebooks available)
var ID;
function getCookies() {
    chrome.cookies.get({url: 'http://127.0.0.1/', name: 'uid'}, function (cookie) {
        ID = cookie.value;
        $.ajax({

        url:"http://127.0.0.1:8000/getList/"+ID,
        success: function (notes) {

            var ele = document.getElementById('names');

            for (i in notes.name) {
                ele.innerHTML = ele.innerHTML +
                '<option value="' + notes.id[i] + '">' + notes.name[i] + '</option>';

            }

        }
    });
    });
}
getCookies();

//2(Open login Page on website)
let click2login = document.getElementById('login');
  click2login.onclick = function (element) {
   chrome.tabs.create({url:"http://127.0.0.1:8000/"});
  };


//3(changes UI according to status)
chrome.cookies.get({url:'http://127.0.0.1/', name:'sessionid'}, function(cookie) {

    if (cookie) {
        $("#beforelogin").hide();
        $("#afterlogin").show();
    }
    else {
                $("#beforelogin").show();
        $("#afterlogin").hide();
    }
});

//4(This is to clip the data in rich format)
document.addEventListener('paste', function(e) {
        e.preventDefault();

        var pastedText = '';

        if (window.clipboardData && window.clipboardData.getData) {

            pastedText = window.clipboardData.getData('Text');

        } else if (e.clipboardData && e.clipboardData.getData) {

            pastedText = e.clipboardData.getData('text/html');

        }

        document.getElementById('text').innerHTML = pastedText;

                $("#text *").not("table").removeAttr("style");
    });


//4(Onclick submission of text)
 $("#button").click(function(e) {
e.preventDefault();


console.log("started");

var text = document.getElementById('text').innerHTML;
var title = document.getElementById('title').value;
// var selection = document.getElementById('names').value;
// var NotebookId = selection.options[selection.selectedIndex].value;
var NotebookId = $("#names").val();


$.ajax({
    url: "http://127.0.0.1:8000/view/"+NotebookId,
    type: "POST",
    data: {
        title:title,
        content:text,
    },
    success: function(text){
        alert("Successfully submitted");

    },
    error:function(){
        alert("Error occured");
    }
});
});


