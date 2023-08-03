import streamlit as st 
from prompting import PROMPT_STRATEGY, PROMPT_STRATEGY_REFINE, PROMPT_PLAN
from functions_ import load_video, split_text, initialize_llm, initialize_summarize_chain, generate_strategy, ini_generate_plan, generate_plan
import os

#setting open api key.
#OPENAI_API_KEY="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"
openai_api_key=os.environ.get('OPENAI_API_KEY')

with st.container():
    st.markdown("""
#Four-Hour Workday Plan : 
This streamlit Implementation shows how to create a strategy for a four-hour workday based on a YouTube Video.
We're using an easy Langchain implementation to show how to use the diffrent component of Langchain.
The is the part of Modeling Days learning. Find the details and code on my [Github](https://github.com/AKASH4148) 
"""
)
    
url_input=st.text_input(label="URL Input", label_visibility="collapsed", placeholder="https://www.youtube.com/watch?v=T6hmdrsLQj8", key="url_input")
if url_input:
    if url_input=='empty':
        st.write("Please enter a valid URL")
    else:
        with st.spinner('Loading the You Tube video transcript....'):
            #Load the you tube video transcript
            data=load_video(url_input)

            #split the transcript into chuncks
            data=split_text(data, chunk_size=1000, chunk_overlap=100)

        #Initialize the llm
        llm=initialize_llm(openai_api_key=openai_api_key, model_name='gpt-3.5-turbo', temperature=0.4)

        with st.spinner("Generating a strategy....."):
            #initialize the summarize chain
            strategy_chain=initialize_summarize_chain(llm=llm, chain_type='refine', question_prompt=PROMPT_STRATEGY, refin_prompt=PROMPT_STRATEGY_REFINE)

            #Generate a strategy
            strategy=generate_strategy(strategy_chain, docs)

        with st.spinner("Generating a plan...."):
            #Initialize the plan chain
            plan_chain=ini_generate_plan(llm=llm, prompt=PROMPT_PLAN, verbose=True)

            #Generate a plan based on the strategy
            plan=generate_plan(plan_chain, strategy)
            st.write(plan)
        st.stop()

