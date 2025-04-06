 # Tic Tac Toe Game in Kivy

This is a simple and fun Tic Tac Toe game built using the **Kivy** framework in Python. The game allows two players to take turns marking their spots on the board. The first player to align three of their marks vertically, horizontally, or diagonally wins the game. If the board is full without a winner, it results in a draw.

<img width="402" alt="image" src="https://github.com/user-attachments/assets/e34d0663-c448-4283-85c9-e1bd6d0b4182" />

## Features
- **Two-player gameplay**: Players alternate turns, one using "X" and the other using "O".
- **Interactive UI**: The board is made up of buttons that respond to clicks, changing color to indicate the current player's move.
- **Game End Popups**: A popup will appear to announce the winner or declare a draw at the end of the game.
- **Simple Reset Mechanism**: After a game ends, you can easily reset the board and start a new game.

## Installation

To run this game, you'll need to install the **Kivy** library. You can install it using `pip`:

```bash
pip install kivy
Running the Game
After installing Kivy, you can run the game by executing the Python script:

python tic_tac_toe.py
This will open a window with a Tic Tac Toe grid. Players can start playing by clicking on the empty cells.

Code Explanation
TicTacToe Class: This is the main class responsible for the game logic. It sets up a 3x3 grid of buttons where players can make their moves. It also handles checking for a winner or a draw.

Popup Notification: Whenever the game ends, a popup will display the message, announcing the winner or that it's a draw. The background is white with black text, and it includes emojis for added fun.

Reset Function: The game resets automatically after each round, clearing the board and allowing players to play again.

Core Functions:
make_move(i, j, btn): Handles the logic when a player makes a move. It updates the board, changes the button text, and checks for a winner or draw.

check_winner(): Checks if either player has won by aligning three of their marks.

show_popup(message): Displays a popup window with the result (winner or draw).

reset(): Resets the game board to its initial state for a new game.
 
Contributing
Feel free to fork this repository and contribute improvements or bug fixes. If you find any issues or have suggestions, please create an issue or pull request.
  
