import configparser
"""
    # Add sections and key-value pairs
    config['Model'] = {'name': 'OLMoE-1B-7B-0924-Instruct', 'file': 'OLMoE-1B-7B-0924-Instruct-Q4_K_L.gguf', 
                       'NCTX' : 4096, 'STOPS': ["<|endoftext|>"]}
    config['UI'] = {'myheader': 'Powerwed by OLMoE 1B-7B, the best 1B MOE chat model',
                          'cursor': "✨", 'av_us' : '🧔‍♂️', 'av_ass' : '🌀'}  
"""

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


if __name__ == '__main__':
    # Call the function to read the configuration file
    NCTX,modelname,modelfile,STOPS,myheader,cursor,av_us,av_ass = read_config()

    # Print the retrieved values
    print(f'NCTX: {NCTX}')
    print(f'modelname: {modelname}')
    print(f'modelfile: {modelfile}')
    print(f'STOPS: {STOPS}')
    print(f'myheader: {myheader}')
    print(f'cursor: {cursor}')
    print(f'av_us: {av_us}')
    print(f'av_ass: {av_ass}')