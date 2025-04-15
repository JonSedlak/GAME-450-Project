from chat_runner import run_chat, tool_router
import random
import json

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
        self.messages.append({'role': 'tool',
                          'name': response.message.tool_calls[0].function.name, 
                          'arguments': response.message.tool_calls[0].function.arguments,
                          'content': process_function_call(response.message.tool_calls[0].function)
                         })
        response = self.completion()    
    
    return response

def main():
    run_chat(
        template_file="FinalProjectCode/trader_chat.json",
        sign="Jon, Nico, Alex",
        inventory=["health potion", "mana potion", "elven cloak"],
        response_processor=process_response, # Pass your response processor
        end_regex=r"ORDER(.*)DONE"
    )

if __name__ == "__main__":
    main()