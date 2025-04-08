from chat_runner import run_chat


def main():
    run_chat(
        template_file="FinalProjectCode/trader_chat.json",
        sign="Jon, Nico, Alex",
        inventory=["health potion", "mana potion", "elven cloak"],
        end_regex=r"ORDER(.*)DONE"
    )


if __name__ == "__main__":
    main()
