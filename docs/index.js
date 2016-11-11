
$.getJSON("song1.json",function (data){
    run(data,document.getElementById("innercontainer1"),document.getElementById("song1title"));
});
$.getJSON("song2.json",function (data){
    run(data,document.getElementById("innercontainer2"),document.getElementById("song2title"));
});



function run(data,dom_element,title_div){
  var song = dom_element;
  var lines = data.text.split("</br>");
  var title = document.createElement("h2");
  title.innerHTML = lines[0]+"</br>";
  title.setAttribute("style","font-family: 'Calligraffitti', cursive; font-size:35px;");
  title_div.appendChild(title);
  (function startLine(i){
    var line = document.createElement("p");
    line.className = "line";
    line.innerHTML = lines[i];
    i++;
    song.appendChild(line);
    if(i == lines.length){
      return;
    }
    startLine(i+1);
  }
)(1);
}
