const dogSearch = document.querySelector(".dog-search"); 
const parentDiv = document.querySelector(".parent")

// adding an event when the user clicks on the search bar 

dogSearch.addEventListener("click", function () {
    dogSearch.style.width = "40%";
    dogSearch.style.transition = "1s"
    dogSearch.style.border = "1px solid black"
    parentDiv.style.filter = "blur(8px)"
}); 

// removing the events when the user clicks away

parentDiv.addEventListener("click", function () {
    dogSearch.style.width = "350px";
    dogSearch.style.border = "none";
    parentDiv.style.filter = "none"
}); 

const logOut = document.querySelector(".log-out")
logOut.addEventListener("click", function () {
    localStorage.clear()
})
