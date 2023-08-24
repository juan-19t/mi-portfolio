let enlace1Menu = document.getElementById('enlace1');
let seccionProyectos = document.getElementById('proyectos');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
let i = 0;

function prueba(valor) {
    valor.style.color = 'white';
}


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

function creandoCarrousel(indice) {
    return seccionProyectos.innerHTML = `<div id="info-proyecto"><h1>Mis proyectos <div id="subrayado"></div></h1>
            <h2>${listaProyectos[indice].titulo}</h2>
            <p>${listaProyectos[indice].descripcion}</p>
            <a href="${listaProyectos[indice].link}" target="_blank">Deploy</a></div>
            </div>
            <div id="contenedor-proyectos">
            
            <div id="detalle-proyecto">
            <img id="imagen-recorte" src=${listaProyectos[indice].imagen} alt="">
            </div>
            </div>`;
}


nextBtn.addEventListener('click', () => {

     if (i < listaProyectos.length - 1) {
        i++;
        creandoCarrousel(i);
    } else {
        i = 0;
        creandoCarrousel(i)

    }
})

prevBtn.addEventListener('click',()=>{
    if (i > 0) {
        i--;
        creandoCarrousel(i);
    } else {
        i = listaProyectos.length-1;
        creandoCarrousel(i)

    }
})

creandoCarrousel(0);


