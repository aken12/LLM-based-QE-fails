LONG_ANSWER_EVALUATION='''
You will be given a question, a reference answer, and an AI-generated answer. 
Your job is to evaluate whether the AI-generated answer includes the information from the reference answer. 
You must evaluate the AI-generated answer based solely on the reference answer and avoid using your own knowledge. 
Treat the answer as "correct" if it includes all the information in the reference answer, "partially correct" if it includes some of the information, and "incorrect" if it includes none of the information or contradicts the reference answer. 
After providing your explanation, output your final verdict by strictly using one of the following: 
"[[2]]" if AI-generated answer is "correct", 
"[[1]]" if AI-generated answer is "partially correct", and 
"[[0]]" if AI-generated answer is "incorrect".
'''

QUERY2DOC = '''
Write a passage that answers the given query: {Query}
'''
    
QUERY2EXPANSION = '''
Write a list of keywords for the following query: {Query}
'''
    
GAQR_TEACHER = '''
You are a search engine. Below are a query and its answer:
query: {Query}
answer: {Answer}
In order to obtain information corresponding to this answer, please provide at least three rewritten queries. Do not answer the rewritten queries. Don't output any words other than the rewritten queries.
''' # Based on: https://github.com/youngbeauty250/GaQR/blob/main/

GAQR_STUDENT = '''
You are a search engine. In order to obtain information for answering the query, please provide at least three rewritten queries.
Do not answer the rewritten queries. Don't output any words other than the rewritten queries. 
Below are a query: {Query}
''' # Based on: https://github.com/youngbeauty250/GaQR/blob/main/

Q2D_PRF = """
Write a passage that answers the given query based on the context:
Context: 
{PRF_doc_1}
{PRF_doc_2}
{PRF_doc_3}
query: {Query}
passage:
"""
    
ANSWER_GENERATION = """
{examples_1}
{examples_2}
{examples_3}
{examples_4}
Q: {Query}
A: 
"""
