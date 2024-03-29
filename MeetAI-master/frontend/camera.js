var constraints = { video: { facingMode: "user" }, audio: false };
const cameraView = document.querySelector("#camera--view"),
      cameraOutput = document.querySelector("#camera--output"),
      cameraSensor = document.querySelector("#camera--sensor"),
      cameraTrigger = document.querySelector("#camera--trigger")


function cameraStart() {
    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(function(stream) {
        track = stream.getTracks()[0];
        cameraView.srcObject = stream;
    })
    .catch(function(error) {
        console.error("Oops. Something is broken.", error);
    });
}
window.addEventListener("load", cameraStart, false);

setInterval(saveImg, 1000)
function saveImg(){
    cameraSensor.width = cameraView.videoWidth;
    cameraSensor.height = cameraView.videoHeight;
    cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
    cameraOutput.src = cameraSensor.toDataURL("image/jpg");
    const data = JSON.stringify({
        image: cameraOutput.src
    });
    
    const response = new XMLHttpRequest();
    response.open("POST", "http://localhost:8001/upload");
    response.setRequestHeader("Content-Type", "application/json");
    response.send(data);
    response.onload = function(){
        var res = JSON.parse(response.responseText)
        console.log(res.emoji);
        if (res.emoji == 0)
        {
            document.getElementById("emoji_img").setAttribute("src", "./emoji/smile.png");
        }
        else if(res.emoji == 1)
        {
            document.getElementById("emoji_img").setAttribute("src", "./emoji/node.png");
        }
        else if(res.emoji == 2)
        {
            document.getElementById("emoji_img").setAttribute("src", "./emoji/applaud.png");
        }
        else if(res.emoji == 3)
        {
            document.getElementById("emoji_img").setAttribute("src", "./emoji/good.png");
        }
        else if(res.emoji == 4)
        {
            document.getElementById("emoji_img").setAttribute("src", "./emoji/hello.png");
        }
        else if(res.emoji == -1)
        {
            document.getElementById("emoji_img").setAttribute("src", "empty.png");
        }
    }

}


