# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  When I ran the game the hints were backwards, like I guessed 65 and the secret was 22 so it told me to go higher instead of lower. The attempt counter was off too, it started at 0 on new games and the number shown in the UI didn't match what was actually being tracked. Also when I lost and clicked New Game it just showed "Game over" again right away because the status never got cleared.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  I used Copilot in VS Code for this project. For a correct suggestion, I asked Copilot to explain the check_guess function and it correctly flagged that the hint messages were swapped, suggesting I change "Go HIGHER" to "Go LOWER" for the Too High case and "Go LOWER" to "Go HIGHER" for the Too Low case. I verified it by running pytest and all three tests passed after the fix. For a misleading suggestion, when I asked Copilot to fix the new game reset bug it suggested setting attempts back to 0, which it copied from the existing buggy code. I caught it because the attempt counter was still off in the live app after applying the fix, so I checked the initial session state setup and saw attempts was initialized to 1, not 0, which confirmed Copilot's suggestion was wrong.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

  I decided a bug was fixed when it passed both a pytest test and worked correctly in the live app. For the hints bug I ran pytest and all three tests passed, confirming that guessing too high returns "Too High" with "LOWER" in the message and guessing too low returns "Too Low" with "HIGHER" in the message. For the new game bug I manually tested it in the browser by losing a game and clicking New Game, verifying that it let me play again instead of showing "Game over" immediately. Copilot helped me generate the pytest cases by suggesting the structure of unpacking the tuple return value from check_guess and asserting on both the outcome and the message.
  
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
