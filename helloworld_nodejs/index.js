const https = require('http');
const PORT = 8000;
https.createServer((req,res) => {
    res.write('Hello World NodeJS!');
    res.end();
}).listen(PORT, () => {
    console.log("server start at port " + PORT);
})

// const options = {
//     hostname: 'localhost',
//     port: 8000,
//     path: '/',
//     method: 'GET'
// };
// const req = https.request(options, res => {
//     console.log(`statusCode: ${res.statusCode}`);
//     res.on('data', d => {
//         process.stdout.write(d)
//     })
// })
// req.on('error', error => {
//     console.error(error)
// })

// req.end();
