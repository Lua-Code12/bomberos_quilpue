function validarCaracteres(e){
    key = e.keyCode || e.which;
    tecla = String.fromCharCode(key).toLowerCase();
    letras = " áéíóúabcdefghijklmnñopqrstuvwxyz";
    especiales = "8-37-39-46";

    tecla_especial = false
    for(var i in especiales){
         if(key == especiales[i]){
             tecla_especial = true;

             break;
         }
     }

     if(letras.indexOf(tecla)==-1 && !tecla_especial){
         return false;

     }
 }


 function validarRut(rutdv) {

    // Despejar Puntos
    var caracteres = rutdv.value.replace('.','');
    // Despejar Guión
    caracteres = caracteres.replace('-','');
    
    // Aislar Rut y Dígito Verificador
    rut = caracteres.slice(0,-1);
    // Se obtiene el digito verificador y en caso de ser un raya K se le agrega el uppercase para dejarlo en mayuscula

    dv = caracteres.slice(-1).toUpperCase();
    
    // Se le otorga un nuevo formato al rut 
    rutdv.value = rut + '-'+ dv
    
    // Condicion para que cumpla con el largo minimo
    if(rut.length < 7) { rutdv.setCustomValidity("RUT Invalido"); return false;}
    
    /* Calcular Dígito Verificador
    Suma actuara como contador
    Multiplo como Multiplo del Algoritmo, para que funcione debe tener un valor 2
    */
    
    suma = 0;
    multiplo = 2;
    
    /*Algoritmo para el digito vefificador del rut, ya que no basta solo con el formato si no tambien en la legalidad de este*/
    
    // 1) Se hara un recorrido al arreglo del caracteres por medio de un for
    
    for(i=1;i<=rut.length;i++) {
    
        // Obtener su Producto con el Múltiplo Correspondiente
        index = multiplo * caracteres.charAt(rut.length - i);
        
        // Contador
        suma = suma + index;
        
        // Consolidar Múltiplo dentro del rango [2,7]
        if(multiplo < 7) { multiplo = multiplo + 1; } else { multiplo = 2; }
  
    }
    
    // Calcular Dígito Verificador en base al algoritmo en base a Módulo 11 
    dvLegal = 11 - (suma % 11);
    
    // En caso de digito verificador terminado  en 0 o K
    dv = (dv == 'K')?10:dv;
    dv = (dv == 0)?11:dv;
    
    // Validar Cuerpo con Digito Verificador
    if(dvLegal != dv) { rutdv.setCustomValidity("RUT Inválido"); return false; }
    
    // Se decreta que es valido
    rutdv.setCustomValidity('');
    }