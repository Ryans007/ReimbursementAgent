from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GEMINI_API_KEY')

revisor_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)