var contextList = ["selection","link","page","image"]

for(i=0 ;i<contextList.length;i++) {
    chrome.contextMenus.create({
        "id": contextList[i],
        "title": contextList[i],
        "contexts": [contextList[i]],

    });
}
chrome.contextMenus.onClicked.addListener(onClickHandler);

function onClickHandler(selectedText) {

    alert(selectedText.selectionText);

}