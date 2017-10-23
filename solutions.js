function sumOfMultiplesBelow(maxNum) {
    var sum = 0;
    for (var eachNum = 0; eachNum < maxNum; eachNum++) {
        if (eachNum % 3 == 0 || eachNum % 5 == 0) {
            sum += eachNum;
        }
    }
    return sum;
}
function problem1() {
    var maxNum = parseFloat(document.getElementById("problem1input").value);
    document.getElementsByTagName('p1answer')[0].innerHTML = String(sumOfMultiplesBelow(maxNum));
}
problem1();
