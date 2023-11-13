#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let result = '';
  for (let i = 0; i < size; i++) {
    result += 'x';
  }
  let i = 0;
  while (i < size) {
    console.log(result);
    i++;
  }
}
