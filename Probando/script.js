const sendButton = document.getElementById('send-button');
const messageInput = document.getElementById('message-input');
const chatBox = document.getElementById('chat-box');

sendButton.addEventListener('click', function () {
    const userMessage = messageInput.value.trim();

    if (userMessage !== "") {
        // Añadir mensaje de usuario con animación
        addMessage(userMessage, 'user');
        messageInput.value = ""; // Limpiar el campo de entrada

        // Animar la respuesta del amigo ficticio
        setTimeout(() => {
            addFriendTyping(); // Mostrar que el amigo está escribiendo

            setTimeout(() => {
                if (userMessage.toLowerCase() === 'hola') {
                    addMessage("¡Hola! ¿Cómo estás?", 'friend');
                }
            }, 1500); // Tiempo de respuesta del amigo ficticio
        }, 1000);
    }
});

// Función para añadir los mensajes al chat con animación
function addMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');

    if (sender === 'user') {
        messageDiv.classList.add('user-message');
        messageDiv.textContent = `Tú: ${message}`;
    } else if (sender === 'friend') {
        messageDiv.classList.add('friend-message');
        messageDiv.textContent = `Amigo: ${message}`;
    }

    // Añadir animación de aparición
    messageDiv.style.opacity = 0; // Empieza invisible
    chatBox.appendChild(messageDiv);

    // Animación para hacer aparecer el mensaje
    setTimeout(() => {
        messageDiv.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        messageDiv.style.opacity = 1;
        messageDiv.style.transform = 'translateY(0)';
    }, 50); // Se aplica después de un pequeño retraso
    chatBox.scrollTop = chatBox.scrollHeight; // Desplazar el chat hacia abajo
}

// Función para simular que el amigo está escribiendo
function addFriendTyping() {
    const typingMessage = document.createElement('div');
    typingMessage.classList.add('message');
    typingMessage.classList.add('friend-message');
    typingMessage.textContent = 'Amigo está escribiendo...';
    typingMessage.style.fontStyle = 'italic';
    typingMessage.style.opacity = 0;
    typingMessage.style.transform = 'translateY(20px)';
    chatBox.appendChild(typingMessage);

    // Animación de "escribiendo"
    setTimeout(() => {
        typingMessage.style.transition = 'opacity 1s ease-out, transform 1s ease-out';
        typingMessage.style.opacity = 1;
        typingMessage.style.transform = 'translateY(0)';
    }, 50); // Aparece con una animación

    // Desaparece después de un tiempo
    setTimeout(() => {
        typingMessage.style.transition = 'opacity 0.6s ease-out';
        typingMessage.style.opacity = 0;
    }, 1500); // El mensaje de "escribiendo..." se va después de 1.5 segundos
}
