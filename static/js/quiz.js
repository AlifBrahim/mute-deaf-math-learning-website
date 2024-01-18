const quizData = [
    {
        question: 'What is the capital of France?',
        options: ['Paris', 'London', 'Berlin', 'Madrid'],
        answer: 'Paris',
    },
    // Add more questions as needed
];

const quizContainer = document.getElementById('quiz');
const resultContainer = document.getElementById('result');
const submitButton = document.getElementById('submit');
const retryButton = document.getElementById('retry');
const showAnswerButton = document.getElementById('showAnswer');

let currentQuestion = 0;
let score = 0;
let incorrectAnswers = [];

function displayQuestion() {
    const questionData = quizData[currentQuestion];
    const optionsHtml = questionData.options.map((option, index) => {
        return `<label class="option">
                    <input type="radio" name="quiz" value="${option}" /> ${option}
                </label>`;
    }).join('');
    quizContainer.innerHTML = `<div class="question">${questionData.question}</div>
                               <div class="options">${optionsHtml}</div>`;
}

function checkAnswer() {
    const selectedOption = document.querySelector('input[name="quiz"]:checked');
    if (selectedOption) {
        const answer = selectedOption.value;
        if (answer === quizData[currentQuestion].answer) {
            score++;
        } else {
            incorrectAnswers.push(currentQuestion);
        }
        currentQuestion++;
        if (currentQuestion < quizData.length) {
            displayQuestion();
        } else {
            displayResult();
        }
    }
}

function displayResult() {
    quizContainer.style.display = 'none';
    submitButton.style.display = 'none';
    retryButton.style.display = 'inline-block';
    showAnswerButton.style.display = 'inline-block';
    resultContainer.innerHTML = `You scored ${score} out of ${quizData.length}!`;
}

function showAnswer() {
    const questionData = quizData[currentQuestion - 1]; // Get the last question
    const options = document.querySelectorAll('.option');
    options.forEach((option) => {
        if (option.textContent.trim() === questionData.answer) {
            // Highlight the correct answer with green
            option.style.backgroundColor = '#0f0';
        }
    });
}

submitButton.addEventListener('click', checkAnswer);
retryButton.addEventListener('click', function() {
    // Reset the quiz to the first question
    currentQuestion = 0;
    score = 0;
    incorrectAnswers = [];
    displayQuestion();
    quizContainer.style.display = '';
    submitButton.style.display = 'inline-block';
    retryButton.style.display = 'none';
    showAnswerButton.style.display = 'none';
    resultContainer.innerHTML = '';
});
showAnswerButton.addEventListener('click', showAnswer);

displayQuestion();
