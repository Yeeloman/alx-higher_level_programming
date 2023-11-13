#!/usr/bin/node

if (isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  let result = '';
  for (let i = 0; i < Number(process.argv[2]); i++) {
    result += 'x';
  }
  let i = 0;
  while (i < Number(process.argv[2])) {
    console.log(result);
    i++;
  }
}
