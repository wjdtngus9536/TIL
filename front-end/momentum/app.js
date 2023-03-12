// console.log('hello world'); // 콘솔에 출력 

// const a = 5;
// const b = 2;
// let myName = "soohyun";

// // 과거의 jsdpsms const와 let대신 var만 사용했다.
// // var은 어디에서나 변경이 가능해서 언어를 통한 보호를 받을 수 없었다.


// console.log(a  , b);
// console.log(a * b);
// console.log(a / b);
// console.log("hello "  , myName);

// /*
// const 자료형을 바꾸려 한 경우
// Uncaught TypeError: Assignment to constant variable.
// at app.js:14:8
// */

// myName = 'jeong';
// console.log('your new name is '  , myName);



/***************************** 
* 2.4 boolean
*****************************/
// const amIFat = null;
// let something; // 변수는 메모리상에 존재하나 값이 주어지지 않은 undifined 상태(값이 할당(초기화)되지 않은 변수)
// console.log(something);


/***************************** 
* 2.5 
*****************************/
// const daysOfWeek = ["mon", "tue", "wed", "thu", "fri", "sat"];
// const nonsense = [1, 2, 'hello', false, null, true, undefined, 'nico']

// // Get Item from Array
// console.log(daysOfWeek) // -1 인덱스는 사용할 수 없음

// // Add one more day to the array
// daysOfWeek.push("sun")
// console.log(daysOfWeek)

// const toBuy = ['potato', 'tomato'];
// toBuy.push('kimbab');

/***************************** 
* 2.6 Objects
*****************************/
// const player = { 
//   name: 'nico',
//   points: 10,
//   fat: true,
//   handsome: true
// };

// console.log(player);
// player.lastName = 'potato';
// console.log(player);


/***************************** 
* 2.7 Functions part 1 & 2
*****************************/
// function sayHello(nameOfPerson, age){
//   console.log('hello my name is ' + nameOfPerson + "and I'm " + age);
// }

// function plus(a, b) {
//   console.log(a + b); // plus(); >> NaN
// }

// plus(8, 60);

// sayHello("soohyun", 10);
// sayHello("hanawo", 23);
// sayHello("nico", 10);

// const player = {
//   name: 'nico',
//   sayHello: function(otherPersonsName){
//     console.log('hello ' + otherPersonsName + ' nice to meet you!');
//     // console.log(self.name); 왜 자기 참초는 안될까?
//   },
// };

// player.sayHello('nico');
// player.sayHello('hanawo');



// 같은 단어 선택 & 동시 수정 : ctrl + shit + L
// 같은 단어 하나씩 추가 선택 : ctrl + D
// 코드 자동 정렬(Code Formatting , Prettier) : Shit + Alt + F


/********************
 * Recap 2.9 & 10
 ********************/
// const calculator = {
//   add: function (a, b) {
//     console.log(a + b);
//   },

//   minus: function (a, b) {
//     console.log(a - b);
//   },

//   div: function (a, b) {
//     console.log(a / b);
//   },

//   power: function (a, b) {
//     console.log(a ** b);
//   },
// };

// const a = 4;
// const b = 2;
// calculator.add(a, b);
// calculator.minus(a, b);
// calculator.div(a, b);
// calculator.power(a, b);


/***************************** 
* 2.11 ~ 12 Returns & Recap
*****************************/
// const age = 25;
// function calculateKrAge(ageOfForeigner) {
//   return ageOfForeigner + 2;
// }

// const krAge = calculateKrAge(age);

// console.log(krAge);


/***************************** 
* 2.13 conditionals
*****************************/
// const age = parseInt(prompt('how old are you?')); 
// javascript를 정지시키고 있음
// prompt를 더 이상 사용하지 않는 이유
// message ui가 안예쁘고, css도 적용하지 못함, 어떤 브라우저는 이런 팝업을 제한하기도 하고 오래된 방법

// console.log(typeof age);

/***************************** 
* 2.14 conditionals part 2
*****************************/
// const age = parseInt(prompt('how old are you?')); 

// if(isNaN(age)){ // condition은 boolean으로 판단돼야함
//   console.log("plese write a number");
// } else {
//   console.log('thank you for writing your age');
// }

/***************************** 
* 2.15 conditionals part 3
*****************************/
// const age = parseInt(prompt('how old are you?'));

// if (isNaN(age)) { // condition은 boolean으로 판단돼야함
//   console.log("plese write a number");
// }
// else if (age < 18) {
//   console.log('you are too young.')
// }
// else if (age >= 18 && age <= 50) { // &&의 역할, 둘 다 true여야 한다. 논리연산자
//   console.log('you can drink')
// }
// else {
//   console.log("you should exercise");
// }

/***************************** 
* 2.16 Recap
*****************************/
// const age = parseInt(prompt('how old are you?'));

// if (isNaN(age)) { // condition은 boolean으로 판단돼야함
//   console.log("plese write a number");
// }
// else if (age < 18) {
//   console.log('you are too young.')
// }
// else if (age >= 18 && age <= 50) { // &&의 역할, 둘 다 true여야 한다. 논리연산자
//   console.log('you can drink')
// }
// else if (age > 50 && age <= 80) {
//   console.log("you should exercise");
// }
// else if (age === 100) {
//   console.log('wow you are wise');
// }
// else if (age > 80) { // boundary, 80초과 중 100 제외 모든 나이
//   console.log('you can do whatever you want.');
// }

/***************************** 
* 3.01 HTML in Javascript
*****************************/

const title = document.getElementById("title");
title.innerText = "Got you!";
console.log(title.id);
console.log(title.className);
