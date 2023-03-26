let navbar = document.querySelector('.navbar');

    document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');
    cartItem.classList.remove('active');
}

let cartItem = document.querySelector('.cart-item-container');

    document.querySelector('#cart-btn').onclick = () =>{
    cartItem.classList.toggle('active');
    navbar.classList.remove('active');

}

window.onscroll = () =>{  
    navbar.classList.remove('active');
    cartItem.classList.remove('active');
}

