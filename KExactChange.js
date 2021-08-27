let coins = [];
let test_cases_no = parseInt(readline(), 10);
while (test_cases_no > 0) {
  table[0] = 0;
  const price = parseInt(readline());
  const coins_no = parseInt(readline());
  for (let i = 0; i < coins_no; i += 1) {
    coins.push(parseInt(readline()));
  }
  for (let i = 0; i < coins_no; i += 1) {
    let crt_price = price - 1;
    while (crt_price >= 0) {
      if (table[crt_price] === 10001) {
        crt_price -= 1;
        continue;
      }
      if (table[crt_price + coins[i]] > table[crt_price] + 1) {
        table[crt_price + coins[i]] = table[crt_price] + 1;
      }
      crt_price -= 1;
    }
  }
  let i = price
  while (true) {
    if (table[i] != 10001) {
      break;
    }
    i += 1;
  }
  print(i + ' ' + table[i]);
  test_cases_no -= 1;
  coins = [];
}