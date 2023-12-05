import { readData } from '../../shared.ts'
import chalk from 'chalk'

function sumNumArray(nums: number[]) {
	return nums.reduce((acc, x) => acc + x, 0)
}

function parseNumberPart(numString: string) {
	return numString.split(' ').flatMap((x) => (x ? [Number(x)] : []))
}

function parseLine(line: string) {
	const [winningNumsText, myNumsText] = line.split(': ')[1].split(' | ')
	return {
		winningNums: parseNumberPart(winningNumsText),
		myNums: parseNumberPart(myNumsText),
	}
}

function calcPoints(matchCount: number) {
	if (matchCount === 0) return 0
	let result = 1
	for (let i = 1; i < matchCount; i++) {
		result = result * 2
	}
	return result
}

function getCardPoints(line: string) {
	const { winningNums, myNums } = parseLine(line)
	const matchCount = winningNums.reduce((acc, winningNum) => {
		if (myNums.includes(winningNum)) {
			return acc + 1
		}
		return acc
	}, 0)
	return calcPoints(matchCount)
}

export async function day4a(dataPath?: string) {
	const data = await readData(dataPath)
	const cardsPoints = data.map(getCardPoints)
	return sumNumArray(cardsPoints)
}

const answer = await day4a()
console.log(chalk.bgGreen('Your Answer:'), chalk.green(answer))
