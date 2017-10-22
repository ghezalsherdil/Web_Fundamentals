var HOUR = 12;
var MINUTE = 12;
var PERIOD = "AM";

if (MINUTE <30){
  if (PERIOD == "AM"){
    console.log ("just after " + HOUR + " in the morning")
  }
  else{
    console.log("just after " + HOUR + " in the evening")
  }

}
else {
  var newHour= HOUR + 1;

  if (newHour > 12 && PERIOD == "PM"){
    newHour = 1;
    PERIOD = "AM";
  }

  if (newHour > 12 && PERIOD == "AM"){
    newHour = 1;
    PERIOD = "PM";
  }

  if (PERIOD == "AM"){
    console.log ("its almost " + (newHour) + " in the morning")
  }
  else{
    console.log("its almost " + (newHour) + " in the evening")
  }
}
