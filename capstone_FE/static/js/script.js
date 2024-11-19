document.addEventListener('DOMContentLoaded', function () {
    // Base URL for the API
    const apiBaseUrl = 'http://localhost:5000/api';

    // Fetch all quizzes and display them on index.html
    function fetchQuizzes() {
        fetch(`${apiBaseUrl}/quizzes`)
            .then(response => response.json())
            .then(data => {
                const quizList = document.getElementById('quiz-list');
                quizList.innerHTML = ''; // Clear any previous quizzes

                // Loop through quizzes and display each one
                data.forEach(quiz => {
                    const listItem = document.createElement('li');
                    listItem.innerHTML = `<a href="/quiz/${quiz.id}">${quiz.title}</a>`;
                    quizList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error fetching quizzes:', error));
    }

    // Load quiz questions for quiz.html
    function loadQuiz() {
        const quizId = window.location.pathname.split('/').pop(); // Get quiz ID from URL
        fetch(`${apiBaseUrl}/quizzes/${quizId}`)
            .then(response => response.json())
            .then(quizData => {
                const quizTitle = document.getElementById('quiz-title');
                quizTitle.textContent = quizData[0].title; // Set the quiz title

                // Fetch and display questions
                fetch(`${apiBaseUrl}/quizzes/${quizId}/questions`)
                    .then(response => response.json())
                    .then(questions => {
                        const quizForm = document.getElementById('quiz-form');
                        quizForm.innerHTML = ''; // Clear any previous questions

                        questions.forEach(question => {
                            const questionDiv = document.createElement('div');
                            questionDiv.classList.add('question');
                            questionDiv.innerHTML = `
                                <p>${question.question_text}</p>
                                <div class="choices">
                                    ${question.choices.map(choice => `
                                        <label>
                                            <input type="radio" name="question-${question.question_id}" value="${choice.choice_id}">
                                            ${choice.choice_text}
                                        </label>
                                    `).join('')}
                                </div>
                            `;
                            quizForm.appendChild(questionDiv);
                        });
                    })
                    .catch(error => console.error('Error fetching quiz questions:', error));
            })
            .catch(error => console.error('Error loading quiz:', error));
    }

    // Submit quiz answers for scoring
    function submitQuiz() {
        // Get quiz ID from URL
        const quizId = window.location.pathname.split('/').pop(); // Get quiz ID from URL

        // Ensure the quizId is valid
        if (!quizId) {
            console.error("Quiz ID is missing from the URL.");
            return;
        }

        const answers = [];
        const questions = document.querySelectorAll('#quiz-form .question');
        
        // Loop through each question to gather the answers
        questions.forEach((questionDiv, index) => {
            const selectedChoice = questionDiv.querySelector('input[type="radio"]:checked');
            
            if (selectedChoice) {
                answers.push({
                    question_id: index + 1, // Use the question index or ID here
                    choice_id: selectedChoice.value, // Selected choice ID
                });
            }
        });

        // Check if any answers were selected
        if (answers.length === 0) {
            console.error("No answers selected.");
            return;
        }

        // Post the answers to the server and get the score
        fetch(`${apiBaseUrl}/submit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ quiz_id: quizId, answers }) // Include quizId with the answers
        })
        .then(response => response.json())
        .then(data => {
            // Redirect to result page with the score
            window.location.href = `/result.html?score=${data.score}`;
        })
        .catch(error => console.error('Error submitting quiz:', error));
    }

    // Display quiz results on result.html
    function displayResult() {
        const urlParams = new URLSearchParams(window.location.search);
        const score = urlParams.get('score');
        const resultElement = document.getElementById('quiz-result');

        if (score !== null) {
            resultElement.textContent = `Your score: ${score}`;
        } else {
            resultElement.textContent = 'No score available.';
        }
    }

    // Determine which function to call based on the current page
    const path = window.location.pathname;

    if (path === '/' || path === '/index.html') {
        fetchQuizzes(); // Load quizzes for index.html
    } else if (path.includes('/quiz/')) {
        loadQuiz(); // Load quiz data for quiz.html
    } else if (path === '/result.html') {
        displayResult(); // Show result for result.html
    }

    // Attach event listener for the submit button on quiz.html
    const submitButton = document.getElementById('submit-btn');
    if (submitButton) {
        submitButton.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent default form submission
            submitQuiz();
        });
    }
});


