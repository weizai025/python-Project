from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv() 

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.8,
)

# invoke batch stream
response = llm.stream('where is China?')

# not stream
# print(response)

# stream
for chunk in response:
    print(chunk.content,end='',flush=True)