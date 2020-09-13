console.log(" My Extension ");
// alert(" Loaded ");

//var dom = document.getElementById("topstuff");
//var links = dom.getElementsByClassName("col");
var links = document.getElementsByTagName("a");
var formatted_links = [];

for(let i = 0 ; i< links.length; i++){
    //let title = links[i].getElementsByTagName('h3');
    //let title = links[i].innerHTML;
    let title = links[i].text;
    let href = links[i].href;

    if(title !== "" && href !== ""){
        formatted_links.push({title:title , href:href});
    }
    
    // console.log('Links ', title);
    //console.log('Links ', title[0]);
}

chrome.runtime.sendMessage({
    "action":"print_messages",
    "data": formatted_links
}), res => {
    console.log(res);
}
//console.log("The DOM is ",dom.innerHTML)