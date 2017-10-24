var numbersOnly = function (list){

var placeHolder = [];

for(var i = 0; i < list.length; i ++){
  if(typeof list[i] == "number"){
    placeHolder.push(list[i]);

  }
}
  return placeHolder;
}

  var test = numbersOnly([23, "apples", "bannana", 123987, "true", 843, -9843, "hopethisworks"])
  console.log(test);
