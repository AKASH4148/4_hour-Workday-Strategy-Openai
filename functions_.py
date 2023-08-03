from langchain import LLMChain
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain

#1) Loading You tube video and generating transcript
def load_video(url):
    loader=YoutubeLoader.from_youtube_url(url, add_video_info=True)
    data=loader.load()
    return data

#2) Spiliting the Transcript into Chunks

def split_text(data, chunk_size, chunk_overlap):
    text_splitter=TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs=text_splitter.split_documents(data)
    return docs

#3) Initialize the Large Language Model
def initialize_llm(openai_api_key, model_name, temperature):
    llm=ChatOpenAI(openai_api_key=openai_api_key, model_name=model_name, temperature=temperature)
    return llm

#4) Initialize the Summarize Chain
def initialize_summarize_chain(llm, chain_type, question_prompt, refine_prompt):
    strategy_chain=load_summarize_chain(llm=llm, chain_type=chain_type, verbose=True, question_prompt=question_prompt, refine_prompt=refine_prompt)
    return strategy_chain
#5) #generate a Strategy
def generate_strategy(strategy_chain, docs):
    strategy=strategy_chain.run(docs)
    return strategy
#6) Initialize the plan chain
def ini_generate_plan(llm, prompt, verbose):
    plan_chain=LLMChain(llm=llm, prompt=prompt, verbose=verbose)
    return plan_chain

#7) Generate a plan
def generate_plan(plan_chain, strategy):
    plan=plan_chain(strategy)
    return plan