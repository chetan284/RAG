import os
import sys

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language

DIRECTORRY_PATH = "/Users/Chetan/PycharmProjects/BmccRagDemo/Data"

# -------------------------------------------------------------------------------------------------------------

print("-----LOADING------")
text_loader_kwargs={'autodetect_encoding': True}
directoryLoader = DirectoryLoader(DIRECTORRY_PATH, glob="./*.md", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
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
from langchain_community.embeddings import GPT4AllEmbeddings

gpt4all_embd = GPT4AllEmbeddings()

db = Chroma.from_documents(chunks, gpt4all_embd)
retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 8},
)

from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
# -------------------------------------------------------------------------------------------------------------

print("-----CHAT BOT------")
from langchain_community.chat_models.ollama import ChatOllama
llm = ChatOllama(model="mistral")

system_template = """
Answer the user's questions based on the below context.
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use three sentences maximum and keep the answer as concise as possible:

{context}
"""

# First we need a prompt that we can pass into an LLM to generate this search query
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{input}"),
    ]
)
document_chain = create_stuff_documents_chain(llm, prompt)
qa_chain = create_retrieval_chain(retriever, document_chain)
qa_chain.pick("answer").invoke({"input": "who is Chetan?"})



