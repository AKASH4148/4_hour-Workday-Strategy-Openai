from langchain.prompts import PromptTemplate

strategy_template= """
You are an expert in creating strategies for getting a four-hour workday. 
You are a productivity coach and you have helped many people achieve a four-hour workday.
The strategy should be based on the following text:
----------
{text}
----------
Given the text, create a detailed strategy. The strategy is aimed to get a working plan on how to achive a four-hour workday.
The strategy should be as detailed as possible
STRATEGY:
"""

PROMPT_STRATEGY = PromptTemplate(template=strategy_template, input_variables=["text"])

#The second prompt is refinement of the summary, based on subsequent chunks.
strategy_refine_template= (
    """
    You are an expert in creating strategies for getting four-hour workday.
    Your goal is to create a detailed strategy for getting a four-hour workday.
    we have provided an existing strategy upto cetain point: {existing_answer}
    (only if you needed) with some more context below

    ---------
    {text}
    ---------
    Given the new context, refine the strategy.
    The strategy is aimed to get a working plan on how to achieve a four-hour workday.
    If the context isn't useful, return the original strategy
    """ 
)

PROMPT_STRATEGY_REFINE=PromptTemplate(
    input_variables=["existing_answer", "text"],
    template=strategy_refine_template
)
plan_template = """
You are an expert in creating plans for getting a four-hour workday. You are a productivity coach and you have helped many people achieve a four-hour workday.
You're goal is to create a detailed plan for getting a four-hour workday.
The plan should be based on the following strategy:
------------
{strategy}
------------
Given the strategy, create a detailed plan. The plan is aimed to get a working plan on how to achieve a four-hour workday.
Think step by step.
The plan should be as detailed as possible.
PLAN:
"""
PROMPT_PLAN=PromptTemplate(template=plan_template, input_variables=["strategy"])
