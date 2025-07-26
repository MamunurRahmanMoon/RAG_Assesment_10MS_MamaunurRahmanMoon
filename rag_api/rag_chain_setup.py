# rag_chain_setup.py

from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain_core.runnables import RunnableLambda

# Load and split markdown
loader = UnstructuredMarkdownLoader("extracted_folder/parsed_text.markdown")
doc = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=100)
splits = text_splitter.split_documents(doc)

# Embedding + Vector DB
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = Chroma.from_documents(splits, embedding=embedding_model)
retriever = vectorstore.as_retriever(search_kwargs={"k": 10})

# Short-Term Memory
memory = ConversationBufferMemory(return_messages=True, memory_key="history")

# LLM
llm = GoogleGenerativeAI(model="models/gemini-2.5-pro")

# Prompt
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="history"),
    ("system", "Answer in Bangla. Use both context and previous conversation."),
    ("human", "Context:\n{context}\n\nQuestion: {question}")
])

# Final RAG Chain
def get_rag_chain():
    context_chain = retriever | (lambda docs: "\n\n".join(d.page_content for d in docs))

    rag_chain = (
        {
            "context": context_chain,
            "question": RunnablePassthrough(),
            "history": RunnableLambda(lambda _: memory.load_memory_variables({})["history"])
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain, memory
