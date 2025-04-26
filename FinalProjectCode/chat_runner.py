
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))
from util.llm_utils import TemplateChat
from collections import defaultdict


# Simple tool processor for demonstration (replace with real tools later)
def tool_router(func):
    calls = defaultdict(list)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        calls[f'{func.__name__}_calls'].append({'name': func.__name__, 'args': args, 'kwargs': kwargs, 'result': result})
        #print('\n\nTools Called: \n', calls, '\n\n')
        return result
    return wrapper


def run_chat(**kwargs):
    chat = TemplateChat.from_file(
        **kwargs
    )

    # Start the chat loop
    first_message = chat.start_chat()
    print("Agent:", first_message)

    while True:
        try:
            user_input = input("You: ")
            if user_input.strip().lower() == "/exit":
                break
            response = chat.send(user_input)
            print("Agent:", response)

        except StopIteration as e:
            if isinstance(e.value, tuple):
                print("Agent:", e.value[0])
                print("Ending match:", e.value[1])
            break
