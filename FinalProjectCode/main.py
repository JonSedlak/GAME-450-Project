# Main file for DND game
from pathlib import Path
from ollama import chat # Import Ollama
import sys
sys.path.append(str(Path(__file__).parents[1]))

# Import the Utils stuff here
from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Define model options/settings
sign_your_name = 'Jon and Nico'
model = 'llama3.2'
messages = [{'role': 'system', 'content': 'You are a DND Dungeon Master'}]
options = {'temperature': 0.2, 'max_tokens': 100, 'seed': seed(sign_your_name)} # Temperature: Low = Accurate, High = Creative

####################################################################
# Chat loop
while True:
  # Send message to Chat Model and store assistant response in Response
  response = chat(model=model, messages=messages, stream=False, options=options)
  print(f'Agent: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})

  # Prompt for user input
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)

  if messages[-1]['content'] == '/exit':
    break
####################################################################


# Save chat
# with open(Path('lab03/attempts.txt'), 'a') as f:
#   file_string  = ''
#   file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
#   file_string += f'Model: {model}\n'
#   file_string += f'Options: {options}\n'
#   file_string += pretty_stringify_chat(messages)
#   file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
#   f.write(file_string)

