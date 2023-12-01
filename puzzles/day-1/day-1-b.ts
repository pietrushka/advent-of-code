import { readData } from '../../shared.ts';
import chalk from 'chalk';

const numberLikeRegex = /[0-9]|one|two|three|four|five|six|seven|eight|nine/g;

const getRealInt = (string: string) => {
  const [numberLikeMatch] = string.match(numberLikeRegex) ?? [];

  if (!numberLikeMatch) return null;

  switch (numberLikeMatch) {
    case 'one':
      return 1;
    case 'two':
      return 2;
    case 'three':
      return 3;
    case 'four':
      return 4;
    case 'five':
      return 5;
    case 'six':
      return 6;
    case 'seven':
      return 7;
    case 'eight':
      return 8;
    case 'nine':
      return 9;
  }

  return parseInt(numberLikeMatch);
};

const findFirstNumber = (line, stringPartial) => {
  const realInt = getRealInt(stringPartial);
  if (realInt) {
    return realInt;
  }
  return findFirstNumber(line, line.slice(0, stringPartial.length + 1));
};

const findLastNumber = (line, stringPartial) => {
  const realInt = getRealInt(stringPartial);
  if (realInt) {
    return realInt;
  }
  return findLastNumber(line, line.slice((stringPartial.length + 1) * -1));
};

export async function day1b(dataPath?: string) {
  const data = await readData(dataPath);
  let numbers = [];
  for (let line of data) {
    numbers.push(
      parseInt(
        `${findFirstNumber(line, line[0])}${findLastNumber(
          line,
          line[line.length - 1]
        )}`
      )
    );
  }
  return numbers.reduce((acc, x) => acc + x, 0);
}

const answer = await day1b();
console.log(chalk.bgGreen('Your Answer:'), chalk.green(answer));
