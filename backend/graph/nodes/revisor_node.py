from langchain_core.messages import HumanMessage, SystemMessage
from ..state import AgentState
from ..chains import revisor_model

REVISOR_PROMPT = """Você é um revisor que avalia respostas geradas por outros agentes.
Avalie a confiança de acordo com a confiança da resposta, se a confiança for inferior a 70%.
sugira validação manual ou abertura de ticket interno, caso a confiança for superior a 70% devolva a resposta do Reimbursement Agent."""

def revisor_node(state: AgentState):
    """Revisa a resposta de reembolso com base na confiança fornecida."""
    messages = [
        SystemMessage(content=REVISOR_PROMPT),
        HumanMessage(content=f"Resposta: {state['reimbursement_answer']}\nConfiança: {state['confidence']}")
    ]
    response = revisor_model.invoke(messages)
    return {
        'final_answer': response.content
    }