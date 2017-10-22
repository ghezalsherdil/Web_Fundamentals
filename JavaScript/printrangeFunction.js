function printRange(startPoint, endPoint, skipAmount) {
  for (var i = startPoint; i < endPoint; i = i+ skipAmount) {
    console.log(i);
  }
}
printRange(2, 10, 2);
