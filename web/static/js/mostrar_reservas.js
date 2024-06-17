document.addEventListener('DOMContentLoaded', (event) => {
    // Obtener el modal
    var modal = document.getElementById("myModal");

    // Obtener el botón que cierra el modal
    var span = document.getElementsByClassName("close")[0];

    // Mostrar el modal automáticamente al cargar la página
    modal.style.display = "block";

    // Cuando el usuario hace clic en <span> (x), cerrar el modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // Cuando el usuario hace clic en cualquier lugar fuera del modal, cerrarlo
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});
