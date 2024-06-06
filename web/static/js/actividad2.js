let hideText_btn2 = document.getElementById('hideText_btn2');
let hideText2 = document.getElementById('hideText2');

hideText_btn2.addEventListener('click', toggleText);
function toggleText() {
    hideText2.classList.toggle('show');
    if(hideText2.classList.contains('show')) {
      hideText_btn2.innerHTML = 'Leer menos';
    } else {
      hideText_btn2.innerHTML = 'Mas información';
    }
}

function togglecabaña(cabaña) {
    const cabañas = ['Bestia Clérigo', 'Vicaria Amelia', 'Emisario Celestial', 'Presencia Lunar', 'Adela', 'Almendra'];
    cabañas.forEach(function(cab) {
        const cabañaElement = document.getElementById('detalles-' + cab);
        if (cab === cabaña) {
            cabañaElement.style.display = (cabañaElement.style.display === 'block') ? 'none' : 'block';
        } else {
            cabañaElement.style.display = 'none';
        }
    });
}