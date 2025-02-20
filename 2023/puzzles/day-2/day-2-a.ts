import { readData } from '../../shared.ts'
import chalk from 'chalk'
import { parseGameSets, sumNumArray, Set } from './common.ts'

const MAX_RED = 12
const MAX_GREEN = 13
const MAX_BLUE = 14

function parseGames(data: string[]) {
	return data.map((line: string) => {
		const [gameIdString, setsString] = line.split(': ')

		const gameId = parseInt(gameIdString.split(' ')[1])
		const sets = parseGameSets(setsString)

		return {
			gameId,
			sets,
		}
	})
}

function findImposibleSet(sets: Set[]) {
	return sets.find((x) => {
		switch (x.color) {
			case 'red':
				return x.num > MAX_RED
			case 'green':
				return x.num > MAX_GREEN
			case 'blue':
				return x.num > MAX_BLUE
		}
		return false
	})
}

export async function day2a(dataPath?: string) {
	const data = await readData(dataPath)

	const games = parseGames(data)

	const possibleGames = []
	for (let { gameId, sets } of games) {
		const isAnyImpossible = !!findImposibleSet(sets)
		if (!isAnyImpossible) {
			possibleGames.push(gameId)
		}
	}

	return sumNumArray(possibleGames)
}

const answer = await day2a()
console.log(chalk.bgGreen('Your Answer:'), chalk.green(answer))
