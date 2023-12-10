import { readData } from '../../shared.ts'
import chalk from 'chalk'
import {
	getRanges,
	getModifiers,
	runModifier,
	findLowestNumer,
} from './day-5-b-utils.ts'

export async function day5b(dataPath?: string) {
	const data = await readData(dataPath)

	let ranges = getRanges(data)
	const modifiers = getModifiers(data)

	for (let [modifierIdx, modifierRules] of modifiers.entries()) {
		let toProcess = [...ranges]
		let processed = []
		// seed-to-soil
		for (let rule of modifierRules) {
			// eg. 88 18 7
			let i = 0

			while (i < toProcess.length) {
				const range = toProcess[i]

				if (!range) {
					i++
					continue
				}

				const { main, differences } = runModifier(rule, range)

				//update
				if (main) {
					processed.push(main)
					toProcess = [
						...toProcess.slice(0, i),
						null,
						...toProcess.slice(i + 1),
						...differences,
					]
				}
				i++
			}
		}

		ranges = [...processed, ...toProcess.filter((x) => x)]
	}

	const numbers = ranges.map(([startNum]) => startNum).flat()

	return findLowestNumer(numbers)
}

const answer = await day5b()
console.log(chalk.bgGreen('Your Answer:'), chalk.green(answer))
