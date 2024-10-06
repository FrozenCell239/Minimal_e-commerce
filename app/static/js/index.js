// Flash dismiss
function flashDismiss(id){
    document.getElementById(`flash-${id}`).remove();
};

// Dialogs handling
function openDialog(route, message){
    document.getElementsByTagName('dialog')[0].showModal();
    document.getElementsByTagName('dialog')[0].style.display = 'flex';
    document.getElementById('dialog-message').innerText = message;
    document.getElementById('dialog-confirm').setAttribute('href', route);
};
function closeDialog(){
    document.getElementsByTagName('dialog')[0].close();
    document.getElementsByTagName('dialog')[0].style.display = 'none';
};