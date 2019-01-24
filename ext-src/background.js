//Receiving messages
// chrome.runtime.onMessage.addListener(function (response,sender,sendResponse){
//
// });
//Creating tabs
// chrome.pageAction.onClicked.addListener(function sendData(){
//
//     chrome.tabs.create({url:url});
//
//
// let click2login = document.getElementById('login');
//
//   click2login.onclick = function (element) {
//
//    alert("welcome");
//
//   };

// chrome.cookies.get({url:'http://127.0.0.1/', name:'sessionid'}, function(cookie) {
//     if (cookie) {
//         alert("hh");
//     }
// });

// chrome.browserAction.onClicked.addListener(function(tab) {
//    chrome.tabs.executeScript(null, {file: "testScript.js"});
// });
chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    alert("message received");
});


\

// chrome.windows.create({
//     type : 'popup',
//     url : "http://yoursite.com/page.html",
//     type: "popup"
// }, function(newWindow) {
//
// });
