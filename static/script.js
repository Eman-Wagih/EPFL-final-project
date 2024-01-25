const userName = document.getElementById("userName");
const passWord = document.getElementById("passWord"); 
const logIN = document.querySelector(".log-in")

// gettig the 
logIN.addEventListener("click", function () {
    localStorage.setItem("userName", userName.value);
    localStorage.setItem("password", passWord.value);
})

window.onload = () => {
    localStorage.getItem("userName", "password")
}


const logOut = document.querySelector(".log-out")
logOut.addEventListener("click", function () {
    localStorage.clear()
})