const usinas = document.getElementById('usinas');
const cliente = document.getElementById('cliente');
const navio = document.getElementById('navio');
const porto = document.getElementById('porto');
const servico = document.getElementById('servico');
usinas.style.display    ='none';
navio.style.display     ='none';
porto.style.display     ='none';
cliente.style.display   ='none';
servico.style.display   ='block';

function mostrarUsina(){
    usinas.style.display    ='block';
    navio.style.display     ='none';
    porto.style.display     ='none';
    cliente.style.display   ='none';
    servico.style.display   ='none';
}
function mostrarCliente(){
    usinas.style.display    ='none';
    navio.style.display     ='none';
    porto.style.display     ='none';
    cliente.style.display   ='block';
    servico.style.display   ='none';
}
function mostrarNavio(){
    usinas.style.display    ='none';
    navio.style.display     ='block';
    porto.style.display     ='none';
    cliente.style.display   ='none';
    servico.style.display   ='none';
}
function mostrarPorto(){
    usinas.style.display    ='none';
    navio.style.display     ='none';
    porto.style.display     ='block';
    cliente.style.display   ='none';
    servico.style.display   ='none';
}
function mostrarServico(){
    usinas.style.display    ='none';
    navio.style.display     ='none';
    porto.style.display     ='none';
    cliente.style.display   ='none';
    servico.style.display   ='block';
}