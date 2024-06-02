function obtenerDatos(id){
    document.getElementById('formulario').action = '/administrar/'+id
    document.getElementById('boton').innerHTML = 'Actualizar'

    nombreactual = document.getElementById('tabla_nombres'+id).innerHTML
    apellidoactual = document.getElementById('tabla_apellidos'+id).innerHTML
    tipodocumentoactual = document.getElementById('tabla_tipodocumento'+id).innerHTML
    documentoctual = document.getElementById('tabla_documento'+id).innerHTML
    telefonoactual = document.getElementById('tabla_telefono'+id).innerHTML
    correoactual = document.getElementById('tabla_correo'+id).innerHTML
    generoactual = document.getElementById('tabla_genero'+id).innerHTML
    carreraactual = document.getElementById('tabla_carrera'+id).innerHTML
    
    document.getElementById('nombres').value = nombreactual
    document.getElementById('apellidos').value = apellidoactual
    document.getElementById('tipo_documento').value = tipodocumentoactual 
    document.getElementById('documento').value = documentoactual 
    document.getElementById('telefono').value = telefonoactual
    document.getElementById('correo').value = correonoactual
    document.getElementById('genero').value = generoactual
    document.getElementById('carrera').value = carreraactual


}
