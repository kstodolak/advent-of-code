package aoc_2025.day_03

import utils.FileReader
import utils.println

fun solve(lines: List<String>, maxBatteries: Int): Long {
    var result: Long = 0

    lines.forEach { line ->
        val maxes = MutableList(maxBatteries) { 0 }

        for (i in 0..<line.length) {
            val battery = line[i].digitToInt()

            for (maxIndex in 0..<maxes.size) {
                val max = maxes[maxIndex]
                if (battery > max && (maxBatteries + i) - maxIndex <= line.length) {
                    maxes[maxIndex] = battery
                    for (ii in maxIndex + 1..<maxes.size) maxes[ii] = 0
                    break
                }
            }
        }

        result += maxes.joinToString("").toLong()
    }

    return result
}

fun part1(input: List<String>) {
    solve(input, 2).println()
}

fun part2(input: List<String>) {
    solve(input, 12).println()
}


fun main() {
//    val input = FileReader.readAsLines("src/aoc_2025/day_03/example")
    val input = FileReader.readAsLines("src/aoc_2025/day_03/input")

    part1(input)
    part2(input)
}