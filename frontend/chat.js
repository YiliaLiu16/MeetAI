setInterval(sendmsg, 1000)
function sendmsg() {
    var input = document.getElementById("userinput").value;
    var div_id = document.getElementById("recommendation")
    var respond1 = document.getElementById("res1")
    var respond2 = document.getElementById("res2")
    var respond3 = document.getElementById("res3")
    if (input != "")
    {
        div_id.style.display = "block";
        const response = new XMLHttpRequest();
        response.open("POST", "http://localhost:8001/chat");
        response.send(input);
        response.onload = function(){
            var res = JSON.parse(response.responseText)
            respond1.innerHTML = res.res1;
            respond2.innerHTML = res.res2;
            respond3.innerHTML = res.res3;   
        }
    }
    else{
        div_id.style.display = "none";
    }
}

function hide_recomendation(){
    let init=false;

    if (!init)
    {
        var div_id = document.getElementById("recommendation")
        div_id.style.display = "none";
        init=true
    }
}
hide_recomendation()