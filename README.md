# Ruthenium's Quiz Game

Welcome to Ruthenium's Quiz Game! This is a simple Python quiz game where players can choose between different game modes: Charades, Riddles, and Trivia.

## Description

This project consists of a Python script (`quiz_game.py`) that implements the QuizGame class. The class includes methods for playing different game modes, including a more difficult bonus round, and loading quiz data from a JSON file (questions, answers, clues, etc). The game offers three modes: Charades, Riddles, and Trivia and triggers a bonus round if the player gets 4 or more out of 5 questions correct. It also has navigation options to welcome the player, and to ask the player if they'd like to play again.

## Instructions

To play the game, simply run the following command in the terminal:

```bash
python ruthenium_quizgame.py ruthenium_quiz_questions.json
```

We hope you enjoy our game!

## Methods/Contributors
Here's a list of our functions and contributors:
| Method/Function        | Primary Author | Techniques Demonstrated      |
|------------------------|----------------|------------------------------|
| __init__               | Maya Mistry   | magic method but it is init |
| load_quiz_data         | Maya Mistry   | key expression, with statement |
| play_charades          | Maya Mistry   ||
| play_riddles           | Maya Mistry   ||
| play_trivia            | Maya Mistry   ||
| play_again             | Maya Mistry   ||
| reset_game             | Maya Mistry   ||
| run                    | Evan Schneider||
| continue_to_next_question| Evan Schneider||
| bonus_round | Evan Schneider | conditional expression, f string |
