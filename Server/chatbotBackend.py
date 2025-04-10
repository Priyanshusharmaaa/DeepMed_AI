
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq


prompt_template = """
You are a trusted medical advisor. Answer user health questions based on general medical knowledge.
Always recommend consulting a doctor for serious or unclear conditions. Be polite, accurate, and detailed.

Question: {question}
Helpful answer:
"""

prompt = PromptTemplate(
    input_variables=["question"],
    template=prompt_template,
)


llm = ChatGroq(
    temperature=0.3,
    groq_api_key="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",
    model_name="llama3-70b-8192"
)

memory = ConversationBufferMemory(memory_key="chat_history")

chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

def ask_medical_bot(question: str) -> str:
    response = chain.run(question=question)
    return response

