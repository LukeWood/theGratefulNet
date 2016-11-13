
$.getJSON("song1.json",function (data){
    run(data,document.getElementById("innercontainer1"),document.getElementById("song1title"));
});
$.getJSON("song2.json",function (data){
    run(data,document.getElementById("innercontainer2"),document.getElementById("song2title"));
});

$.getJSON("song3.json",function(data){
  run(data,document.getElementById("innercontainer3"),document.getElementById("song3title"));
});

if(typeof(String.prototype.trim) === "undefined")
{
    String.prototype.trim = function()
    {
        return String(this).replace(/^\s+|\s+$/g, '');
    };
}

function capitolize(str){
  var val = str.trim()
  if(val.length <= 1){
    return "";
  }
  return val[0].toUpperCase() + val.slice(1);
}

function run(data,dom_element,title_div){
  var song = dom_element;
  var lines = data.text.split("</br>");
  console.log(lines);
  var title = document.createElement("h2");
  title.innerHTML = lines[0]+"</br>";
  title.setAttribute("style","font-family: 'Calligraffitti', cursive; font-size:35px;");
  title_div.appendChild(title);

  (function startLine(i){
    if(i >= lines.length){
      return;
    }
    var line = document.createElement("p");
    line.className = "line";
    line.innerHTML = capitolize(lines[i]);
    i++;
    if(line.innerHTML.length > 1){
      song.appendChild(line);
    }

    startLine(i+1);
  }
)(1);

}
