package aoc_2025.day_01

import utils.*
import kotlin.math.abs

fun main() {
    fun part1() {
        var currentPosition = 50
        var result = 0
        val lines = FileReader.readAsLines("./src/aoc_2025/day_01/input") // INPUT
//        val lines = FileReader.readAsLines("./src/aoc_2025/day_01/example") // EXAMPLE

        lines.forEach { line ->
            val direction = line[0]
            val move = line.substring(1).toInt()
            val moveDelta =  if (direction == 'R') move else -move
            val newPosition = currentPosition + moveDelta

            currentPosition = ((newPosition % 100) + 100) % 100
            if (currentPosition == 0) {
                result += 1
            }
        }

        result.println()
    }

    fun part2() {
        var currentPosition = 50
        var result = 0
        val lines = FileReader.readAsLines("./src/aoc_2025/day_01/input") // INPUT
//        val lines = FileReader.readAsLines("./src/aoc_2025/day_01/example") // EXAMPLE

        lines.forEach { line ->
            val direction = line[0]
            val move = line.substring(1).toInt()
            val moveDelta = if (direction == 'R') move else -move
            val newPosition = currentPosition + moveDelta

            val potentiallyCrossedZero = abs(newPosition) / 100
            if (moveDelta > 0 || currentPosition == 0) {
                result += potentiallyCrossedZero
            } else if (newPosition <= 0) {
                result += 1 + potentiallyCrossedZero
            }

            currentPosition = ((newPosition % 100) + 100) % 100
        }

        result.println()
    }

    part1()
    part2()
}