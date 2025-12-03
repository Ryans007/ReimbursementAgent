from typing import TypedDict
from typing_extensions import Annotated
from langchain_core.messages import AnyMessage
import operator

class AgentState(TypedDict):
    label: str
    user_message: str
    reimbursement_answer: str
    classification_agent_explaination: str
    confidence: float
    messages: Annotated[list[AnyMessage], operator.add]
    final_answer: str