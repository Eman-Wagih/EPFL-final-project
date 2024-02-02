window.onload = () => {
    localStorage.getItem("userName", "password")
}
const displayUserName = document.querySelector(".display-user-name"); 

displayUserName.innerText = `Hello ${localStorage.getItem("userName")}`


const logOut = document.querySelector(".log-out")
logOut.addEventListener("click", function () {
    localStorage.clear()
})