package utils

import java.io.File

object FileReader {
    fun readAsLines(path: String): List<String> {
        return File(path).readLines()
    }

    fun readAndSplitBy(path: String, delimiter: String): List<String> {
        return File(path).readText().trim().split(delimiter)
    }
}