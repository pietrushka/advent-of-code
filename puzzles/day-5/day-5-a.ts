import { readData } from '../../shared.ts'
import chalk from 'chalk'

const numStringToArr = (s: string) => s.split(' ').map(Number)

function getModifiers(data: string[]) {
	const modifiers: number[][][] = []
	for (let line of data.slice(1)) {
		if (line.length === 0) continue
		if (line.includes('map')) {
			modifiers.push([])
			continue
		}
		modifiers[modifiers.length - 1].push(numStringToArr(line))
	}
	return modifiers
}

function runModifier(modifierRules: number[][], inputNumber: number) {
	for (let rule of modifierRules) {
		const [destinationRangeStart, sourceRangeStart, rangeLength] = rule
		const idxDiff = inputNumber - sourceRangeStart
		const isInRange = 0 <= idxDiff && idxDiff <= rangeLength
		if (isInRange) {
			return destinationRangeStart + idxDiff
		}
	}
	return inputNumber
}

function findLowest([firstNum, ...restNums]: number[]) {
	let lowest = firstNum
	for (let num of restNums) {
		if (num < lowest) lowest = num
	}
	return lowest
}

export async function day5a(dataPath?: string) {
	const data = await readData(dataPath)

	const input = numStringToArr(data[0].split(': ')[1])
	const modifiers = getModifiers(data)

	let result = input
	for (let modifierRules of modifiers) {
		result = result.map((x) => runModifier(modifierRules, x))
	}
	return findLowest(result)
}

const answer = await day5a()
console.log(chalk.bgGreen('Your Answer:'), chalk.green(answer))
