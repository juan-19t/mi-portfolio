let enlace1Menu = document.getElementById('enlace1');
let seccionProyectos = document.getElementById('proyectos');
let botonSlide = document.getElementById('boton-slide');

function prueba(valor){
    valor.style.color= 'white';
}


let listaProyectos = [
    {
        titulo: "Gallo Rojo",
        descripcion:"este es el de gallo rojo",
        imagen:"./imagenes/recorte-gallo.PNG",
        link:"https://gallo-rojo-koefvgyjk.vercel.app/" 
    },
      {
        titulo: "Gestion escolar",
        descripcion:"este es el de gestion escolar",
        imagen:"./imagenes/recorte-gestion.PNG",
        link:"https://gestion-escolar.vercel.app/"
    },
      {
        titulo: "AmalfiExcursiones",
        descripcion:"este es el de excursiones",
        imagen:"./imagenes/recorte-excursiones.PNG",
        link:"https://amalfiexcursiones-bv33.vercel.app/" 
    },
      {
        titulo: "Piedra, papel o tijera",
        descripcion:"este es el juego",
        imagen:"./imagenes/recorte-juego.PNG",
        link:"https://piedra-papel-tijera-gules.vercel.app/"
    }
]

            seccionProyectos.innerHTML = `<div id="info-proyecto"><h1>Mis proyectos <div id="subrayado"></div></h1>
            <h2>${listaProyectos[0].titulo}</h2>
            <p>${listaProyectos[0].descripcion}</p>
            <a href="${listaProyectos[0].link}" target="_blank">Deploy</a></div>
            </div>
            <div id="contenedor-proyectos">
            
            <div id="detalle-proyecto">
            <img id="imagen-recorte" src=${listaProyectos[0].imagen} alt="">
            </div>
            </div>`;
    
            let i = 0;
    seccionProyectos.addEventListener('click',()=>{
        
                if(i<listaProyectos.length-1){
                    i++;
                seccionProyectos.innerHTML = `<div id="info-proyecto"><h1>Mis proyectos <div id="subrayado"></div></h1>
                            <h2>${listaProyectos[i].titulo}</h2>
                           <p>${listaProyectos[i].descripcion}</p>
                                <a href="${listaProyectos[i].link}" target="_blank">Deploy</a>
                                </div>
                           <div id="contenedor-proyectos">
                           
                               <div id="detalle-proyecto">
                               <img id="imagen-recorte" src=${listaProyectos[i].imagen} alt="">
                            </div>
                        </div>`;
                }else{
                    i = 0;
                    seccionProyectos.innerHTML = `<div id="info-proyecto"><h1>Mis proyectos <div id="subrayado"></div></h1>
                            <h2>${listaProyectos[i].titulo}</h2>
                           <p>${listaProyectos[i].descripcion}</p>
                           <a href="${listaProyectos[i].link} ">Deploy</a></div>
                           </div>
                           <div id="contenedor-proyectos">
                           
                               <div id="detalle-proyecto">
                               <img id="imagen-recorte" src=${listaProyectos[i].imagen} alt="">
                            </div>
                        </div>`;
                }
            
    })
    

