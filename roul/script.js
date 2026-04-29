
function sendPlace(){
    const placeName = document.getElementById("namePlace").value

    fetch("http://127.0.0.1:8000/append", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' 
        },

        body: JSON.stringify({place: String(placeName)})
    }) 
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.status == false){
            document.getElementById("answer").innerText = data.erro;
        }
        else{
            document.getElementById("answer").innerText = data.answer;
        }

        if(data.list.status == false){
            console.log(data.list_etc.status.erro)
        }
        else{
            console.log(data.list.answer)
        }
    });
    
}

function deletePlace(){
    const placeName = document.getElementById("namePlace").value

    fetch("http://127.0.0.1:8000/remove", {
        method: "DELETE",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({place: String(placeName)})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.status == false){
            document.getElementById("answer").innerText = data.erro;
        }
        else{
            document.getElementById("answer").innerText = data.answer;
        }
        
    });
}

function draw(){

    fetch("http://127.0.0.1:8000/draw", {
        method:"GET",
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data =>{
        console.log(data)
        if(data.status == false){
            document.getElementById("answer").innerText = data.erro;
        }
        else{
            document.getElementById("answer").innerText = data.answer;
        }
    });
}


