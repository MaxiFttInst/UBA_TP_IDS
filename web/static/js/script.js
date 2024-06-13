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

function cambiarActivo(anterior, nuevo){
  if(anterior){
    const cabaniaAnterior = document.getElementById(anterior.dataset.cabaniaId)
    cabaniaAnterior.classList.remove("cabania-visible")
  }

  const cabañaNueva = document.getElementById(nuevo.dataset.cabaniaId)
  cabañaNueva.classList.add("cabania-visible")

  return nuevo
}

const botonesCabanias = document.getElementsByClassName("boton-cabania")
let cabania_actual = null
for(let i = 0; i < botonesCabanias.length; i++){
  const elemento_cabania = botonesCabanias[i]
  elemento_cabania.addEventListener("click", () => {
    cabania_actual = cambiarActivo(cabania_actual, elemento_cabania)
  })
}

let dark_mode = false;
let dark_mode_btn = document.getElementById('moon_btn');
let modeFa = document.getElementById('modeFa');
let white_elements = document.getElementsByClassName("bc-white");
let dark_elements = document.getElementsByClassName("bc-light-gray");

dark_mode_btn.addEventListener('click',toggleDarkMode);
function toggleDarkMode() {
  dark_mode = !dark_mode;
  if(dark_mode) {
    modeFa.classList.remove('fa-sun-o');
    modeFa.classList.add('fa-moon-o');
    for (var i = 0; i < white_elements.length; i++) {
      white_elements[i].style.backgroundColor="rgb(31, 31, 31)";
      white_elements[i].style.color="white";
    }
    for (var i = 0; i < dark_elements.length; i++) {
      dark_elements[i].style.backgroundColor="rgb(51, 51, 51)";
    }
    console.log(dark_mode);
  } else {
    console.log(dark_mode);
    modeFa.classList.add('fa-sun-o');
    modeFa.classList.remove('fa-moon-o');
    for (var i = 0; i < white_elements.length; i++) {
      white_elements[i].style.backgroundColor="white";
      white_elements[i].style.color="black";
    }
    for (var i = 0; i < dark_elements.length; i++) {
      dark_elements[i].style.backgroundColor="rgb(31, 31, 31)";
    }

  }
}