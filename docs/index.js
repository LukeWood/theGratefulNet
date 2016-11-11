
$.getJSON("song1.json",function (data){
    run(data);
});
$.getJSON("song2.json",function (data){
    run2(data);
});
function run2(data){
  var song = document.getElementById("innercontainer2");
  var lines = data.text.split("</br>");
  var i = 1;
  var title = document.createElement("h2");
  title.innerHTML = lines[0]+"</br>";
  title.setAttribute("style","font-family: 'Calligraffitti', cursive; font-size:35px;");
  document.getElementById("song2title").appendChild(title);
  (function startLine(){
    var line = document.createElement("p");
    line.className = "line";
    line.innerHTML = lines[i];
    i++;
    song.appendChild(line);
    if(i == lines.length){
      return;
    }
//    setTimeout(startLine,300);

    startLine();
  }
  )();
}


function run(data){
  var song = document.getElementById("innercontainer1");
  var lines = data.text.split("</br>");
  var i = 1;
  var title = document.createElement("h2");
  title.innerHTML = lines[0];
  title.setAttribute("style","font-family: 'Calligraffitti', cursive; font-size:35px;");
  document.getElementById("song1title").appendChild(title);
  (function startLine(){
    var line = document.createElement("p");
    line.className = "line";
    line.innerHTML = lines[i];
    i++;
    song.appendChild(line);
    if(i == lines.length){
      return;
    }
  //  setTimeout(startLine,300);
    startLine();
  }
  )();
}
