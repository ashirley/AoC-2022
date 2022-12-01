/^\s*$/ { 
  if (currTotal > biggestTotal[0]) {
    biggestTotal[2] = biggestTotal[1];
    biggestTotal[1] = biggestTotal[0];
    biggestTotal[0] = currTotal;
  } else if (currTotal > biggestTotal[1]) {
    biggestTotal[2] = biggestTotal[1];
    biggestTotal[1] = currTotal;
  } else if (currTotal > biggestTotal[2]) {
    biggestTotal[2] = currTotal;
  }
  currTotal = 0;
  next
}

{
   currTotal = currTotal + $1
}
END { print biggestTotal[0] + biggestTotal[1] + biggestTotal[2] }
