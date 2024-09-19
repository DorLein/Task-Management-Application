
const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");
const sign_in_btn2 = document.querySelector("#sign-in-btn2");
const sign_up_btn2 = document.querySelector("#sign-up-btn2");


sign_up_btn.addEventListener("click", function() {
    container.classList.add("sign-up-mode");
}, false);

sign_in_btn.addEventListener("click", function() {
    container.classList.remove("sign-up-mode");
}, false);

sign_up_btn2.addEventListener("click", function() {
    container.classList.add("sign-up-mode2");
}, false);

sign_in_btn2.addEventListener("click", function() {
    container.classList.remove("sign-up-mode2");
}, false);

window.addEventListener('load', function () {
    container.classList.add("sign-up-mode");

})


