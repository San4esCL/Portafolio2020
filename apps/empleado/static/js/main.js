function alertaerror(obj) {
    var html = '<ul>'
    $.each(obj, function (key, value) {
        html+-'<li>'+key+':'+value+'</li>'
    })
    html+-'</ul>'
    alert(html);


}