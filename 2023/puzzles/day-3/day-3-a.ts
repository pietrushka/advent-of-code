import { readData } from '../../shared.ts'
import chalk from 'chalk'

function sumNumArray(nums: number[]) {
	return nums.reduce((acc, x) => acc + x, 0)
}

function getChar(x: number, y: number, data: string[]): string | undefined {
	return data?.[y]?.[x]
}

function checkSymbolNerby(x: number, y: number, data: string[]) {
	const coordinates = [
		[x, y - 1],
		[x + 1, y - 1],
		[x + 1, y],
		[x + 1, y + 1],
		[x, y + 1],
		[x - 1, y + 1],
		[x - 1, y],
		[x - 1, y - 1],
	]

	return coordinates.some(([positionX, positionY]) => {
		const char = getChar(positionX, positionY, data)
		const isCharSymbol = /[^\w\s.]/.test(char)
		return isCharSymbol
	})
}

function validateNumber(
	processedNumberCharIndexes: number[],
	lineIdx: number,
	data: string[]
) {
	return processedNumberCharIndexes
		.map((x) => [x, lineIdx])
		.some((coordinates) =>
			checkSymbolNerby(coordinates[0], coordinates[1], data)
		)
}

export async function day3a(dataPath?: string) {
	const data = await readData(dataPath)

	let validNumbers = []
	for (let lineIdx = 0; lineIdx < data.length; lineIdx++) {
		const line = data[lineIdx]

		let processedNumberCharIndexes: number[] = []

		for (let charIdx = 0; charIdx <= line.length; charIdx++) {
			const char = getChar(charIdx, lineIdx, data)
			const isCharNumber = /[0-9]/.test(char)

			if (isCharNumber) {
				processedNumberCharIndexes.push(charIdx)
				continue
			}

			if (!processedNumberCharIndexes.length) {
				continue
			}

			const isNumberValid = validateNumber(
				processedNumberCharIndexes,
				lineIdx,
				data
			)

			if (isNumberValid) {
				const number = parseInt(
					processedNumberCharIndexes.map((idx) => line[idx]).join('')
				)
				validNumbers.push(number)
			}

			processedNumberCharIndexes = []
		}
	}

	return sumNumArray(validNumbers)
}

console.time('test')
const answer = await day3a()
console.timeEnd('test')
console.log(chalk.bgGreen('Your Answer:'), chalk.green(answer))
