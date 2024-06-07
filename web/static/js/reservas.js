const tagsHabitacion = document.getElementsByClassName("btn-habitacion")

const CABAÑAS = {
    "1": {
       "nombre": "Cabaña 1",
       "descripcion": "Descripcion de la cabaña 1"
    },
    "2": {
       "nombre": "Cabaña 2",
       "descripcion": "Descripcion de la cabaña 2"
    },
    "3": {
       "nombre": "Cabaña 3",
       "descripcion": "Descripcion de la cabaña 3"
    },
    "4": {
       "nombre": "Cabaña 4",
       "descripcion": "Descripcion de la cabaña 4"
    },
}
// Esto habria que recibirlo desde el back (?)

function cambiarActivo(anterior, nuevo){
    const botonAnterior = anterior.children[0]
    botonAnterior.classList.remove("active")

    const botonNuevo = nuevo.children[0]
    botonNuevo.classList.add("active")

    return nuevo
}

window.onload = () => {
    const descripcion = document.getElementById("descripcion-cabaña")
    let tagActivo = tagsHabitacion[0]
    let cabaña = CABAÑAS[tagActivo.dataset.cabaña]
    
    descripcion.innerHTML += cabaña["descripcion"]

    for (let i = 0; i < tagsHabitacion.length; i++){
        const tag = tagsHabitacion[i]
        tag.addEventListener("click", () => {
            tagActivo = cambiarActivo(tagActivo, tag)
            cabaña = CABAÑAS[tagActivo.dataset.cabaña]
            descripcion.innerHTML = cabaña["descripcion"]
        })
    }
}

