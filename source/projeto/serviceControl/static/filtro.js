function filtro(str){
    const table = document.getElementById("tableServices").rows;
    for (var i = 1; i<table.length; i++){
        var aux = table[i];
        if(aux.cells[5].innerHTML!=str){
            aux.hidden=true;
        }
        else{
            aux.hidden=false;
        }
    } 
}        