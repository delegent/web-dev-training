console.log("Hello ")


// let Fname = prompt('Enter you name: ')
// let Sname = prompt('Enter Partners Name');
// console.log(Fname,Sname);

let yName = document.getElementById('y-name');
let pName = document.getElementById('p-name');
let button = document.getElementById('btn');
let ans = document.getElementById('ans');
button.addEventListener('click',function(){
	let no =  Math.floor(Math.random() * 100) + 1;
	
	ans.innerHTML = `<h1>${yName.value} and ${pName.value} your love % is ${no}</h1>`
})
console.log(yName);












// console.log(no);

//  
 




















