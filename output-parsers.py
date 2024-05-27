from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser,CommaSeparatedListOutputParser,JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel,Field


def call_string_output_parser():
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.8,
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system","tell me a joke about following subject"),
        ("human","{input}"),
    ])

    parser = StrOutputParser()
    chain = prompt | llm | parser

    return  chain.invoke({"input":"dog"})

print(call_string_output_parser())

def call_list_output_parser():
    llm = ChatOpenAI(
    model="gpt-3.5-turbo-1106",
    temperature=0.8,
    )

    # Prompt Template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system","Generate a list of 10 synonyms for the following word.Return the results as a comma separated list"),
            ("human","{input}")
        ]
    )

    # parse
    parser = CommaSeparatedListOutputParser()

    # Create LLM Chain
    chain = prompt | llm | parser

    return chain.invoke({"input":"happy"})

print(call_list_output_parser())

def call_json_output_paser():
    llm = ChatOpenAI(
    model="gpt-3.5-turbo-1106",
    temperature=0.8,
    )

    # Prompt Template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system","Extract infomation from following phrase.\nFormatting Instructions:{format_instructions}"),
            ("human","{phrase}")
        ]
    )

    class Person(BaseModel):
        name:str = Field(description="the name of the person")
        age:int = Field(description="the age of the person")

    # parse
    parser = JsonOutputParser(pydantic_object=Person)
    
    chain = prompt | llm | parser

    return chain.invoke({
        "phrase":"lisi is 20 years old",
        "format_instructions":parser.get_format_instructions()})

print(call_json_output_paser())