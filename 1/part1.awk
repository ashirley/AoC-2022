BEGIN { biggestIndex=-1; biggestTotal=0; currTotal=0; currIndex=0; }
/^\s*$/ { 
  print currIndex
  if (currTotal > biggestTotal) {
    biggestIndex = currIndex;
    biggestTotal = currTotal;
  }
  currIndex++;
  currTotal = 0;
  next
}

{
   currTotal = currTotal + $1
}
END { print biggestIndex, biggestTotal }
