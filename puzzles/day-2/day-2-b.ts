import { readData } from '../../shared.ts'
import chalk from 'chalk'
import { parseGameSets, sumNumArray, Set } from './common.ts'

function getMaxColorCubeCount(sets: Set[], color: string) {
	return (
		Math.max(...sets.filter((x) => x.color === color).map((x) => x.num)) || 1
	)
}

function getGameCubeCountPower(sets: Set[]) {
	const maxRed = getMaxColorCubeCount(sets, 'red')
	const maxGreen = getMaxColorCubeCount(sets, 'green')
	const maxBlue = getMaxColorCubeCount(sets, 'blue')
	return maxRed * maxGreen * maxBlue
}

export async function day2b(dataPath?: string) {
	const data = await readData(dataPath)
	const allSetsStrings = data.map((line: string) => line.split(': ')[1])
	const setsByGames = allSetsStrings.map(parseGameSets)
	const gamesPowers = setsByGames.map(getGameCubeCountPower)

	return sumNumArray(gamesPowers)
}

const answer = await day2b()
console.log(chalk.bgGreen('Your Answer:'), chalk.green(answer))
