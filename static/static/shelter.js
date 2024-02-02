const submit = document.querySelector(".submit-btn");
const msg = document.querySelector(".msg")
const contactForm = document.querySelector(".Shelter-Contact")


// displaying msg 
submit.addEventListener("click", function (e) {
    e.preventDefault()
    contactForm.style.display = "none";
    const name = document.querySelector(".name").value
    msg.innerText = `
    Hello ${name}, 
    thank you for wanting to take care of a pet,
    we will send your contact info to the pet owner 
    `
})

const logOut = document.querySelector(".log-out")
logOut.addEventListener("click", function () {
    localStorage.clear()
})