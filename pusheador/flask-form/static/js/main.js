const btnDelete = document.querySelectorAll('.btn-delete')

// Esto retornado es una lista de nodos, lo voy a pasar a arreglo
if(btnDelete) {
    const btn_array = Array.from(btnDelete);
    btn_array.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('Are you sure you want to delete it ?')) {
                e.preventDefault();
            }
        });
    });
}