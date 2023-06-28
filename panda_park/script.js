
function vnesenie() {
    let heigth = document.getElementById('rost').value
    heigth.innerHtml = 'text';
    return heigth;
};

function knopka () {
    let znachenie = document.getElementById('otvet').onclick;
    
    return znachenie;
}

function table (){
    let tbl = document.getElementById('zapis')
    tbl.innerHTML = '<tr><td>' + imya + '</td>';
    tbl.innerHTML = '<td>' + rost.value + 'cm </td></tr>';



}

function save () {
    nazv.push(imy);
    heigth.push(rost);
    document.getElementById('spisok').innerHTML = spisok(nazv, heigth)
}