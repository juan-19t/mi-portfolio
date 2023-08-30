let enlace1Menu = document.getElementById('enlace1');
let seccionProyectos = document.getElementById('proyectos');
let indiceDiv = document.getElementById('indice');
let contenedorProyecto = document.getElementById('contenedor-proyectos');
let infoProyecto = document.getElementById('info-proyecto');
let i = 0;

// function prueba(valor) {
//     valor.style.color = 'white';
// }


let listaProyectos = [
    {
        titulo: "Gallo Rojo",
        descripcion: "este es el de gallo rojo",
        imagen: "./imagenes/recorte-gallo.PNG",
        link: "https://gallo-rojo-koefvgyjk.vercel.app/"
    },
    {
        titulo: "Gestion escolar",
        descripcion: "este es el de gestion escolar",
        imagen: "./imagenes/recorte-gestion.PNG",
        link: "https://gestion-escolar.vercel.app/"
    },
    {
        titulo: "AmalfiExcursiones",
        descripcion: "este es el de excursiones",
        imagen: "./imagenes/recorte-excursiones.PNG",
        link: "https://amalfiexcursiones-bv33.vercel.app/"
    },
    {
        titulo: "Piedra, papel o tijera",
        descripcion: "este es el juego",
        imagen: "./imagenes/recorte-juego.PNG",
        link: "https://piedra-papel-tijera-gules.vercel.app/"
    }
]
function  creandoCarrousel(indice) {
    
    infoProyecto.innerHTML = `<h1>Mis proyectos <div id="subrayado"></div></h1>
            <h2>${listaProyectos[indice].titulo}</h2>
            <p>${listaProyectos[indice].descripcion}</p>
            <a href="${listaProyectos[indice].link}" target="_blank">Deploy</a></div>`;

    contenedorProyecto.innerHTML = `
            <div id="detalle-proyecto">
            <img id="imagen-recorte" src=${listaProyectos[indice].imagen} alt="">
            </div>
            `;
}

creandoCarrousel(0);

let prevBtn = document.getElementById('prevBtn');
let nextBtn = document.getElementById('nextBtn');

nextBtn.addEventListener('click', () => {
        
    if (i < listaProyectos.length - 1) {
        i++;
        creandoCarrousel(i);
    } else {
        i = 0;
        creandoCarrousel(i)
    }
    indiceDeProyectos(i);
}   )

prevBtn.addEventListener('click', () => {
    if (i > 0) {
        i--;
         creandoCarrousel(i);
    } else {
        i = listaProyectos.length - 1;
        creandoCarrousel(i)
    }
        indiceDeProyectos(i);
})



indiceDeProyectos(i);
function indiceDeProyectos(numero) {
    indice = numero + 1;
    total = listaProyectos.length;
    indiceDiv.innerHTML = `<p id="numeros-indice">${indice}/${total}</p>`;
}








