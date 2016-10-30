
$.getJSON("song2.json",function (data){
    run(data);
    });


function run(data){
  var song = document.getElementById("song");
  var lines = data.text.split("</br>");
  var i = 1;
  var title = document.createElement("h2");
  title.innerHTML = lines[0];
  document.getElementById("cen").appendChild(title);
  (function startLine(){
    var line = document.createElement("p");
    line.className = "line";
    line.innerHTML = lines[i];
    i++;
    song.appendChild(line);
    if(i == lines.length){
      return;
    }
    setTimeout(startLine,1000);
  }
  )();
}
