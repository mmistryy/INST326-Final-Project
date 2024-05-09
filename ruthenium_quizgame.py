# Group: Ruthenium 
# Maya Mistry, Evan Schneider
# INST326 (Spring 2024)
# Final Project: Ruthenium's Quiz Game

import json
import random

class QuizGame:
    """
    A class that represents a quiz game with multiple game modes.

    Attributes:
        quiz_data (dict): A dictionary containing quiz data loaded from the JSON file.
        cumulative_score (int): The cumulative score of the player in the current game session.
        correct_answers (int): The number of questions answered correctly.
        current_game_mode (function): The current game mode function being played.
        questions_attempted (int): The total number of questions attempted in the current session.
    """

    def __init__(self, file_name):
        """
        Brings in the quiz game with data from a JSON file.

        Args:
            file_name (str): The name of the JSON file containing quiz questions.
        """
        self.quiz_data = self.load_quiz_data(file_name) 
        self.cumulative_score = 0
        self.correct_answers = 0
        self.current_game_mode = None
        self.questions_attempted = 0

    def load_quiz_data(self, file_name):
        """
        Loads quiz data from the JSON file.

        Args:
            file_name (str): The name of the JSON file containing quiz questions.

        Returns:
            dict: The data loaded from the JSON file.
        """
        with open(file_name, 'r') as file:
            return json.load(file)

    def play_charades(self):
        """Plays the charades game mode."""
        self.current_game_mode = self.play_charades
        charades_questions = self.quiz_data['charades']
        question = random.choice(charades_questions)
        
        print("\n*** Charades Game Mode ***")
        print("Guess the thing or person based on the charades clues:")
        print("Question:", question['question'])
        
        print("\nClues:")
        for i, clue in enumerate(question['clues'], 1):
            print(f"{i}. {clue}")
        
        guess = input("\nYour guess: ").strip().capitalize()

        if guess == question['answer']:
            print("Nice, that's correct!")
            self.cumulative_score += 1
            self.correct_answers += 1
        else:
            print("Wrong... it's actually:", question['answer'])

        self.questions_attempted += 1
        self.continue_to_next_question()

    def play_riddles(self):
        """Plays the riddles game mode."""
        self.current_game_mode = self.play_riddles
        riddles = self.quiz_data['riddles']
        question = random.choice(riddles)
        
        print("\n*** Riddles Game Mode ***")
        print("Can you solve this riddle?")
        print("Question:", question['question'])
        
        guess = input("\nYour guess: ").strip().capitalize()

        if guess == question['answer']:
            print("Nice, that's correct!")
            self.cumulative_score += 1
            self.correct_answers += 1
        else:
            print("Wrong... it's actually:", question['answer'])

        self.questions_attempted += 1
        self.continue_to_next_question()

    def play_trivia(self):
        """Plays the trivia game mode."""
        self.current_game_mode = self.play_trivia
        trivia_questions = self.quiz_data['trivia']
        question = random.choice(trivia_questions)
        
        print("\n*** Trivia Game Mode ***")
        print("Answer the trivia question:")
        print("Question:", question['question'])
        
        guess = input("\nYour answer: ").strip().capitalize()

        if guess == question['answer']:
            print("Nice, that's correct!")
            self.cumulative_score += 1
            self.correct_answers += 1
        else:
            print("Wrong... it's actually:", question['answer'])

        self.questions_attempted += 1
        self.continue_to_next_question()

    # run(self)

    # continue_to_next_question(self)

    # bonus round

    def play_again(self):
        """
        Prompts the player to play again or quit.
        If the player chooses to continue, the game state is reset.
        """
        choice = input("Thanks for playing! Would you like to play again? (yes/no): ").strip().lower()
        if choice == 'yes':
            self.reset_game()
            self.run()
        else:
            print("Ok, see you next time!")

    def reset_game(self):
        """Resets the game state to start a new game session."""
        self.cumulative_score = 0
        self.correct_answers = 0
        self.current_game_mode = None
        self.questions_attempted = 0

if __name__ == "__main__":
    quiz_game = QuizGame('ruthenium_quiz_questions.json')
    quiz_game.run()