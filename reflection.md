# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").




**Yes the hints were backwards:**

*when i moved towards a lower number it would keep asking me to go lower
*but when i moves to a higher number it would keep asking me to move higher



**Difficulties weren't calibrated correctly, both easy and hard gave less tries than normal**

**The range of numbers to guess from weren't correct given the difficulty level**

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

***I used copilot***

***The AI got the update score function correct and moved it accordingly to the logic file***

***It did not however understand the logic corrections needed for difficulty range and number of attemps, one of them i told it to do explicitly and one i fixed manually***

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?


*I mostly tested it on the app myself, but the ai also helped me write a few tests.*
*I tested the hint mechanism, difficulty toggle, new game button by using the app*

*Yes I went over how the update score test worked with the AI, both for implementation and understanding*

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

*States basically tell what changes and what doesn't, streamlit updates states after every interaction (because page rebuilds), but to store values we then use session states*


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

*Verify all the code AI gives me*

*Always make my intent clear, AI is not good at infering intent*

*Be more explicit with my instructions, and keep the scope of changes managable so that i also have context of what's happening*

*AI is very good at writing code, but not as effective as writing functional code. You need to be adding the functionality dimension yourself. Also the code is pretty much always correct but that doesn't mean it does what you want it to though*
