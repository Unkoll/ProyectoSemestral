function register(){
    location.href = "/registro"
}

function login(){
    location.href = "/inicio"
}

function principal(){
    var email, pass
    email = document. getElementById("correo").value;
    pass = document. getElementById("contraseña").value;

    if(email == "admin" && pass == "0000"){
        location.href = "/administrador"
    }
    else{
        alert("Datos incorrectos, intente nuevamente.")
    }
}

function principalinvitado(){
    location.href = "principal.html"
}

function redirectionWsp() {
    location.href = "https://api.whatsapp.com/send/?phone=56992775881&text=Hola!%20quiero%20comprar%20en%20su%20página%20web";
}