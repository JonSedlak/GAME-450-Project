# Magic and Muscles
### **Authors:**   *Jonathan Sedlak,   Nicholas Novak,   Alex Wood*

**Description:**
Our Ollama agent is a DND shopkeeper that runs Magic and Muscles. Its role is to welcome adventurers and sell them items based on their needs, such as the type of quest they will embark on or the class they belong to. The adventurers can negotiate a price if they so choose to. The shopkeeper will roll a 20 sided dice and (1) if the number is greater than or equal to 15, then the adventurer gets the price they negotiated for. (2) If the dice is less than 15, then the item is firm at the original price offered by the shopkeeper. (3) If the dice lands on 20, then the item is free. Once the trade is finalized the chat ends. Based on if the player negotiates for a trade, the system will output a voice. 

**Recommended Approach:**
"I am a wizard about to embark on a very long journey throught the forest. I am looking for a powerful staff and a new cloak. What do you have in stock?"
If you are offered an item that you are interested in and want to negotiate for it then say the item name and price in gold: "I would like to buy the legendary staff of elements, but I will only offer you 45 gold."


---

**Jonathan Sedlak**
- Created the framework for the system
- Implemented ollama and the chat system with given model paremeters
- Created a template for the model to use which acts as a tavern shopkeeper
- Assisted with further implementation

**Nicholas Novak**
- I implemented and modified a tool usage system that takes into account that the model uses the tools constantly despite being told not to use a tool after every response
- The tool rolls a dice and uses a random number generator to roll with set thresholds for failure success and accounting for non-barterting responses
- Helped write the content for the initial model prompt

**Alex Wood**
- Created the detailed and complex RAG database, and implemented the RAG system into the agent.
- Debugging of some text to speech properties
- General brainstorm process, modular designing, and documentation

---

# Final Project Documentation


**Description**
We plan to use prompt engineering to create a D&D shopkeeper that encounters adventurers as they walk into the shop. The shopkeeper sells items that the adventurers need based on what adventure they will embark on and their class (wizard, sorcerer, paladin, etc.). Our model parameters will consist of a temperature of around 0.2, which will maintain consistency and accuracy with responses, giving it the slightest amount of creativity, especially regarding RAG-based information and shop items. The max token is set to 150, which is plenty for the generative response to get out what it needs to say. 

To further enhance the functionality of our system, we will be using tool calling to allow the player to haggle/barter with the shopkeeper and maybe lower the prices they will have to pay. This is done with a dice roll function that is specifically made for moments where you need to haggle a price. It will generate a random number and then check if they rolled one of three options: 20, greater than or equal to 15, or less than 15. Based on which dice is rolled, the system will generate a funny text-to-speech generation before finishing the trade. 

Finally, we will implement a Retrieval-Augmented-Generation (RAG) system to keep general information and stats on the shopkeeper’s inventory. Plan to be able to ask questions about stats and background on items and purposes, while the shopkeeper agent will pull the most accurate and applicable information.


**Features**
Base System Functionality
Our llama 3.2 agent is a D&D shopkeeper that runs Magic and Muscles. Its role is to welcome adventurers and sell them items based on their needs, such as the type of quest they will embark on or the class they belong to. The adventurers can negotiate a price if they so choose to. The shopkeeper will roll a 20 sided dice and (1) if the number is greater than or equal to 15, then the adventurer gets the price they negotiated for. (2) If the dice is less than 15, then the item is firm at the original price offered by the shopkeeper. (3) If the dice lands on 20, then the item is free. Once the trade is finalized the chat ends.

**Prompt Engineering and Model Parameter Choice**
Temperature: 0.2
Max_Tokens: 150
With the given parameters, we want the agent to be relatively accurate in its responses while still retaining some amount of creativity, hence the 0.2 temperature. Given the model 150 max tokens gives it that buffer room for the little extra amount of creativity. 
For prompt engineering our agent was given the role of a D&D shopkeeper that sells items to players who stop by. It will offer items based on the class and adventure of the player. The twist is that if the player tries to negotiate for a price of an item, then the agent will roll a dice and determine the new price of the negotiated item. The agent is to respond in a specific way that activates the tool call, and a specific way to end the conversation with the sold items and the price. 

**Tool Usage**
Roll_for_price is a tool that takes in player, item_price, player_negotiated_price, and item. It then uses a random number generator from 1-20 like a d20. It checks for 20, greater than or equal to 15, and less than 15. 20 means the item is free, greater than or equal to 15 means it is offered to you at your asked price, and lower means it is offered to you at the shopkeeper’s stated price. This tool is used for the purposes of negotiating price.

**Planning and Reasoning**
This was done using llama 3.2 as our LLM model for multi-step reasoning and planning. We use a step-by-step process within the model prompting us to give the llama agent a chain of thought process. Our model also uses an if-then thought process, like ‘if’ the player is a certain class, ‘then’ sell them certain items. Or ‘if’ the player is negotiating with me, ‘then’ use the tool calling feature. 

**RAG Implementation & Innovation**
The RAG system incorporated into the project is meant to contain a vast amount of information on enough items to make the experience more catered towards the individual needs of D&D classes. Within the RAG text file, we have selected 10 of the most popular character classes, namely: Wizard, Fighter, Rogue, Druid, Paladin, Sorcerer, Bard, Warlock, Ranger, and Artificer. Each section is formatted appropriately and contains a brief description of their characters general characteristics and three items that the Shopkeeper has in stock, 30 in total. Each item has a brief description and gives general stat upgrades or abilities of each item. From giving the RAG all of these details, our goal was to allow for the agent to make multiple connections between character class, personality, and items to make the best shopping recommendations. Then, based on the usefulness of these items, the shopkeeper can determine a fair price before beginning to haggle with the user and initiate tool calls.

**Additional Tools / Innovation**
Text-to-speech is used after a player negotiates for a trade. Based on the dice that is rolled, the AI will output 1 of 4 speeches before completing the trade. This adds some humor to the trading system when a player barters for a trade. 


**Code Quality & Modular Design**
Our code is formatted into a modular design, being separated into code chunks and files, all within the “FinalProjectCode” folder. 
