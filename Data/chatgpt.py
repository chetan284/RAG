import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#
import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

vectorimport os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

import os
import sys
import tiktoken
import export
# import langchain_openai

# from langchain_community.embeddings import OpenAIEmbeddings
from langchain.embeddings import OpenAIEmbeddings


import apikey
import openai


# from langchain_community.indexes import
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = apikey.OPENAI_KEY



query = sys.argv[1]

print(query)

loader = TextLoader("Data/input.md")
# index = VectorstoreIndexCreator().from_loaders([loader])
#
# print(index.query(query))



# embeddings_model = OpenAIEmbeddings(apikey.OPENAI_KEY)
embeddings_model = OpenAIEmbeddings()
vector = embeddings_model.embed_query("apple")

print(vector)

# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# len(embeddings), len(embeddings[0])
#
# embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
# print(embedded_query[:5])
#

