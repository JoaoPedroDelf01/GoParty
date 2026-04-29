function sendPlace(){
    const placeName = document.getElementById("namePlace").value

    fetch("http://127.0.0.1:8000/adicionar", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' 
        },

        body: JSON.stringify({place: String(placeName)})
    }) 
    .then(res => res.json())
    .then(data => {
        console.log(data)
        if (data.status == false){
            document.getElementById("answer").innerText = data.erro
        }
        else{
            document.getElementById("answer").innerText = data.mensagem
        } 
    })
}

function deletePlace(){
    const placeName = document.getElementById("namePlace").value

    fetch("http://127.0.0.1:8000/remover", {
        method: "DELETE",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({place: String(placeName)})
    })
    .then(res => res.json())
    .then(data => {
        console.log(data)
        if (data.status == false){
            document.getElementById("answer").innerText = data.erro
        }
        else{
            document.getElementById("answer").innerText = data.mensagem
        }
        
    })
}

function draw(){

    fetch("http://127.0.0.1:8000/sortear", {
        method:"GET",
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(res => res.json())
    .then(data =>{
        console.log(data)
        if(data.status == false){
            document.getElementById("answer").innerText = data.erro
        }
        else{
            document.getElementById("answer").innerText = data.vencedor
        }
    })
}