document.getElementById('consultar_reservas').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar que el formulario se envíe automáticamente
    
    let nombreCliente = document.getElementById('fname').value;
    let idCliente = document.getElementById('fdni').value;
  
    // Datos a enviar a la API
    let data = {  
        "cliente_id": idCliente,
        "nombre_cliente" : nombreCliente
    };

    // Realizar la solicitud POST a la API del backend
    fetch(`https://posadabyteados.pythonanywhere.com/reserva?fname=${nombreCliente}&fdni=${idCliente}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('La solicitud no fue exitosa');
        }
        return response.json();
    })
    .then(data => {
        // Mostrar los datos en el popup
        let modalText = document.getElementById('modalText');
        modalText.innerText = JSON.stringify(data, null, 2);
        document.getElementById('myModal').style.display = "block";
    })
    .catch(error => {
        console.error('Error:', error);
    });
});