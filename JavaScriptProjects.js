// Temperature in Kelvin
const kelvin = 0;

// Temperature in Celsius
const celsius = kelvin - 273;

// Temperature in Fahrenheit
let fahrenheit = celsius * (9/5) + 32;

// Rounded Temperature Decimel Down
fahrenheit = Math.floor(fahrenheit);

console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`);

let newton = Math.floor(celsius * (33/100));

console.log(`The temperature is ${newton} degrees Newton.`)

//---------------------------------------------------------------//

// My Age
const myAge = 30;

// Early Years
let earlyYears = 2;

earlyYears *= 10.5;

// Later Years
let laterYears = myAge - 2;

laterYears *= 4;

console.log(earlyYears);
console.log(laterYears);

// Dog Years
const myAgeInDogYears = earlyYears + laterYears;

// My Name
myName = 'Lawrence'.toLowerCase();

console.log(`My name is ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} years old in dog years.`)

//---------------------------------------------------------------//

let userName = '';

userName ? console.log(`Hello, ${userName}!`) : console.log('Hello!');

const userQuestion = 'Am I going to be rich?';

console.log(`The user asked: ${userQuestion}`);

const randomNumber = Math.floor(Math.random() * 8);

let eightBall = ''

switch (randomNumber){
  case 0:
    eightball = 'It is certain';
    break;
  case 1:
    eightBall = 'It is decidedly so';
    break;
  case 2:
    eightBall = 'Reply hazy try again';
    break;
  case 3:
    eightBall = 'Cannot predict now';
    break;
  case 4:
    eightBall = 'Do not count on it';
    break;
  case 5:
    eightBall = 'My sources say no';
    break;
  case 6:
    eightBall = 'Outlook not so good';
    break;
  case 7:
    eightBall = 'Signs point to yes';
    break;
}

console.log(`The Eight Ball answered: ${eightBall}`)

if (randomNumber === 0) {
    eightBall = 'It is certain';
} else if (randomNumber === 1) {
    eightBall = 'It is decidedly so'
} else if (randomNumber === 2) {
    eightBall = 'Reply hazy try again'
} else if (randomNumber === 3) {
    eightBall = 'Cannot predict now'
} else if (randomNumber === 4) {
    eightBall = 'Do not count on it'
} else if (randomNumber === 5) {
    eightBall = 'My sources say no'
} else if (randomNumber === 6) {
    eightBall = 'Outlook not so good'
} else if (randomNumber === 7) {
    eightBall = 'Signs point to yes'
} else {
    console.log('Error')
}

//--------------------------------------------------------//

let raceNumber = Math.floor(Math.random() * 1000);

const registeredEarly = false;

const runnerAge = 19;

if (runnerAge >= 18 && registeredEarly === true){
  raceNumber += 1000;
};

if (runnerAge >= 18 && registeredEarly === true){
  console.log(`Racer Number ${raceNumber} starts at 9:30 am.`);
} else if (runnerAge >= 18 && registeredEarly === false) {
  console.log(`Racer Number ${raceNumber} starts at 11:00 am.`);
}

if (runnerAge < 18) {
  console.log(`Racer Number ${raceNumber} starts at 12:30 pm.`);
} else {
  console.log('See the Registration Desk');
}

//--------------------------------------------------------------//

const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();
  if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissors') {
    return userInput;
  } else {
    console.log('Error');
  }
};

// console.log(getUserChoice('rock'));

function getComputerChoice(){
  switch (Math.floor(Math.random() * 3)) {
    case 0:
      return 'rock';
    case 1:
      return 'paper';
    case 2:
      return 'scissors';
  }
};

// console.log(getComputerChoice());

function determineWinner(userChoice, computerChoice){
  if (userChoice === 'bomb') {
    return 'User Won'
  }
  if (userChoice === computerChoice) {
    return 'Tie';
  }
  if (userChoice === 'rock') {
    if (computerChoice === 'paper') {
      return 'Computer Won';
    } else {
      return 'User Won';
    }
  }
  if (userChoice === 'paper') {
    if (computerChoice === 'scissors') {
      return 'Computer Won';
    } else {
      return 'User Won';
    }
  }
  if (userChoice === 'scissors') {
    if (computerChoice === 'rock') {
      return 'Computer Won';
    } else {
      return 'User Won';
    }
  }
};

// console.log(determineWinner('paper', 'rock'))

function playGame () {
  const userChoice = getUserChoice('rock');
  const computerChoice = getComputerChoice();
  console.log( 'You threw:' + userChoice);
  console.log('The computer threw:' + computerChoice);
  console.log(determineWinner(userChoice, computerChoice));
};

playGame();

//------------------------------------------------------------//