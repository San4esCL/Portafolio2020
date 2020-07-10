
$(function() {
      $("#formulareishon").validate({

        /*
	        $.validator.setDefaults({
  	        errorClass:'error-label',
            highlight: function(element){
    	    $(element).addClass('error-control');
            },
            unhighlight: function(element){
            $(element).removeClass('error-control');
            }
            });
        */
        rules: {
          mail: {
            required: true,
            mail: true
          },
          run: {
              required:true,
              run: true
          },
          nombre: {
              required:true,
              nombre: true
          },
          fecha: {
            required:true,
            fecha: true
        },
        telefono: {
            required:true,
            telefono: true
        },
        region: {
            required:true,
            region: true
        },
          ciudad: {
            required: true,
            ciudad: true
          },
        vivienda: {
          required: true,
          vivienda: true
        }
          
        
        },
        messages: {
            mail: {
            required: 'Ingresa tu correo electrónico',
            email: 'Formato de correo no válido'
            },
            run: {
            required: 'Ingresa una Run',
            run: 'formato de run no valido'
            },
            nombre: {
            required: 'Ingresa tu nombre completo',
            email: 'Formato de nombre no válido'

            },
            fecha: {
            required: 'Ingresa tu fecha de nacimiento',
            email: 'Fecha requerida'
            },
            telefono: {
            required: 'Ingresa un telefono',
            telefono: 'telefono de contacto requerido'
            },
            region: {
            required: 'Ingresa una region',
            region: 'region requerida'
            },
            ciudad: {
            required: 'Ingresa una ciudad',
            ciudad: 'ciudad requerida'
            },
            vivienda: {
              required: 'Ingresa un tipo vivienda',
              vivienda: 'tipo de vivienda requerida'
              }
        }
      
      });
    });
    //function confirmar(){
     // var mensaje = confirm("guardado")
      //if (mensaje){
       //   alert("gracias");
     // }
      //else{
       //   alert("formulario cancelado");
      //}
      
    //}
