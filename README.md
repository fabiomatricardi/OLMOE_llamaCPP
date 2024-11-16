<img src='https://github.com/fabiomatricardi/OLMOE_llamaCPP/raw/main/olmoe-logo.png' width = 900>
# OLMOE_llamaCPP
Streamlit chatbot with llama.cpp and OLMoE from AllenAI AI2

### Introduction
OLMoE is a sparse Model, Mixture of Experts by AllenAI. The model use 1B active parameters during inference, but has a total of 7B.

There are actually some limitations on running these models: only the flagged options are really working:
- [x] Transformers (not quantized) requires a lot of memory
- [ ] Ollama (quantized) actually does not support yet OLMoE
- [ ] Llama-cpp-python (quantized) actually does not support yet OLMoE
- [x] **llama.cpp (quantized) is the best working option**


### The Stack
Here I am using llama.cpp directly from G.Gerganov repo, running the `llama-server.exe` in one terminal window, and a python program in another terminal.

- You can actually use directly the rovided Web-chat interface, amazing look and functionalities
- you can use python with the `openai` module
- you can use python with traditional `requests/json` modules 

Here I am using the `openai` module in 3 different applications:
- terminal UI
- automatic benchmark evaluation in the terminal
- Streamlit app

## Benchmarks results
<img src='https://github.com/fabiomatricardi/OLMOE_llamaCPP/raw/main/OLMoE-1B-7B-0924-Instruct_table.png' width = 800>

The model is quite good at:
- conversation
- summarization
- text understanding
- content creation
- creativity
- **REFLECTION PROMPT**: despite being only a 1B active parameters, the results are coherent and correctly formatted

#### IT struggles in RAG because it does not stick to the context only!

---

## How to use this repo
2 Steps: install llama.cpp and clone the repo
#### 1 - install llama.cpp


#### 2 - clone and run the repo
Open a terminal window in your preferred position
- clone the repo
- enter the repo directory
- create a python virtual environment in the repo directory
```
python -m venv venv
venv\script\activate
pip install openai tiktoken streamlit==1.40.0
```
- open another terminal window





