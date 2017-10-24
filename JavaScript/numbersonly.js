var numbersOnly = function(items) {

  // placeholder array that will hold all the numeric values after the type has been determined
  var placeHolder = [];


  // a simple for loop that will go through each one of the items and check what it is, we know how to loop based on the number of items

  for(var i = 0; i < items.length; i++) {

    // if the item at position i is of numeric type we push the item into the placeholder array, this does not disturb position
    if (typeof items[i] == "number"){
      placeHolder.push(items[i]);
    }
  }

  // finally, we return the placeHolder array since it has all of its values sorted out
  return placeHolder;

}


// tests

var tests = numbersOnly([1, 2, 3, "number", "cuatro", 6]);

var newArray = numbersOnly([1, "apple", -3, "orange", 0.5]);

console.log(tests);
console.log(newArray);
