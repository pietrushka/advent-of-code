import { readData } from '../../shared.ts'
import chalk from 'chalk'

function sumNumArray(nums: number[]) {
	return nums.reduce((acc, x) => acc + x, 0)
}

function parseNumberPart(numString) {
	return numString.split(' ').flatMap((x) => (x ? [Number(x)] : []))
}

function parseLine(line) {
	const [winningNumsText, myNumsText] = line
		.split('|')
		.map((part) => part.trim())
	return {
		winningNums: parseNumberPart(winningNumsText),
		myNums: parseNumberPart(myNumsText),
	}
}

function getCardMatchCount(line) {
	const { winningNums, myNums } = parseLine(line)
	return winningNums.reduce(
		(acc, winningNum) => (myNums.includes(winningNum) ? acc + 1 : acc),
		0
	)
}

export async function day4b(dataPath?: string) {
	const cards = await readData(dataPath)

	const copies = Array(cards.length).fill(1)

	for (let [cardIdx, card] of cards.entries()) {
		const matchCount = getCardMatchCount(card)

		for (let i = 0; i < matchCount; i++) {
			copies[cardIdx + i + 1] += copies[cardIdx]
		}
	}

	return sumNumArray(copies)
}

const answer = await day4b()
console.log(chalk.bgGreen('Your Answer:'), chalk.green(answer))
