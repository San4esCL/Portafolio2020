ventana = new Ventana();

function Ventana(){
    this.showHTML = function (objContainer,stPagina){
      
			   var datosxx="";
           $.ajax({
                  type: "GET",
                  url: stPagina ,
                  async: false,
                  cache: false,
                  //headers: "stHeader",
                  //contentType: "application/json; charset=utf-8",
                  success: function (response) {
                        //alert("success" + response);
                        //  document.write (response)
                        datosxx = response;
                    },
                  error: function (msg, status, errorThrown) {
                          alert("success" + response);       
                          alert (msg)
                            datosxx = "Error " + msg
                            //wndMsgAlert("Error" + msg);
                            //wndMsgAlert(errorThrown+'\n'+status+'\n'+msg.statusText+'\n>>1.-'+msg.responseText);
                            datosxx=null;
                  }
            });
        document.getElementById(objContainer).innerHTML = datosxx;
    }
    this.getJSon = function (stPagina){
			var datosxx="";
           $.ajax({
                  type: "GET",
                  url: stPagina ,
									//contentType: "application/json; charset=utf-8",
									//dataType: "json",
                  async: false,
                  cache: false,
                  //headers: "stHeader",
                  //contentType: "application/json; charset=utf-8",
                  success: function (response) {
                        
                        //  document.write (response)
                        datosxx = response;
                    },
                  error: function (msg, status, errorThrown) {
											if (msg.detail.equals("Not found."))
	                  	    
	                        datosxx = "Error " + msg
	                        //wndMsgAlert("Error" + msg);
	                        //wndMsgAlert(errorThrown+'\n'+status+'\n'+msg.statusText+'\n>>1.-'+msg.responseText);
	                        datosxx=null;
                  }
            });
					return datosxx;
    }
		this.getPost = function (stType,stPagina,stData){
			var datosxx="";
           $.ajax({
                  type: stType,
                  url: stPagina ,
									data: stData,
									//contentType: "application/json; charset=utf-8",
									dataType: "json",
                  async: false,
                  cache: false,
                  //headers: "stHeader",
                  //contentType: "application/json; charset=utf-8",
                  success: function (response) {
                        
                        //  document.write (response)
                        datosxx = response;
                    },
                  error: function (msg, status, errorThrown) {
                  	         
                            datosxx = "Error " + msg
                            //wndMsgAlert("Error" + msg);
                            //wndMsgAlert(errorThrown+'\n'+status+'\n'+msg.statusText+'\n>>1.-'+msg.responseText);
                            datosxx=null;
                  }
            });
    }
}


