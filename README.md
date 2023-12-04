# Golang vs NodeJS Performance Test
This is a test of how fast go is compared to nodejs. I'm doing this for a school project and I only have a few days to do it so it won't be very good.

## Testing
I ran the tests with python subprocesses while Vscode and Firefox were running (I forgot to close them). The scripts I tested were run 50 times each, taking the time in milliseconds at the start and end of each run. The time taken from each run was put into the [performance.json](https://github.com/kierancrumb/golang-vs-nodejs/blob/main/performance.json) file.

## Algorithm
My algorithm makes a list with the values `[1, 1]`, adds the sum of all the values in the array to the end of it, and reapeats that 100,000 times. The algorithm is pretty much the same in both languages.

Implementation in javascript:
```
let [arr, i] = [[1, 1], 0];

while (i < 100_000) {
  let val = 0;

  for (let e = 0; e < arr.length; e++) {
    val += arr[e];
  }

  arr.push(val);
  i += 1;
}
```