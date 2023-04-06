function register(){
    location.href = "registro.html"
}

function login(){
    location.href = "index.html"
}

function principal(){
    var email, pass
    email = document. getElementById("correo").value;
    pass = document. getElementById("contraseña").value;

    if(email == "admin" && pass == "0000"){
        location.href = "principal.html"
    }
    else{
        alert("Datos incorrectos, intente nuevamente.")
    }
}

function principalinvitado(){
    location.href = "principal.html"
}