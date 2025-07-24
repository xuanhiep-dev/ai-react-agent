# RAG Chatbot Tutorial

This file show the way to create a RAG Chatbot

### 1. Install some libraries

```
!pip install -q transformers==4.41.2
!pip install -q bitsandbytes==0.43.1
!pip install -q accelerate==0.31.0
!pip install -q langchain==0.2.5
!pip install -q langchainhub==0.1.20
!pip install -q langchain-chroma==0.1.1
!pip install -q langchain-community==0.2.5
!pip install -q langchain-openai==0.1.9
!pip install -q langchain_huggingface==0.0.3
!pip install -q chainlit==1.1.304
!pip install -q python-dotenv==1.0.1
!pip install -q pypdf==4.2.0
!npm install -g localtunnel
!pip install -q numpy==1.24.4
!pip install -q pyngrok
```

### 2. Import the libraries

```
import chainlit as cl
import torch

from chainlit.types import AskFileResponse

from transformers import BitsAndBytesConfig
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface.llms import HuggingFacePipeline

from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.chains import ConversationalRetrievalChain

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
```

### 3. Create text splitter and instance vectorization

```
# Create text splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)

# Create instance vectorization
embedding = HuggingFaceEmbeddings()
```

### 4. Input processing

```
# Call process_file function for input processing
* Input: a message from user
* Output: Relevant docs 
```
### 5. Chroma database

```
# Call get_vector_db function for Chroma database
* Input: Your documents 
* Output: Chroma database 
```
### 6. Create Large Model

```
# Create Large Model using get_huggingface_llm function: (LLM = get_huggingface_llm())
```

### 7. Create welcome message

```
welcome_message = """Welcome to the PDF QA! To get started:
1. Upload a PDF or text file
2. Ask a question about the file
"""
```

### 8. Create on_chat_start function

```
# on_chat_start function is called when the chat starts: async def on_chat_start()
"""
```

### 9. Create on_message function

```
# on_message function is called when the user send the message: async def on_message()
"""
```

### 10. Create file file_name.py for demo

```
%%writefile file_name.py
"""
```

### 11. Deploy chatbot demo using ngrok

```
from pyngrok import ngrok
!ngrok config add-authtoken <your_authen>

url = ngrok.connect(port).public_url
print(url)

!chainlit run file_name.py
"""
```