from flask import Flask, render_template, request, redirect, url_for
from game_data import game_data  # Import the game data from game_data.py

app = Flask(__name__)

# Keep track of the current level
current_level = 0

@app.route('/')
def index():
    # Redirect to the first level
    return redirect(url_for('game_level', level=1))

@app.route('/level/<int:level>', methods=['GET', 'POST'])
def game_level(level):
    global current_level

    if level != current_level + 1:
        return "Please complete the previous level first."

    if request.method == 'POST':
        selected_word = request.form.get('word')
        correct_word = game_data[level - 1]['correct_word']

        if selected_word == correct_word:
            current_level = level
            return "Correct! Good job! You can now proceed to the next level."

        return "Try again. This is not the correct word."

    return render_template('level.html', level_number=level, **game_data[level - 1])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
