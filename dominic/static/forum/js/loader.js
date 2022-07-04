var message_ele = document.getElementById("message_container");

setTimeout(function () {
    message_ele.style.display = "none";
}, 3000);


var loader = document.getElementById("loader")
var pageContent = document.getElementById("pageContent")

const submitAction = () => {
    loader.classList.remove("hideThis")
    pageContent.classList.add("blurContent")
}