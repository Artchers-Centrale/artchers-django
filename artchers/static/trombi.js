
function showInfo(tab){
    if(tab.classList.contains("hidden")){
        tab.classList.remove("hidden");
    } else {
        tab.classList.add("hidden")
    }
}

info1.addEventListener('click',showInfo(infoListeux1))
infoListeux1.classList.remove("hidden");