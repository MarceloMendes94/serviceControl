/*preenchendo meses*/
var x = document.getElementById("mes");
var meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'];
for(var i = 0; i < meses.length; i++){
    var option = document.createElement("option");
    option.value = i+1;
    option.innerHTML = meses[i];
    x.appendChild(option);
}    
