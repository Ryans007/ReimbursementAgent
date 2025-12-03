from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GEMINI_API_KEY')

class ReimbursementAgentOutput(BaseModel):
    answer: str
    confidence: float

reimbursement_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
reimbursement_chain = reimbursement_model.with_structured_output(ReimbursementAgentOutput)