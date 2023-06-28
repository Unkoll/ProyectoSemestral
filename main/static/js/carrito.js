document.addEventListener('DOMContentLoaded', function() {
    // Variables
    const listaProductos = document.getElementById('lista-productos');
    const listaProductosDisponibles = document.getElementById('lista-productos-disponibles');
    const totalElement = document.getElementById('total');
    const comprarBtn = document.getElementById('comprar-btn');
    
    let carrito = [];
    
    // Función para agregar un producto al carrito
    function agregarProducto(id, nombre, precio) {
        const producto = {
            id: id,
            nombre: nombre,
            precio: precio
        };
        
        carrito.push(producto);
        mostrarCarrito();
    }
    
    // Función para mostrar el carrito de compras
    function mostrarCarrito() {
        listaProductos.innerHTML = '';
        
        carrito.forEach(function(producto) {
            const li = document.createElement('li');
            li.textContent = `${producto.nombre} - Precio: ${producto.precio}`;
            listaProductos.appendChild(li);
        });
        
        calcularTotal();
    }
    
    // Función para calcular el total de la compra
    function calcularTotal() {
        let total = 0;
        
        carrito.forEach(function(producto) {
            total += producto.precio;
        });
        
        totalElement.textContent = total;
    }
    
    // Evento para agregar un producto al hacer clic en el botón correspondiente
    listaProductosDisponibles.addEventListener('click', function(event) {
        if (event.target.classList.contains('agregar-btn')) {
            const id = event.target.getAttribute('data-id');
            const nombre = event.target.getAttribute('data-nombre');
            const precio = parseFloat(event.target.getAttribute('data-precio'));
            
            agregarProducto(id, nombre, precio);
        }
    });
    
    // Evento para enviar la solicitud POST al hacer clic en el botón de compra
    comprarBtn.addEventListener('click', function() {
        if (carrito.length > 0) {
            const url = '/crear_boleta/';  // URL para guardar la boleta
            
            // Crear objeto FormData con los detalles del carrito
            const formData = new FormData();
            
            carrito.forEach(function(producto, index) {
                formData.append(`productos[${index}][id]`, producto.id);
                formData.append(`productos[${index}][nombre]`, producto.nombre);
                formData.append(`productos[${index}][precio]`, producto.precio);
            });
            
            // Enviar solicitud POST con los detalles del carrito
            fetch(url, {
                method: 'POST',
                body: formData
            })
            .then(function(response) {
                // Aquí puedes manejar la respuesta del servidor
                // Por ejemplo, mostrar un mensaje de éxito, redirigir, etc.
            })
            .catch(function(error) {
                console.error('Error al enviar la solicitud POST:', error);
            });
        }
    });
});
