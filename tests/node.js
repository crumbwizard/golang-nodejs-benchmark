let [arr, i] = [[1, 1], 0];

while (i < 100_000) {
  let val = 0;

  for (let e = 0; e < arr.length; e++) {
    val += arr[e];
  }

  arr.push(val);
  i += 1;
}