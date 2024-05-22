const sendButton = document.getElementById('send');
const input = document.getElementById('input');
const chat = document.getElementsByClassName('chat')[0];

function createMessage(text){
    const message = document.createElement('div');
    message.classList.add('message');
    message.innerHTML = "<p>" + text + "</p>";
    return message;
}

function createMessageUser(){
    const text = input.value;
    if (text === '') {
        return;
    }
    const message = createMessage(text);
    message.classList.add('user');
    chat.appendChild(message);
    chat.scrollTop = chat.scrollHeight;

    // block the input
    input.value = '';
    input.disabled = true;
    createMessageBot(text);
}

function createMessageBot(userText){
    // loading message
    const waiting = createMessage('...');
    waiting.classList.add('bot');
    chat.appendChild(waiting);
    chat.scrollTop = chat.scrollHeight;

    // Send the request to the API
    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userText })
    })
    .then(response => response.json())
    .then(data => {
        const text = data.answer;

        const message = createMessage(text);
        message.classList.add('bot');
        chat.appendChild(message);
        chat.scrollTop = chat.scrollHeight;

        // unblock the input
        input.disabled = false;
        waiting.remove();
    })
    .catch(error => {
        console.error("Erro ao enviar a requisição:", error);
        input.disabled = false;
        waiting.remove();
    });
}

function clickButton(e) {
    e.preventDefault();
    createMessageUser();
}

// Adiciona um event listener para o botão de enviar
sendButton.addEventListener('click', clickButton);

// Adiciona um event listener para a tecla Enter
input.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        createMessageUser();
    }
});
