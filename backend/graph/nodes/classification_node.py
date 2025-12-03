from ..chains import classification_chain
from langchain_core.messages import HumanMessage, SystemMessage
from ..state import AgentState

# Prompt do agente de classificação
CLASSIFICATION_PROMPT = """Você é um classificador de mensagens. Classifique a mensagem do usuário em uma das categorias fornecidas.
Categorias possíveis: Reembolso, Cancelamento, Financeiro, Exceções, Suporte, Entrega, Pedido, Fraude
Explaination: Explique o porque tomou essa decisão"""

def classification_node(state: AgentState):
    """Classifica a mensagem do usuário em uma das categorias fornecidas."""
    response = classification_chain.invoke([
        SystemMessage(content=CLASSIFICATION_PROMPT),
        HumanMessage(content=state['user_message'])
    ])
    return {
        'label': response.label,
        'classification_agent_explaination': response.explaination
    }