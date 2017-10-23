function sumOfMultiplesBelow(maxNum: number) {
  let sum = 0;
  for (let eachNum = 0; eachNum < maxNum; eachNum++) {
    if (eachNum % 3 == 0 || eachNum % 5 == 0) {
      sum += eachNum;
    }
  }
  return sum;
}

function problem1() {
  let maxNum : number = parseFloat((<HTMLInputElement>document.getElementById("problem1input")).value);
  document.getElementsByTagName('p1answer')[0].innerHTML = String(sumOfMultiplesBelow(maxNum));
}
problem1();