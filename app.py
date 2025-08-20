from flask import Flask, render_template, request, redirect, url_for
from database.game_model import get_games, add_game_to_db, get_game_by_id, update_game_in_db, delete_game_from_db
import os

app = Flask(__name__)

@app.route('/')
def index():
    games = get_games()
    return render_template('index.html', games=games)

@app.route('/add', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        release_year = request.form['release_year']
        add_game_to_db(title, genre, release_year)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_game(id):
    game = get_game_by_id(id)
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        release_year = request.form['release_year']
        update_game_in_db(id, title, genre, release_year)
        return redirect(url_for('index'))
    return render_template('edit.html', game=game)

@app.route('/delete/<int:id>')
def delete_game(id):
    delete_game_from_db(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
