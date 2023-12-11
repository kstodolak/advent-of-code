(require('../utils/arrayUtils'))();
const fs = require('fs');
const path = require('path');

const MAX_SIZE = 100000;
const MAX_DISK_SPACE = 70000000;
const MIN_SPACE_LEFT = 30000000;
function parseCommands(commands) {
    const fileSystem = {
        size: 0,
        name: "/",
        type: "dir",
        children: [],
        parent: null,
    }


    let actualDirectory = fileSystem;
    commands.forEach(command => {
        if (command[0] === "$") {
            if (command[1] == "cd") {
                if (command[2] == "/") {
                    actualDirectory = fileSystem
                    return;
                }

                if (command[2] == "..") {
                    actualDirectory = actualDirectory.parent
                    return;
                }

                actualDirectory = actualDirectory.children.find(child => child.name === command[2]);
                return
            }

            if (command[1] == 'ls') {

            }
            return;
        }

        if (command[0] === "dir") {
            actualDirectory.children.push({
                name: command[1],
                type: "dir",
                size: 0,
                children: [],
                parent: actualDirectory
            });
            return;
        }
        const size = Number(command[0])
        actualDirectory.children.push({
            name: command[1],
            type: "file",
            size,
            children: [],
            parent: actualDirectory
        });

        updateSize(actualDirectory, size);
    });

    return fileSystem;
}

function updateSize(actualDirectory, size) {
    actualDirectory.size += size;
    if (actualDirectory.parent != null) {
        return updateSize(actualDirectory.parent, size)
    }
}

function getInnerSize(dir) {
    let size = 0;
    for (let i = 0; i < dir.children.length; i++) {
        if (dir.children[i].type === 'file') continue;
        const el = dir.children[i];

        if (el.size <= MAX_SIZE) {
            size += el.size
        }
        size += getInnerSize(el);
    }

    return size
}

function getDirsToRemove(dir, toRemove, potentials = []) {
    for (let i = 0; i < dir.children.length; i++) {
        if (dir.children[i].type === 'file') continue;
        const el = dir.children[i];

        if (el.size < toRemove) continue
        if (el.size === toRemove) return el;
        else {
            potentials.push(el);
            getInnerSize2(el, toRemove, potentials);
        }
    }

    return potentials;
}

fs.readFile(path.resolve(__dirname, './input.txt'), 'utf8', (err, data) => {
    if (err) {
        console.error(err)
        return;
    }

    const commands = data.trim().split('\n').map(el => el.split(' '));
    const fileSystem = parseCommands(commands);

    // part 1
    console.log(getInnerSize(fileSystem));

    // part 2
    const neededToRemove = (MAX_DISK_SPACE - fileSystem.size - MIN_SPACE_LEFT) * -1;
    const result2 = getDirsToRemove(fileSystem, neededToRemove)
    console.log(result2.map(el => el.size).sortAsc()[0])
});
