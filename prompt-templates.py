from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Instantiate Model
llm = ChatOpenAI(
    model="gpt-3.5-turbo-1106",
    temperature=0.8,
)

# Prompt Template
prompt = ChatPromptTemplate.from_template('tell me a joke about the {subject}')

# Create LLM Chain
chain = prompt | llm 

response = chain.invoke({"subject":"dog"})

print(response)