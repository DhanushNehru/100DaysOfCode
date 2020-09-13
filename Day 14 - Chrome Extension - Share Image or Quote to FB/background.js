// alert('Hi');

function MyGenericClick(info, tab){
    console.log("Clicked on page", info, tab);
    alert(" Please select an image/ quote ");
}

function MyImageClick(info, tab){
    console.log("Clicked on image", info, tab);
    chrome.windows.create({
        "url":"https://facebook.com/sharer.php?u="+info.srcUrl+"&display=popup",
        "type":"popup"
    })
}

function MyQuoteClick(info, tab){
    console.log("Clicked on quote", info, tab);
    chrome.windows.create({
        //"url":"http://google.com",
        "url":"https://facebook.com/sharer.php?u="+info.pageUrl+"&display=popup&quote="+ info.selectionText,
        "type":"popup"
    })
}

chrome.contextMenus.create({
    "title": "Share",
    "contexts":["page"],
    "onclick": MyGenericClick
})

chrome.contextMenus.create({
    "title": "Share Image",
    "contexts":["image"],
    "onclick": MyImageClick
})

chrome.contextMenus.create({
    "title": "Share Quote",
    "contexts":["selection"],
    "onclick": MyQuoteClick
})

function sendResponse(){

}

chrome.runtime.onMessage.addListener(
    function(msg, sender, sendResponse){
        console.log('Message : ', msg);
        sendResponse({"text": "Received the links"});
    }
)