var array_productos = [];

    if (localStorage.getItem('PRODUCTOS')) {
      array_productos = JSON.parse(localStorage.getItem('PRODUCTOS')) || [];
      $('#carrito-producto').append(texto);
      $('#carrito-precio').html(total);
      $('#precio-offcanva').html(total);
    }

    function comprar(id) {
      // alert(id);
      var producto = $('#producto-' + id);

      var p = {
        id: id,
        img: producto.data('img'),
        nombre: producto.data('nombre'),
        precio: producto.data('precio')
      };

      array_productos.push(p);

      console.log(array_productos);

      localStorage.setItem('PRODUCTOS', JSON.stringify(array_productos));

      // localStorage.setItem('RICHARD', JSON.stringify({
      //     name: 'richard',
      //     edad: '23',
      //     status: 'rico millonario',
      //     profesion: 'informatico'
      // }));
      llenar_carrtio();
    }

    function llenar_carrtio() {
      $('#carrito-producto').html('');
      var texto = '';
      var total = 0;
      array_productos.forEach(producto => {
        texto = texto + `
                <tr>
                  <td><img src="${producto.img}" width="50px"></td>
                  <td>${producto.nombre}</td>
                  <td>$${producto.precio}</td>
                </tr>
                `;

        total += producto.precio;
      });

      $('#carrito-producto').append(texto);
      $('#carrito-precio').html(total);
      $('#precio-offcanva').html(total);
    }