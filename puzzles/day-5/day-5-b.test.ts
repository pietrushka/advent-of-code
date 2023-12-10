import { runModifier } from './day-5-b-utils.ts'

describe('day-5-b', () => {
	test('rule includes whole range', () => {
		const rule = [52, 50, 48]
		const range = [79, 92]
		const { main, differences } = runModifier(rule, range)
		expect(main).toEqual([81, 94])
		expect(differences).toEqual([])
	})
	test('intersection at range beginning end', () => {
		const rule = [56, 93, 4]
		const range = [85, 95]
		const { main, differences } = runModifier(rule, range)
		expect(main).toEqual([56, 58])
		expect(differences).toEqual([[85, 92]])
	})
	test('intersection at range beginning', () => {
		const rule = [49, 53, 8]
		const range = [57, 69]
		const { main, differences } = runModifier(rule, range)
		expect(main).toEqual([53, 56])
		expect(differences).toEqual([[61, 69]])
	})
})
