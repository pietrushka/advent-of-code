// TODO tidy up (stored here to allow testing)

type Range = ReturnType<typeof getRanges>[number]

const numStringToArr = (s: string) => s.split(' ').map(Number)

export function findLowestNumer([firstNum, ...restNums]: number[]) {
	let lowest = firstNum
	for (let num of restNums) {
		if (num < lowest) lowest = num
	}
	return lowest
}

function arrayToTuples<T extends unknown>(
	array: T[],
	result: T[][] = []
): T[][] {
	return array.length < 2
		? result
		: arrayToTuples(array.slice(2), [...result, array.slice(0, 2)])
}

function startSizeToRange([start, length]: number[]) {
	return [start, start + length - 1]
}

export function getRanges(data: string[]) {
	const nums = numStringToArr(data[0].split(': ')[1])
	const numTuples = arrayToTuples(nums)
	return numTuples.map(startSizeToRange)
}

export function getModifiers(data: string[]) {
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

const getDiffStart = ({
	min1,
	max1,
	min2,
	max2,
	isIntersectionInTheMiddle,
}: {
	min1: number
	max1: number
	min2: number
	max2: number
	isIntersectionInTheMiddle: boolean
}) => {
	if (isIntersectionInTheMiddle) {
		return min1
	}

	if (min1 < min2) {
		return min1
	}

	return max2 + 1
}

export function getRangesRelations(range1: Range, range2: Range) {
	let intersection: number[] | undefined
	// range1 - range2
	let differences: number[][] = []
	const [min1, max1] = range1
	const [min2, max2] = range2

	if (min1 === min2 && max1 === max2) {
		intersection = [...range1]
		return { intersection, differences }
	}

	// no intersection => no differences
	if (max1 < min2 || max2 < min1) {
		return { intersection, differences }
	}

	let iMin = min1 < min2 ? min2 : min1
	let iMax = max1 < max2 ? max1 : max2
	intersection = [iMin, iMax]

	// range 2 includes whole range1 => no diff
	if (min2 <= min1 && max2 >= max1) {
		return { intersection, differences }
	}

	const isIntersectionInTheMiddle = min1 < min2 ? max2 < max1 : false
	differences = [
		[getDiffStart({ min1, max1, min2, max2, isIntersectionInTheMiddle })],
	]

	if (!isIntersectionInTheMiddle) {
		const end = min1 < min2 ? min2 - 1 : max1
		differences[0].push(end)
		return { intersection, differences }
	}

	differences[0].push(min2 - 1)
	differences.push([max2 + 1, max1])

	return { intersection, differences }
}

export function runModifier(modifier: number[], range: Range) {
	const [destinationRangeStart, sourceRangeStart, rangeLength] = modifier
	const ruleSourceRange = startSizeToRange([sourceRangeStart, rangeLength])

	const { intersection, differences } = getRangesRelations(
		range,
		ruleSourceRange
	)
	const sourceDestinationStartDiff = destinationRangeStart - sourceRangeStart

	if (!intersection) {
		return {}
	}

	const rangePartModified = [
		intersection[0] + sourceDestinationStartDiff,
		intersection[1] + sourceDestinationStartDiff,
	]

	return { main: rangePartModified, differences }
}
