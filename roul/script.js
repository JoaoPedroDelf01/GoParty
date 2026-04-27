function enviarBar(){
    const barName = document.getElementById("addBar").value

    fetch("http://127.0.0.1:8000/adicionar", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' 
        },

        body: JSON.stringify({bar: String(barName)})
    }) 
    .then(res => res.json())
    .then(data => {
        console.log(data)
        if (data.status == false){
            document.getElementById("mensagem").innerText = "Erro ao adicionar bar"
        }
        if (data.status == true){
            document.getElementById("mensagem").innerText = "Bar adicionado com sucesso"
        } 
    })
}

