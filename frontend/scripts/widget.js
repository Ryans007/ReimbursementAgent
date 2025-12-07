class ChatWidget {
    constructor() {
        this.thread_id = null;
        this.isOpen = false;
        this.init();
    }

    init() {
        const widget = document.getElementById('chat-widget');

        const chatButton = document.createElement('button');
        chatButton.className = 'chat-button';
        chatButton.innerHTML = '💬';
        chatButton.onclick = () => this.toggleChat();

        const chatWindow = document.createElement('div');
        chatWindow.className = 'chat-window';
        chatWindow.style.display = 'none';
        chatWindow.innerHTML = `
            <div class="chat-header">
                <h2>Agente de Reembolso</h2>
                <button class="close-btn" onclick="chatWidget.toggleChat()">✕</button>
            </div>
            <div class="chat-messages" id="chat-messages"></div>
            <div class="chat-input-area">
                <input
                    type="text"
                    class="chat-input"
                    id="chat-input"
                    placeholder="Digite sua mensagem..."
                    onkeypress="if(event.key==='Enter') chatWidget.sendMessage();"
                >
                <button class="send-btn" onclick="chatWidget.sendMessage();">➤</button>
            </div>
        `;

        widget.appendChild(chatButton);
        widget.appendChild(chatWindow);

        this.chatButton = chatButton;
        this.chatWindow = chatWindow;
        this.messagesContainer = document.getElementById('chat-messages');
        this.inputField = document.getElementById('chat-input');

        this.addMessage('Olá! Eu sou seu agente de reembolso. Como posso ajudá-lo?', 'bot');
    }

    toggleChat() {
        this.isOpen = !this.isOpen;
        this.chatWindow.style.display = this.isOpen ? 'flex' : 'none';

        if (this.isOpen) {
            setTimeout(() => this.inputField.focus(), 100);
        }
    }

    addMessage(content, sender = 'user') {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;

        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.textContent = content;

        messageDiv.appendChild(contentDiv);
        this.messagesContainer.appendChild(messageDiv);

        this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
    }

    async sendMessage() {
        const message = this.inputField.value.trim();

        if (!message) return;

        this.addMessage(message, 'user');
        this.inputField.value = '';

        try {
            this.addMessage('...', 'bot');

            const response = await apiService.sendMessage(message, this.thread_id);

            const lastMessage = this.messagesContainer.lastChild;
            lastMessage.remove();

            if (response.thread_id) {
                this.thread_id = response.thread_id;
            }

            if (response.ai_message) {
                this.addMessage(response.ai_message, 'bot');
            } else {
                this.addMessage('Desculpe, houve um erro na comunicação.', 'bot');
            }
        } catch (error) {
            const lastMessage = this.messagesContainer.lastChild;
            lastMessage.remove();

            this.addMessage('Erro ao conectar com o servidor. Tente novamente.', 'bot');
        }
    }
}

let chatWidget;
document.addEventListener('DOMContentLoaded', () => {
    chatWidget = new ChatWidget();
});
