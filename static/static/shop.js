const addToCart = document.querySelectorAll(".add-to-cart");  
const buyingForm = document.querySelector(".buying");
const orderNow = document.querySelector(".order-now");
const displayInfo = document.querySelector(".display-info")


let productType = '';
let productPrice = '';

// to determine which item was clicked on
addToCart.forEach((button) => {
    button.addEventListener("click", function (event) {

        buyingForm.style.display = "block";

        let productTypeElement = event.target.closest('.item').querySelector('.product-type');
        let productPriceElement = event.target.closest('.item').querySelector('.price');
        productType = productTypeElement ? productTypeElement.textContent : '';
        productPrice = productPriceElement ? productPriceElement.textContent : '';
    });
});

// displaying the msg
orderNow.addEventListener("click", function (event) {
    event.preventDefault();

    buyingForm.style.display = "none";

    const clientName = document.querySelector(".client-name").value;
    const clientPhone = document.querySelector(".client-phone").value; 
    const clientEmail = document.querySelector(".client-email").value; 
    const clientAddress = document.querySelector(".client-address").value;

    displayInfo.innerText = `
        Hello ${clientName}, 
        Thank you for shopping with Us!
        Kindly note that the ${productType} you ordered will be delivered to your address at ${clientAddress} within two days.
        we will send you an update at ${clientEmail} right after your order has been shipped. 
        our delivery agent will call you on ${clientPhone} so please be sure to pick up.
        The total amount is ${productPrice}
    `;
});

const logOut = document.querySelector(".log-out")
logOut.addEventListener("click", function () {
    localStorage.clear()
})