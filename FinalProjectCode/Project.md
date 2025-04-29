# Magic and Muscles
### **Authors:**   #*Jonathan Sedlak,   Nicholas Novak,   Alex Wood*

**Description:**
Our Ollama agent is a DND shopkeeper that runs Magic and Muscles. Its role is to welcome adventurers and sell them items based on their needs, such as the type of quest they will embark on or they class they belong to. The adventurers can negotiate a price if they so choose to. The shopkeeper will roll a 20 sided dice and (1) if the number is greater than or equal to 15, then the adventurer gets the price they negotatied for. (2) If the dice is less than 15, then the item is firm at the original price offered by the shopkeeper. (3) If the dice lands on 20, then the item is free. Once the trade is finalized the chat ends. 

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
