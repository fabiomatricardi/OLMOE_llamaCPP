import configparser


def create_config():
    config = configparser.ConfigParser()

    # Add sections and key-value pairs
    config['Model'] = {'name': 'OLMoE-1B-7B-0924-Instruct', 'file': 'OLMoE-1B-7B-0924-Instruct-Q4_K_L.gguf', 
                       'NCTX' : 4096, 'STOPS': ["<|endoftext|>"]}
    config['UI'] = {'myheader': 'Powerwed by OLMoE 1B-7B, the best 1B MOE chat model',
                          'cursor': "✨", 'av_us' : '🧔‍♂️', 'av_ass' : '🌀'}  
                          #"🦖"  #A single emoji, e.g. "🧑‍💻", "🤖", "🦖". 😁🤖🧔‍♂️🧞‍♂️🔮🩻🪆🌀🟡🟨💬♦️ Shortcodes are not supported.


    # Write the configuration to a file
    with open('OLMOE.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)


if __name__ == '__main__':
    create_config()