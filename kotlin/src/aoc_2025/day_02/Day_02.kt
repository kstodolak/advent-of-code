package aoc_2025.day_02

import utils.*

fun main() {
    fun isInvalidId(id: String, chunkSize: Int): Boolean {
        if (id.length % chunkSize != 0) return false

        val chunked = id.chunked(chunkSize)
        return chunked.all { it == chunked[0] }
    }

    fun part1() {
        val invalidIds = mutableListOf<Long>()
//        val input = FileReader.readAndSplitBy("./src/aoc_2025/day_02/example", ",") // EXAMPLE
        val input = FileReader.readAndSplitBy("./src/aoc_2025/day_02/input", ",") // INPUT

        val ranges = input.map {
            val (a, b) = it.split("-").map { numStr -> numStr.toLong() }

            Pair(a, b)
        }

        ranges.forEach { range ->
            val (a, b) = range

            for (i in a..b) {
                val iAsStr = i.toString()
                // Skip numbers with odd length (can't be split into two equal halves)
                if (iAsStr.length % 2 == 0 && isInvalidId(iAsStr, iAsStr.length / 2)) {
                    invalidIds.add(i)
                }
            }
        }

        invalidIds.sum().println()
    }

    fun part2() {
        val invalidIds = mutableListOf<Long>()
//        val input = FileReader.readAndSplitBy("./src/aoc_2025/day_02/example", ",") // EXAMPLE
        val input = FileReader.readAndSplitBy("./src/aoc_2025/day_02/input", ",") // INPUT

        val ranges = input.map {
            val (a, b) = it.split("-").map { numStr -> numStr.toLong() }

            Pair(a, b)
        }

        ranges.forEach { range ->
            val (a, b) = range

            for (i in a..b) {
                val iAsStr = i.toString()
                for (chunkSize in 1..(iAsStr.length / 2)) {
                    if (isInvalidId(iAsStr, chunkSize)) {
                        invalidIds.add(i)
                        break
                    }
                }
            }
        }

        invalidIds.sum().println()
    }

    part1() // 13919717792
    part2() // 14582313461
}