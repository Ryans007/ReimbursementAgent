from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GEMINI_API_KEY')

class ClassificationResult(BaseModel):
    label: str
    explaination: str

classification_model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.5)
classification_chain = classification_model.with_structured_output(ClassificationResult)
