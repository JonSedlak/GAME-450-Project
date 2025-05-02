# Magic and Muscles
### **Authors:**   #*Jonathan Sedlak,   Nicholas Novak,   Alex Wood*

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
- 
