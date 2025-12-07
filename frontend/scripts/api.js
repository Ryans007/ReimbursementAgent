const API_BASE_URL = 'http://localhost:8002';

const apiService = {
    async sendMessage(message, thread_id) {
        try {
            const response = await fetch(`${API_BASE_URL}/chat/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user_message: message,
                    thread_id: thread_id
                })
            });

            if (!response.ok) {
                throw new Error(`Erro: ${response.status}`);
            }
            return await response.json()

        } catch (error) {
            console.error('Erro ao enviar mensagem:', error);
            throw error;
        }
    },

    async getHistory(thread_id) {
        try {
            const response = await fetch(`${API_BASE_URL}/chat_history/`);

            if (!response.ok) {
                throw new Error(`Erro: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('Erro ao buscar histórico:', error);
            throw error;
        }
    }
};
