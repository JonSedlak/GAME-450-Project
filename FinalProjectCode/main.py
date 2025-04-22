from chat_runner import run_chat, tool_router
import random
from util.llm_utils import run_console_chat, tool_tracker
import json

@tool_tracker
def process_function_call(function_call):
    name = function_call.name
    args = function_call.arguments

    return globals()[name](**args)

def roll_for_price(player, item_price, player_negotiated_price , item):
    n_dice = 1
    sides = 20
    roll = sum([random.randint(1, sides) for _ in range(n_dice)])
    if roll == 20:
        return f'{player} rolled {roll} for {item} and succeeded and the item is free!'
    elif roll >= 15:
        return f'{player} rolled {roll} for {item} and the price was changed to {player_negotiated_price}'
    else:
        return f'{player} rolled {roll} for {item} and the price stays firm at {item_price}!'


def process_response(self, response):
    # Fill out this function to process the response from the LLM
    # and make the function call 
    
    if response.message.tool_calls:
        fn_call = response.message.tool_calls[0].function
        result = process_function_call(fn_call)

        # append the tool’s output
        self.messages.append({
            'role': 'tool',
            'name': fn_call.name,
            'content': result
        })

        # re‑invoke the model so it can see the tool’s output
        response = self.completion()

        # **append** that assistant response into the history
        self.messages.append({
            'role': response.message.role,
            'content': response.message.content
        })

    return response

def main():
    run_chat(
        template_file="FinalProjectCode/trader_chat.json",
        sign="Jon, Nico, Alex",
        process_response=process_response, # Pass your response processor
        end_regex=r"ORDER(.*)DONE"
    )

if __name__ == "__main__":
    main()