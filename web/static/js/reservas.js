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

