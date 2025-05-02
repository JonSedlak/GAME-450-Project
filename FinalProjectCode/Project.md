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

#DELETE THIS below

Agent: Welcome, brave adventurer! I see you're preparing for a grand quest ahead. You've come to the right place - Magic and Muscles is here to equip you with the finest gear to aid you on your 
journey. What can I help you find today?

Please take a look around our shelves, and let me know what catches your eye. We have everything from common potions to rare magical artifacts. Our prices are fair, but we do offer some... creative options for those who are willing to negotiate.

What's on your mind? Do you need something specific for your class or the nature of your quest?
You: I need a sword
Agent: A sword, you say? We have just the thing for you. Let me show you our selection.

We have a fine Longsword with a sturdy blade and a comfortable grip. It's perfect for any adventurer looking to deal damage from a distance. The price on this one is 25 gold pieces.

Next to it, we have a Master Sword, said to be forged in the heart of a dragon's lair. Its power is unmatched, but its price reflects that - 50 gold pieces.

We also have a Short sword with a sleek design and a balanced weight. It's ideal for those who prefer close combat. The price on this one is 15 gold pieces.

Which one catches your eye?
You: I want the short sword for 10
Agent: You want to buy the Short Sword, but you're offering a price of 10 gold pieces. I'm afraid that's not quite enough.

The Short Sword is a fine piece of craftsmanship, but it's worth more than that. I can offer you a discount, but I need at least 15 gold pieces for it.

Would you like to try again? Perhaps we can come to a mutually agreeable price.
You: 13?
Agent: You're trying to negotiate the price of the Short Sword again! You're offering 13 gold pieces, but I'm afraid that's still a bit short.

Let me see... (checking prices) Ah, yes! I can do 14 gold pieces for you. That's as low as I can go without losing money on the deal.

What do you say? Will 14 gold pieces seal the deal for you?
You: Deal.
Agent: We have a deal! The Short Sword is yours for 14 gold pieces.

Let me just ring this up for you... (rings up the sale)

ORDER [ {Short Sword: 14}, {Total: 14} ] DONE.
Ending match: [ {Short Sword: 14}, {Total: 14} ]
Exception ignored on calling ctypes callback function: <function catch_errors.<locals>.call_with_this at 0x000002A08C46FC10>
Traceback (most recent call last):
  File "C:\ProgramData\Anaconda3\lib\site-packages\comtypes\_comobject.py", line 91, in call_with_this
  File "C:\ProgramData\Anaconda3\lib\logging\__init__.py", line 1474, in error
  File "C:\ProgramData\Anaconda3\lib\logging\__init__.py", line 1699, in isEnabledFor
TypeError: 'NoneType' object is not callable