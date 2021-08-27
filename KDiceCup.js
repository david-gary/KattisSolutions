let line = readline().split(' ');
let results = [];
const N = parseInt(line[0], 10);
const M = parseInt(line[1], 10);
let dice = [N, M];
dice.sort((a, b) => {
  return a - b;
});
for (let i = dice[0] + 1; i <= dice[1] + 1; i += 1) {
  results.push(i);
}