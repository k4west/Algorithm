const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

readline.on('line', function(line) {
    input = line.split(' ').map(el => parseInt(el));
}).on('close', function(){
	const A = parseInt(input[0]);
    const B = parseInt(input[1]);
    console.log(A+B);
    process.exit();
});