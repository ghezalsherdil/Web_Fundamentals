var onlyNumbers = function (list){
  var container = []
  for (var i = 0; i < list.length; i++){
    if (typeof list[i] == "number"){
      container.push(list[i]);
    }
  }
  return container
}
var test =onlyNumbers([12,"hello",473289, -9834,"ok",-984])
console.log(test);
