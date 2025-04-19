# LLM-based-QE-fails  
Experimental Details for “LLM-based Query Expansion Fails for Unfamiliar and Ambiguous Queries”

## Query Expansion
- **LLMs used**  
  - gpt-3.5-turbo-0125  
  - [meta-llama/Meta-Llama-3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct)  
  - [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)  
- **Common settings**  
  - Temperature for query expansion: 0  
  - Maximum output tokens: 128  
- **Query expansion methods**  
  - **Query2Doc**  
    - [Query2doc: Query Expansion with Large Language Models](https://aclanthology.org/2023.emnlp-main.585/)  
  - **Query2Expansion**  
    - [Query Expansion by Prompting Large Language Models](https://arxiv.org/abs/2305.03653)  
  - **GaQR (learning-based method)**  
    - [GaQR: An Efficient Generation-augmented Question Rewriter](https://dl.acm.org/doi/10.1145/3627673.3679930)  
    - We performed our own hyperparameter tuning.  
    - Training data: 5,000 randomly sampled MS MARCO train examples + 2,863 MIRACL train examples (7,863 total)  
    - Generate 20 rewrites per query with GPT (gpt-3.5-turbo-0125, temperature = 1.0), then filter by effectiveness in BM25 (Recall@100)  
    - Train [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on the filtered data using:  
      - LoRA (alpha = 32, r = 16)  
      - learning_rate = 1e-4  
      - epochs = 5  
      - batch size = 32  
    - Development set: 500 randomly sampled MS MARCO train examples  

## Evaluation Criteria for Assessing LLM Knowledge
- **Short Answer (NQ, TQ)**  
  - Metric: Exact Match  
  - Labels: Correct or Incorrect  
    - "LLM has sufficient knowledge" ⇨ Correct  
    - "LLM lacks sufficient knowledge" ⇨ Incorrect  
- **Long Answer (MS MARCO, BioASQ)**  
  - LLM-based evaluation using the `LONG_ANSWER_EVALUATION` prompt in `prompt.py`  
  - Reference papers:  
    - [Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference](https://arxiv.org/abs/2403.04132)  
    - [Evaluating Open-QA Evaluation](https://proceedings.neurips.cc/paper_files/paper/2023/file/f323d594aa5d2c68154433a131c07959-Paper-Datasets_and_Benchmarks.pdf)  
  - LLM configuration:  
    - gpt-4-turbo-2024-04-09  
    - Temperature: 0  
  - Output labels:  
    - correct (2)  
    - partially correct (1)  
    - incorrect (0)  
    - "LLM has sufficient knowledge" ⇨ correct or partially correct  
    - "LLM lacks sufficient knowledge" ⇨ incorrect  
  - Agreement with human author on 100 randomly sampled cases:  
    - Cohen’s κ = 0.6218  
