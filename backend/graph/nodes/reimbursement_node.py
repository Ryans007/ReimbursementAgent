from ..chains import reimbursement_chain
from ..tools.vector_store_tool import search_in_vectorstore_tool
from ..state import AgentState
from langchain_core.messages import HumanMessage, SystemMessage

REIMBURSEMENT_PROMPT = """Você é um agente interno que auxilia colaboradores a decidirem sobre reembolsos e cancelamentos.
Você ja tem a classificação da mensagem :{label} e a explicação para essa classificação : {explanation}.
Consulte a base de conhecimento:
{vector_store_content}.
Sempre consulte a base de conhecimento antes de responder.
E classifique a confiança da sua resposta com base na relação dela coma base de conhecimento."""

def reimbursement_node(state: AgentState):
    """Fornece uma resposta de reembolso com base na mensagem do usuário, classificação e explicação."""
    search_result = search_in_vectorstore_tool.invoke(state['user_message'])
    response = reimbursement_chain.invoke([
        SystemMessage(content=REIMBURSEMENT_PROMPT.format(
            label=state['label'],
            explanation=state['classification_agent_explaination'],
            vector_store_content=search_result
        )),
        HumanMessage(content=state['user_message'])
    ])
    return {
        'reimbursement_answer': response.answer,
        'confidence': response.confidence
    }