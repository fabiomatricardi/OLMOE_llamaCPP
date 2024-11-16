# here using pure llama.cpp server with llama-server.exe -m models/OLMoE-1B-7B-0924-Instruct-Q4_K_L.gguf
# main: server is listening on http://127.0.0.1:8080 - starting the main loop
from openai import OpenAI
import sys
from time import sleep
import configparser

########### read ini FILE ###############################################
def read_config():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('OLMOE.ini',encoding='utf-8')

    # Access values from the configuration file
    #debug_mode = config.getboolean('General', 'debug')
    NCTX = config.getint('Model', 'NCTX')
    modelname = config.get('Model', 'name')
    modelfile = config.get('Model', 'file')
    STOPS = config.get('Model', 'STOPS')
    myheader = config.get('UI', 'myheader')
    cursor = config.get('UI', 'cursor')
    av_us = config.get('UI', 'av_us')
    av_ass = config.get('UI', 'av_ass')

    # Return a dictionary with the retrieved value
    return NCTX,modelname,modelfile,STOPS,myheader,cursor,av_us,av_ass

############### set global variables ############################################
NCTX,modelname,modelfile,STOPS,myheader,cursor,av_us,av_ass = read_config()

print("\033[95;3;6m")
print("1. Waiting 10 seconds for the API to load...")
sleep(10)
print("2. Connecting to the Llama.CPP server API...")
print(myheader)
print("\033[0m")  #reset all

# Point to the local server
client = OpenAI(base_url="http://localhost:8080/v1", api_key="not-needed", organization=modelname)
history = [
    {"role": "system", "content": "You are OLMoE AI, a helpful assistant. You reply only to the user questions. You always reply in the language of the instructions.",}
]
print("\033[92;1m")
counter = 1
while True:
    history = [
        {"role": "system", "content": "You are OLMoE AI, a helpful assistant. You reply only to the user questions. You always reply in the language of the instructions.",}
    ]        
    userinput = ""
    print("\033[1;30m")  #dark grey
    print("Enter your text (end input with Ctrl+D on Unix or Ctrl+Z on Windows) - type quit! to exit the chatroom:")
    print("\033[91;1m")  #red
    lines = sys.stdin.readlines()
    for line in lines:
        userinput += line + "\n"
    if "quit!" in lines[0].lower():
        print("\033[0mBYE BYE!")
        break
    history.append({"role": "user", "content": userinput})
    print("\033[92;1m")

    completion = client.chat.completions.create(
        model="local-model", # this field is currently unused
        messages=history,
        temperature=0.25,
        frequency_penalty  = 1.53,
        max_tokens = 1200,
        stream=True,
        stop=STOPS
    )

    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content
    history.append(new_message)  
    counter += 1  