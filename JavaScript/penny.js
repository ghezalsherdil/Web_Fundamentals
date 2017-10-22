function testfunction(days, money, sum) {
  dayfumction(days);
  console.log("money", money/100);
  console.log("sum",sum/100);
}
function dayfumction(days){
  console.log("day", days);
}
var money = 1;
var sum = 1;
for (var days = 2; days <= 30; days++){
  money = money *2;
  sum = sum + money;
testfunction (days, money, sum)
  // if (money == Infinity){
  //   break
  // }
}


function greetSomeone(person)
{
  if (person == "Martin") {
    console.log("Yo dawg, howz it goin?");
  }
  else {
    console.log("Greetings Earthling!");
  }
}

greetSomeone("Martingk")
