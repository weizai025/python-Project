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
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are an ai chef.Create a unique recipe based on following main ingredient"),
        ("human","{input}")
    ]
)

# Create LLM Chain
chain = prompt | llm 

response = chain.invoke({"input":"tomatoes"})

print(response.content)