function obtenerHoy(){
    var today = new Date();
    var dia = today.getDate();
    var mes = today.getMonth() + 1; //January is 0!
    var año = today.getFullYear();
    
    if (dia < 10) {
       dia = '0' + dia;
    }
    
    if (mes < 10) {
       mes = '0' + mes;
    } 
        
    return `${año}-${mes}-${dia}`
}

const inputsCalendario = document.getElementsByClassName("input_calendario")
const hoy = obtenerHoy()
for(let i = 0; i < inputsCalendario.length; i++){
    inputsCalendario[i].setAttribute("min", hoy)
}

const botonCambiarCalendario = document.getElementById("cambiar-calendario")
const contenidoBotonSiguiente = `Siguiente <i class="fa fa-arrow-right" aria-hidden="true"></i>`
const contenidoBotonAnterior = `Volver <i class="fa fa-arrow-left" aria-hidden="true"></i></i>`
const calendarios = document.getElementsByClassName("calendar")
let calendarioActual = 0
botonCambiarCalendario.addEventListener("click", () => {
    for(let i = 0; i < calendarios.length; i++){
        if(i == calendarioActual){
            calendarios[i].classList.toggle("calendar_active")
            if(i == 0){
                botonCambiarCalendario.innerHTML = contenidoBotonSiguiente
            } else if(i == calendarios.length - 2){
                botonCambiarCalendario.innerHTML = contenidoBotonAnterior
            }
            
            if(i == calendarios.length - 1){
                botonCambiarCalendario.innerHTML = contenidoBotonSiguiente
                calendarios[0].classList.toggle("calendar_active")
                calendarioActual = 0
            } else{
                calendarios[i+1].classList.toggle("calendar_active")
                calendarioActual++
            }
            break
        }
    }
})