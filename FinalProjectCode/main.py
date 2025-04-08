# Main file for DND game
from pathlib import Path
from ollama import chat # Import Ollama
import sys
sys.path.append(str(Path(__file__).parents[1]))


# Import the Utils stuff here
from ollama import chat
from util.llm_utils import pretty_stringify_chat, TemplateChat, ollama_seed as seed

# Define model options/settings
context = 'You are a D&D shopkeeper that encounters adventurers as they walk into the shop. You (the shopkeeper) sells items that the adventurers need based on what adventure they will embark on and their class (wizards, sorcerer, paladin, etc..). Your shop has infinite items, but depending on the quality of the item is how much gold it will cost, (leather armor costs 5 gold, master sword costs 100 gold, etc..). The adventurer might try to negotiate a price. Remeber how much gold each item costs that you are selling and remember how much gold the player (adventurer) has. After negotiating a trade, calculate the total price of the trade and subtract it from the players gold offering.'
sign_your_name = 'Jon, Nico, Alex'
model = 'llama3.2'
messages = [{'role': 'system', 'content': context}]
options = {'temperature': 0.2, 'max_tokens': 100, 'seed': seed(sign_your_name)} # Temperature: Low = Accurate, High = Creative

####################################################################
# Funtion to run the chat

def run_console_chat(sign, **kwargs):
    chat = TemplateChat.from_file(sign=sign, **kwargs)
    chat_generator = chat.start_chat()
    print(next(chat_generator))
    while True:
        try:
            message = chat_generator.send(input('You: '))
            print('Agent:', message)
        except StopIteration as e:
            if isinstance(e.value, tuple):
                print('Agent:', e.value[0])
                ending_match = e.value[1]
                print('Ending match:', ending_match)
            break

####################################################################
# Chat loop
# while True:
#   # Send message to Chat Model and store assistant response in Response
#   response = chat(model=model, messages=messages, stream=False, options=options)
#   print(f'========\nAgent: {response.message.content}')
#   messages.append({'role': 'assistant', 'content': response.message.content})

#   # Prompt for user input
#   message = {'role': 'user', 'content': input('========\nYou: ')}
#   messages.append(message)

#   if messages[-1]['content'] == '/exit':
#     break
  
####################################################################
# MAIN
if __name__ == "__main__":
    # Run lab04.py to test your template interactively
   
    run_console_chat(
        template_file="FinalProjectCode/trader_chat.json",
        inventory=["mana potion", "health potion"],
        sign=sign_your_name,
        end_regex=r"ORDER(.*)DONE"
    )
