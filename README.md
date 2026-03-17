# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- Number guesssing game.
- Input a number in the range of game mode, the game will tell you if you should go higher or lower, correct you answer based on that. If you get the right answer in the allotted tries then you win!

- [ ] Detail which bugs you found.
- Hint Mechanism
- Difficult Level Attempts
- Difficulty Level Range

- [ ] Explain what fixes you applied.
- Corrected the hint logic, if guess is higher than the number then hint should say go lower and vice versa
- Corrected the number of attempts given at each difficulty level
- Corrected the range of number to guess from for depending on the difficulty

## 📸 Demo

- ![My screenshot](winning.png)


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
