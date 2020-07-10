jsHabitacion = new HabitacionJS();
function HabitacionJS(){
   this.fuLeer = function (){
     if (document.getElementById("txId").value != ""){
          var res= ventana.getJSon("http://localhost:8000/habitacion/" + document.getElementById("txId").value );
          if (typeof(res.habitacion_id) != null) {
               document.getElementById("txvalor").value =  res.valorhab
               document.getElementById("txcapacidad").value =  res.capacidad_hab
               document.getElementById("cbtipohab").value =  res.tipohabitacion_id
               document.getElementById("txbaños").value =  res.baños
               document.getElementById("txdorm").value =  res.dormitorios
               document.getElementById("txtam").value =  res.tamañom2
               document.getElementById("btInsertar").disabled = true
               document.getElementById("btActualizar").disabled = false
               document.getElementById("btEliminar").disabled = false
               document.getElementById("txId").disabled = true
          }
          else {
              alert("No existe el registro")
              document.getElementById("btActualizar").disabled = true
              document.getElementById("btEliminar").disabled = true
          }
     }else{
          alert("Para leer un registro debe tener una ID de Habitacion, este no puede quedar en blanco")
     }
   }
   this.fuEliminar = function (){
     var userselection = confirm("Estas seguro que deseas eliminar este registro?")
     if (userselection == true ){
          var res= ventana.getPost("DELETE","http://localhost:8000/habitacion/" + document.getElementById("txId").value,"" );
          alert("Regisstro eliminado correctamente!")
          jsHabitacion.fuCancelar()
     }else{
          jsHabitacion.fuCancelar()
     }
   }
   this.fuInsertar = function (){
        var res= ventana.getPost("POST","http://localhost:8000/habitacion/"
                             ,{
                               "valorhab":  document.getElementById("txvalor").value
                               ,"capacidad_hab": document.getElementById("txcapacidad").value
                               ,"tamañom2": document.getElementById("txtam").value
                               ,"baños": document.getElementById("txbaños").value
                               ,"dormitorios": document.getElementById("txdorm").value
                               ,"tipohabitacion_id": document.getElementById("cbtipohab").value
                             }
                             );
        jsHabitacion.fuCancelar()
        alert("Habitacion registrada correctamente!")
   }
   this.fuActualizar = function (){
        var res= ventana.getPost("PUT","http://localhost:8000/habitacion/" + document.getElementById("txId").value + "/"
                             ,{
                               "capacidad_hab":  document.getElementById("txcapacidad").value
                               ,"valorhab": document.getElementById("txvalor").value
                               ,"baños": document.getElementById("txbaños").value
                               ,"dormitorios": document.getElementById("txdorm").value
                               ,"tamañom2": document.getElementById("txtam").value
                               ,"tipohabitacion_id": document.getElementById("cbtipohab").value
                              }
                             );
        jsHabitacion.fuCancelar()
   }
   this.fuCancelar = function (){
        document.getElementById("txvalor").value =  ""
        document.getElementById("txcapacidad").value =  ""
        document.getElementById("txbaños").value =  ""
        document.getElementById("txdorm").value =  ""
        document.getElementById("txtam").value =  ""
        document.getElementById("txId").value = ""
        document.getElementById("cbtipohab").value = ""
        document.getElementById("cbtipohab").disabled = false
        document.getElementById("btActualizar").disabled = true
        document.getElementById("btEliminar").disabled = true
        document.getElementById("btInsertar").disabled = false


        //Habilita los botones para que se vuelvan a ocupar
        document.getElementById("txId").value = ""
        document.getElementById("txId").disabled = false
        document.getElementById("btLeer").disabled = false
        jsHabitacion.listarProductos();
   }

   this.listarProductos = function(){
     // Para Destruir, en caso de que quiera recargar la tabla
     $("#tabla").dataTable().fnDestroy();
     $('#tabla').DataTable( {
         ajax:    {
       "url": "http://localhost:8000/habitacion",
       "dataSrc": ""
     },
     "columns": [
            { "data": "habitacion_id" },
            { "data": "valorhab" },
            { "data": "capacidad_hab" },
            { "data": "tamañom2" },
            { "data": "baños" },
            { "data": "dormitorios"}
        ],
         deferRender:    true,
         scrollY:        200,
         scrollCollapse: true,
         scroller:       true,
         //retrieve: true,
        // destroy: true,
         loadingRecords: "Cargando...",
         processing:     "Procesando...",
         paging: false,
         //searching: false
     } );
   }
}
JsTipoHabitacion = new TipoHabJS();
function TipoHabJS(){
     this.THLeer = function(){
       if (document.getElementById("txId").value != ""){
            var res= ventana.getJSon("http://localhost:8000/tipohabitacion/" + document.getElementById("txId").value );
            document.getElementById("txdesc").value =  res.desc_tipohab
            if (document.getElementById("txdesc").value != "undefined") {
            //if(res != null){
                 document.getElementById("txdesc").value =  res.desc_tipohab
                 document.getElementById("btInsertar").disabled = true
                 document.getElementById("btActualizar").disabled = false
                 document.getElementById("btEliminar").disabled = false
                 document.getElementById("txId").disabled = true
            }
            else {
               document.getElementById("txdesc").value=""
                alert("No existe el registro")
                document.getElementById("btActualizar").disabled = true
                document.getElementById("btEliminar").disabled = true
            }
       }else{
            alert("Para leer un registro debe tener una ID de Habitacion, este no puede quedar en blanco")
       }
     }
     this.THCancelar = function(){
          document.getElementById("btActualizar").disabled = true
          document.getElementById("btEliminar").disabled = true
          document.getElementById("btInsertar").disabled = false
          document.getElementById("txdesc").value = ""
          document.getElementById("txId").value = ""
  
          //Habilita los botones para que se vuelvan a ocupar
          document.getElementById("txId").value = ""
          document.getElementById("txId").disabled = false
          document.getElementById("btLeer").disabled = false
          JsTipoHabitacion.THlistarProductos();
     }
     this.THEliminar = function (){
          var userselection = confirm("Estas seguro que deseas eliminar este registro?")
          if (userselection == true ){
               var res= ventana.getPost("DELETE","http://localhost:8000/tipohabitacion/" + document.getElementById("txId").value,"" );
               alert("Registro eliminado correctamente!")
               JsTipoHabitacion.THCancelar()
          }else{
               JsTipoHabitacion.THCancelar()
          }
        }
     this.THActualizar = function (){
        var res= ventana.getPost("PUT","http://localhost:8000/tipohabitacion/" + document.getElementById("txId").value + "/"
                             ,{
                               "desc_tipohab": document.getElementById("txdesc").value
                              }
                             );
                             JsTipoHabitacion.THCancelar()
   }
   this.THlistarProductos = function(){
     // Para Destruir, en caso de que quiera recargar la tabla
     $("#tabla").dataTable().fnDestroy();
     $('#tabla').DataTable( {
         ajax:    {
       "url": "http://localhost:8000/tipohabitacion",
       "dataSrc": ""
     },
     "columns": [
            { "data": "tipohabitacion_id" },
            { "data": "desc_tipohab" }
        ],
         deferRender:    true,
         scrollY:        200,
         scrollCollapse: true,
         scroller:       true,
         //retrieve: true,
        // destroy: true,
         loadingRecords: "Cargando...",
         processing:     "Procesando...",
         paging: false,
         //searching: false
     } );
   }
   this.THInsertar = function (){
     var res= ventana.getPost("POST","http://localhost:8000/tipohabitacion/"
                          ,{
                            "desc_tipohab":  document.getElementById("txdesc").value
                          }
                          );
     JsTipoHabitacion.THCancelar()
     alert("Habitacion registrada correctamente!")
}
}
JsTipoEvento = new TipoEventoJS();
function TipoEventoJS(){
     this.TELeer = function(){
          if (document.getElementById("txId").value != ""){
               var res= ventana.getJSon("http://localhost:8000/tipoevento/" + document.getElementById("txId").value );
               if (typeof(res.tipoevento_id) != null) {
                    document.getElementById("txdesc").value =  res.desc_tipoevento
                    document.getElementById("btInsertar").disabled = true
                    document.getElementById("btActualizar").disabled = false
                    document.getElementById("btEliminar").disabled = false
                    document.getElementById("txId").disabled = true
               }
               else {
                   alert("No existe el registro")
                   document.getElementById("btActualizar").disabled = true
                   document.getElementById("btEliminar").disabled = true
               }
          }else{
               alert("Para leer un registro debe tener una ID de Habitacion, este no puede quedar en blanco")
          }
        }
     this.TECancelar = function(){
          document.getElementById("btActualizar").disabled = true
          document.getElementById("btEliminar").disabled = true
          document.getElementById("btInsertar").disabled = false
          document.getElementById("txdesc").value = ""
          document.getElementById("txId").value = ""
  
          //Habilita los botones para que se vuelvan a ocupar
          document.getElementById("txId").value = ""
          document.getElementById("txId").disabled = false
          document.getElementById("btLeer").disabled = false
          JsTipoEvento.TElistarProductos();
     }
     this.TEEliminar = function (){
          var userselection = confirm("Estas seguro que deseas eliminar este registro?")
          if (userselection == true ){
               var res= ventana.getPost("DELETE","http://localhost:8000/tipoevento/" + document.getElementById("txId").value,"" );
               alert("Registro eliminado correctamente!")
               JsTipoEvento.TECancelar()
          }else{
               JsTipoEvento.TECancelar()
          }
        }
     this.TEActualizar = function (){
        var res= ventana.getPost("PUT","http://localhost:8000/tipoevento/" + document.getElementById("txId").value + "/"
                             ,{
                               "desc_tipoevento": document.getElementById("txdesc").value
                              }
                             );
     JsTipoEvento.TECancelar()
   }
     this.TElistarProductos = function(){
     // Para Destruir, en caso de que quiera recargar la tabla
     $("#tabla").dataTable().fnDestroy();
     $('#tabla').DataTable( {
         ajax:    {
       "url": "http://localhost:8000/tipoevento",
       "dataSrc": ""
     },
     "columns": [
            { "data": "tipoevento_id" },
            { "data": "desc_tipoevento" }
        ],
         deferRender:    true,
         scrollY:        200,
         scrollCollapse: true,
         scroller:       true,
         //retrieve: true,
        // destroy: true,
         loadingRecords: "Cargando...",
         processing:     "Procesando...",
         paging: false,
         //searching: false
     } );
   }
   this.TEInsertar = function (){
     var res= ventana.getPost("POST","http://localhost:8000/tipoevento/"
                          ,{
                            "desc_tipoevento":  document.getElementById("txdesc").value
                          }
                          );
     JsTipoEvento.TECancelar();
     alert("Habitacion registrada correctamente!")
}
}
JsEvento = new EventoJS();
function EventoJS(){
     this.ELeer = function(){
          if (document.getElementById("txId").value != ""){
               var res= ventana.getJSon("http://localhost:8000/evento/" + document.getElementById("txId").value );
               if (typeof(res.evento_id) != null) {
                    document.getElementById("txcapacidad").value =  res.capacidad_evt
                    document.getElementById("txvalor").value =  res.valorevt
                    document.getElementById("cbevento").value =  res.tipoevento_id
                    document.getElementById("btInsertar").disabled = true
                    document.getElementById("btActualizar").disabled = false
                    document.getElementById("btEliminar").disabled = false
                    document.getElementById("txId").disabled = true
               }
               else {
                   alert("No existe el registro")
                   document.getElementById("btActualizar").disabled = true
                   document.getElementById("btEliminar").disabled = true
               }
          }else{
               alert("Para leer un registro debe tener una ID de Habitacion, este no puede quedar en blanco")
          }
        }
     this.ECancelar = function(){
          document.getElementById("btActualizar").disabled = true
          document.getElementById("btEliminar").disabled = true
          document.getElementById("btInsertar").disabled = false
          document.getElementById("txvalor").value = ""
          document.getElementById("txcapacidad").value = ""
          document.getElementById("cbevento").value = ""
          document.getElementById("cbevento").disabled = false
          document.getElementById("txId").value = ""
  
          //Habilita los botones para que se vuelvan a ocupar
          document.getElementById("txId").value = ""
          document.getElementById("txId").disabled = false
          document.getElementById("btLeer").disabled = false
          JsEvento.ElistarProductos();
     }
     this.EEliminar = function (){
          var userselection = confirm("Estas seguro que deseas eliminar este registro?")
          if (userselection == true ){
               var res= ventana.getPost("DELETE","http://localhost:8000/evento/" + document.getElementById("txId").value,"" );
               alert("Registro eliminado correctamente!")
               JsEvento.ECancelar()
          }else{
               JsEvento.ECancelar()
          }
        }
     this.EActualizar = function (){
        var res= ventana.getPost("PUT","http://localhost:8000/evento/" + document.getElementById("txId").value + "/"
                             ,{
                               "valorevt": document.getElementById("txvalor").value,
                               "capacidad_evt": document.getElementById("txcapacidad").value,
                               "tipoevento_id": document.getElementById("cbevento").value
                              }
                             );
     JsEvento.ECancelar()
   }
     this.ElistarProductos = function(){
     // Para Destruir, en caso de que quiera recargar la tabla
     $("#tabla").dataTable().fnDestroy();
     $('#tabla').DataTable( {
         ajax:    {
       "url": "http://localhost:8000/evento",
       "dataSrc": ""
     },
     "columns": [
            { "data": "evento_id" },
            { "data": "valorevt" },
            { "data": "capacidad_evt" },
            { "data": "tipoevento_id" }
        ],
         deferRender:    true,
         scrollY:        200,
         scrollCollapse: true,
         scroller:       true,
         //retrieve: true,
        // destroy: true,
         loadingRecords: "Cargando...",
         processing:     "Procesando...",
         paging: false,
         //searching: false
     } );
   }
   this.EInsertar = function (){
     var res= ventana.getPost("POST","http://localhost:8000/evento/"
                          ,{
                            "valorevt":  document.getElementById("txvalor").value,
                            "capacidad_evt":  document.getElementById("txcapacidad").value,
                            "tipoevento_id":  document.getElementById("cbevento").value
                          }
                          );
     JsEvento.ECancelar();
     alert("Habitacion registrada correctamente!")
}
}
JsUsuario = new UsuarioJS();
function UsuarioJS(){
     this.ULeer = function(){
          if (document.getElementById("txId").value != ""){
               var res= ventana.getJSon("http://localhost:8000/usuario/" + document.getElementById("txId").value );
               if (typeof(res.id_usuario) != null) {
                    document.getElementById("txuser").value =  res.nombre_usuario
                    document.getElementById("txcorreo").value =  res.correo_usuario
                    document.getElementById("txfecnac").value =  res.fechanac_usuario
                    document.getElementById("txfono").value =  res.fono_usuario
                    document.getElementById("txfecre").value =  res.fecha_registro
                    document.getElementById("btInsertar").disabled = true
                    document.getElementById("txfecre").disabled = true
                    document.getElementById("btActualizar").disabled = false
                    document.getElementById("txId").disabled = true
               }
               else {
                   alert("No existe el registro")
                   document.getElementById("btActualizar").disabled = true
                   document.getElementById("btEliminar").disabled = true
               }
          }else{
               alert("Para leer un registro debe tener una ID de Habitacion, este no puede quedar en blanco")
          }
        }
     this.UCancelar = function(){
          document.getElementById("btActualizar").disabled = true
          document.getElementById("btInsertar").disabled = true
          document.getElementById("txuser").value = ""
          document.getElementById("txcorreo").value = ""
          document.getElementById("txfono").value = ""
          document.getElementById("txfecnac").value = ""
          document.getElementById("txfecre").disabled = true
          document.getElementById("txfecre").value = ""
          
          document.getElementById("txId").value = ""
          document.getElementById("txId").disabled = false
          document.getElementById("btLeer").disabled = false
          JsUsuario.UlistarProductos();
     }
     this.UEliminar = function (){
          var userselection = confirm("Estas seguro que deseas eliminar este registro?")
          if (userselection == true ){
               var res= ventana.getPost("DELETE","http://localhost:8000/usuario/" + document.getElementById("txId").value,"" );
               alert("Registro eliminado correctamente!")
               JsUsuario.UCancelar()
          }else{
               JsUsuario.UCancelar()
          }
        }
     this.UActualizar = function (){
        var res= ventana.getPost("PUT","http://localhost:8000/usuario/" + document.getElementById("txId").value + "/"
                             ,{
                               "valorevt": document.getElementById("txvalor").value,
                               "capacidad_evt": document.getElementById("txcapacidad").value,
                               "tipoevento_id": document.getElementById("cbevento").value
                              }
                             );
     JsUsuario.UCancelar()
   }
     this.UlistarProductos = function(){
     // Para Destruir, en caso de que quiera recargar la tabla
     $("#tabla").dataTable().fnDestroy();
     $('#tabla').DataTable( {
         ajax:    {
       "url": "http://localhost:8000/usuario",
       "dataSrc": ""
     },
     "columns": [
            { "data": "id_usuario" },
            { "data": "nombre_usuario" },
            { "data": "correo_usuario" },
            { "data": "fechanac_usuario" },
            { "data": "fono_usuario" }
        ],
         deferRender:    true,
         scrollY:        200,
         scrollCollapse: true,
         scroller:       true,
         //retrieve: true,
        // destroy: true,
         loadingRecords: "Cargando...",
         processing:     "Procesando...",
         paging: false,
         //searching: false
     } );
   }
   this.UInsertar = function (){
     var today = new Date();
     var date = today.getDate()+'-'+(today.getMonth()+1)+'-'+today.getFullYear();
     var res= ventana.getPost("POST","http://localhost:8000/usuario/"
                          ,{
                            "nombre_usuario":  document.getElementById("txvalor").value,
                            "passwd_usuario":  document.getElementById("txcapacidad").value,
                            "correo_usuario":  document.getElementById("cbevento").value,
                            "fechanac_usuario":  document.getElementById("cbevento").value,
                            "fono_usuario":  document.getElementById("cbevento").value,
                            "fecha_registro":  date
                          }
                          );
     alert("Habitacion registrada correctamente!")
}
}