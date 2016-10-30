
$.getJSON("song2.json",function (data){
    run(data);
    });


function run(data){
  var song = document.getElementById("song");
  var lines = data.text.split("</br>");
  var i = 0;
  (function startLine(){
    var line = document.createElement("p");
    line.className = "line";
    line.innerHTML = lines[i];
    i++;
    song.appendChild(line);
    if(i == lines.length){
      return;
    }
    setTimeout(startLine,100);
  }
  )();
}
