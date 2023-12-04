import { readData } from '../../shared.ts'
import chalk from 'chalk'

function sumNumArray(nums: number[]) {
	return nums.reduce((acc, x) => acc + x, 0)
}

const ADJACENT_NUMBERS_REQUIRED = 2

function getChar(x: number, y: number, data: string[]): string | undefined {
	return data?.[y]?.[x]
}

function getAdjacentPositions(x: number, y: number) {
	return [
		[x, y - 1],
		[x + 1, y - 1],
		[x + 1, y],
		[x + 1, y + 1],
		[x, y + 1],
		[x - 1, y + 1],
		[x - 1, y],
		[x - 1, y - 1],
	]
}

function getNumbersCoordinateStrings(data: string[]) {
	let numbersCoordinates: string[][] = []

	for (let lineIdx = 0; lineIdx < data.length; lineIdx++) {
		const line = data[lineIdx]

		let processedNumberCharIndexes: string[] = []

		for (let charIdx = 0; charIdx <= line.length; charIdx++) {
			const char = getChar(charIdx, lineIdx, data)
			const isCharNumber = /[0-9]/.test(char)

			if (isCharNumber) {
				processedNumberCharIndexes.push([charIdx, lineIdx].join(';'))
				continue
			}

			if (!processedNumberCharIndexes.length) {
				continue
			}

			numbersCoordinates.push(processedNumberCharIndexes)

			processedNumberCharIndexes = []
		}
	}

	return numbersCoordinates // eg. [["0;1", 0;2"]]
}

function convertCoordinatesStringsToNumber(
	coordinatesStrings: string[],
	data: string[]
) {
	const numberDigits = coordinatesStrings.map((coords) => {
		const [x, y] = coords.split(';').map(Number)
		return getChar(x, y, data)
	})

	return parseInt(numberDigits.join(''))
}

export async function day3b(dataPath?: string) {
	const data = await readData(dataPath)
	const numbersCoordinates = getNumbersCoordinateStrings(data)

	const ratios = data.flatMap((line, lineIdx) =>
		Array.from(line).flatMap((char, charIdx) => {
			if (char !== '*') return []

			const adjacentCoordinates = getAdjacentPositions(charIdx, lineIdx).map(
				(coords) => coords.join(';')
			)
			const adjacentNumbers = numbersCoordinates.filter((coords) =>
				coords.some((coord) => adjacentCoordinates.includes(coord))
			)

			if (adjacentNumbers.length !== ADJACENT_NUMBERS_REQUIRED) {
				return []
			}

			const ratio =
				convertCoordinatesStringsToNumber(adjacentNumbers[0], data) *
				convertCoordinatesStringsToNumber(adjacentNumbers[1], data)

			return ratio
		})
	)

	return sumNumArray(ratios)
}

const answer = await day3b()
console.log(chalk.bgGreen('Your Answer:'), chalk.green(answer))
