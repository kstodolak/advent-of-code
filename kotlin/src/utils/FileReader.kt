package utils

import java.io.File

object FileReader {
    fun readAsLines(path: String): List<String> {
        return File(path).readLines()
    }
}