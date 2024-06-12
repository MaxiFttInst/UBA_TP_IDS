function w3_open() {
  var x = document.getElementById("mySidebar");
  x.style.width = "300px";
  x.style.paddingTop = "10%";
  x.style.display = "block";
}

function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
}

function openNav() {
  var x = document.getElementById("navDemo");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}

document.querySelectorAll('.header').forEach(header => {
  header.addEventListener('click', function() {
      var info = this.querySelector('.info');
      if (info.classList.contains('visible')) {
          info.classList.remove('visible');
      } else {
          info.classList.add('visible');
      }
  });
});

let hideText_btn = document.getElementById('hideText_btn');
let hideText = document.getElementById('hideText');

hideText_btn.addEventListener('click', toggleText);
function toggleText() {
    hideText.classList.toggle('show');
    if(hideText.classList.contains('show')) {
      hideText_btn.innerHTML = 'Leer menos';
    } else {
      hideText_btn.innerHTML = 'Mas información';
    }
}

let hideText_btn2 = document.getElementById('hideText_btn2');
let hideText2 = document.getElementById('hideText2');

hideText_btn2.addEventListener('click', toggleText2);
function toggleText2() {
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
