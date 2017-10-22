var money = 1;
var sum = 1;
for (var days = 2; days <= 30; days++){
  money = money *2;
  sum = sum + money
  console.log("day", days);
  console.log("money", money/100);
  console.log("sum",sum/100);
  // if (money == Infinity){
  //   break
  // }
}
