export type Set = ReturnType<typeof parseGameSets>[number]

export function parseGameSets(setsString: string) {
	return setsString
		.split('; ')
		.flatMap((x: string) => x.split(', '))
		.map((x) => {
			const [num, color] = x.split(' ')
			return { color, num: parseInt(num) }
		})
}

export function sumNumArray(nums: number[]) {
	return nums.reduce((acc, x) => acc + x, 0)
}
