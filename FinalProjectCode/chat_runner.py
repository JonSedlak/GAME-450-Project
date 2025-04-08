
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))
from util.llm_utils import TemplateChat


# Simple tool processor for demonstration (replace with real tools later)
def tool_router(response):
    content = response.message.content
    # Placeholder: we can parse and route tool calls here
    # For now, just return the response unchanged
    return response


def run_chat(template_file, sign, **kwargs):
    chat = TemplateChat.from_file(
        template_file=template_file,
        sign=sign,
        function_call_processor=tool_router,
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
