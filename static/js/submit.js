
function submit(weekday)
{
  if(typeof(weekday)==="undefined")
  { 
    if(document.getElementById('mon')["checked"] === true)
      weekday = 0;
    else if(document.getElementById('tue')["checked"] === true)
      weekday = 1;
    else if(document.getElementById('wed')["checked"] === true)
      weekday = 2;
    else if(document.getElementById('thu')["checked"] === true)
      weekday = 3;
    else if(document.getElementById('fri')["checked"] === true)
      weekday = 4;
  
  }
  var select = document.getElementById("office");
  var option = select.options[select.selectedIndex].id;
  var input = document.getElementById("mon");
	var xmlhttp=new XMLHttpRequest();
	xmlhttp.onreadystatechange=function()
  	{
  		if (xmlhttp.readyState==4 && xmlhttp.status==200)
    	{
    		document.getElementById("head").innerHTML=xmlhttp.responseText;
    	}
  	}
	xmlhttp.open("POST","/submit/",true);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
  xmlhttp.send("office="+option+"&weekday="+weekday);
}

