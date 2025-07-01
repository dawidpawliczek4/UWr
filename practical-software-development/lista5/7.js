const fs = require('fs');
const util = require('util');

fs.readFile('example.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file with callback:', err);
    } else {
        console.log('Data read with callback:', data);
    }
});


// 1
function readFileWithPromise(filePath, encoding) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, encoding, (err, data) => {
            if (err) {
                reject(err);
            } else {
                resolve(data);
            }
        });
    });
}

readFileWithPromise('example.txt', 'utf8')
    .then(data => console.log('Data read with manual Promise:', data))
    .catch(err => console.error('Error reading file with manual Promise:', err));


// 2
const readFilePromisified = util.promisify(fs.readFile);

readFilePromisified('example.txt', 'utf8')
    .then(data => console.log('Data read with util.promisify:', data))
    .catch(err => console.error('Error reading file with util.promisify:', err));



// 3
const { promises: fsPromises } = fs;

fsPromises.readFile('example.txt', 'utf8')
    .then(data => console.log('Data read with fs.promises:', data))
    .catch(err => console.error('Error reading file with fs.promises:', err));

(async () => {
    try {
        const dataManual = await readFileWithPromise('example.txt', 'utf8');
        console.log('Data read with manual Promise (async/await):', dataManual);

        const dataPromisified = await readFilePromisified('example.txt', 'utf8');
        console.log('Data read with util.promisify (async/await):', dataPromisified);

        const dataFsPromises = await fsPromises.readFile('example.txt', 'utf8');
        console.log('Data read with fs.promises (async/await):', dataFsPromises);
    } catch (err) {
        console.error('Error reading file with async/await:', err);
    }
})();
