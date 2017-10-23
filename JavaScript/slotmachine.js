function slotMachine(quarters) {
  while (quarters > 0) {
    var winningChance = Math.floor(Math.random()*100) + 1;
    console.log(winningChance);
    if (27 == winningChance){
      //you win if 27
      console.log("You WIN!");
      var reward = Math.floor(Math.random()*51) + 50;
      console.log('current quarters', quarters);
      console.log('current reward', reward);
      return quarters + reward;
    }
    else{
      console.log("Please try again");
    }
    quarters--;
  }
  return quarters;
}
var total = slotMachine(27);
console.log(total);
