import os
import sys

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language

DIRECTORY_PATH = "/Users/Chetan/PycharmProjects/RAG/Data"
os.environ["OPENAI_API_KEY"] = constants.APIKEY

# -------------------------------------------------------------------------------------------------------------

print("-----LOADING------")
text_loader_kwargs={'autodetect_encoding': True}
directoryLoader = DirectoryLoader(DIRECTORY_PATH, glob="./*.md", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
directoryDocument = directoryLoader.load()

# -------------------------------------------------------------------------------------------------------------

print("-----SPITING------")
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,
    length_function=len,
    add_start_index=True,
)
chunks = text_splitter.split_documents(directoryDocument)
print(f"Split {len(directoryDocument)} documents into {len(chunks)} chunks.")

# -------------------------------------------------------------------------------------------------------------
print("-----CHROMA DB------")
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

openAi_embd = OpenAIEmbeddings(disallowed_special=())

db = Chroma.from_documents(chunks, openAi_embd)
retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 8},
)

# -------------------------------------------------------------------------------------------------------------

from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo")

# First we need a prompt that we can pass into an LLM to generate this search query

prompt = ChatPromptTemplate.from_messages(
    [
        ("placeholder", "{chat_history}"),
        ("user", "{input}"),
        (
            "user",
            "Given the above conversation, generate a search query to look up to get information relevant to the conversation",
        ),
    ]
)

retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer the user's questions based on the below context:\n\n{context}",
        ),
        ("placeholder", "{chat_history}"),
        ("user", "{input}"),
    ]
)
document_chain = create_stuff_documents_chain(llm, prompt)

qa = create_retrieval_chain(retriever_chain, document_chain)
question = "Who is Chetan?"
result = qa.invoke({"input": question})
result["answer"]

