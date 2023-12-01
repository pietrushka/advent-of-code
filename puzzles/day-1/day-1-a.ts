import { readData } from '../../shared.ts';
import chalk from 'chalk';

export async function day1a(dataPath?: string): Promise<number> {
  const data = await readData(dataPath);
  let numbers = [];
  for (let line of data) {
    const lineNums = line
      .match(/[0-9]|one|two|three|four|five|six|seven|eight|nine/g)
      .map((x) => {
        if (/[0-9]/.test(x)) {
          return parseInt(x);
        }

        switch (x) {
          case 'one':
            return '1';
          case 'two':
            return '2';
          case 'three':
            return '3';
          case 'four':
            return '4';
          case 'five':
            return '5';
          case 'six':
            return '6';
          case 'seven':
            return '7';
          case 'eight':
            return '8';
          case 'nine':
            return '9';
        }
      });
    numbers.push(parseInt(`${lineNums[0]}${lineNums[lineNums.length - 1]}`));
  }
  return numbers.reduce((acc, x) => acc + x, 0);
}

const answer = await day1a();
console.log(chalk.bgGreen('Your Answer:'), chalk.green(answer));
