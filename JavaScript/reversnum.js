function reverse(num) {
  console.log(num);
  var rev = "";
  while(num > 0) {
    var lastNum = num % 10;
    rev = rev + lastNum;
    num /= 10;
    num = Math.floor(num);
  }
  console.log(rev);
}
reverse(1234567890);
