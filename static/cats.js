
const catSearch = document.querySelector(".cat-search"); 
const parentDiv = document.querySelector(".parent")

// adding an event when the user clicks on the search bar 
catSearch.addEventListener("click", function () {
    catSearch.style.width = "40%";
    catSearch.style.transition = "1s"
    catSearch.style.border = "1px solid black"
    parentDiv.style.filter = "blur(8px)"
}); 

// removing the events when the user clicks away
parentDiv.addEventListener("click", function () {
    catSearch.style.width = "350px";
    catSearch.style.border = "none";
    parentDiv.style.filter = "none"
}); 

const logOut = document.querySelector(".log-out")
logOut.addEventListener("click", function () {
    localStorage.clear()
})

