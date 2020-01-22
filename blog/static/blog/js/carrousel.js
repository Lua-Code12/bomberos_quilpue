//almacenar contenedor de imagen en variable
var contenedorimagenes=$('#contenedor-imagenes');
//almacenar botones en variables
var siguiente=$('#btn-siguiente');
var anterior=$('#btn-anterior');

//mover ultima imagen al inicio
$('#contenedor-imagenes section:last').insertBefore('#contenedor-imagenes section:first');

//muestra la primera imagen con margen -100%
contenedorimagenes.css('margin-left', '-'+100+'%');

//mover derecha
function moverderecha(){
    contenedorimagenes.animate({
        marginLeft:'-'+200+'%'
    },700,function(){
        $('#contenedor-imagenes section:first').insertAfter('#contenedor-imagenes section:last');
        contenedorimagenes.css('margin-left', '-'+100+'%');
    });
}

function moverizquierda(){
    contenedorimagenes.animate({
        marginLeft:0
    },700,function(){
        $('#contenedor-imagenes section:last').insertBefore('#contenedor-imagenes section:first');
        contenedorimagenes.css('margin-left', '-'+100+'%');
    });
}

siguiente.on('click',function() {
    moverderecha();
})

anterior.on('click',function() {
    moverizquierda();
})

function autoplay(){
    interval = setInterval(function(){
        moverderecha();
    },15000);
}

autoplay();