function arrayFunc(){
  var num = []
  for (var i = 0; i <= 100; i++) {
    if ((i % 2) == 0) {
      num.push(i);
    }
}
  return num;
  }
console.log(arrayFunc());
