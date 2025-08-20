from database.connection import create_connection

def get_games():
    client = create_connection()
    rows = client.execute("SELECT id, title, genre, release_year FROM Juego")
    client.close()
    return [{'id': r[0], 'title': r[1], 'genre': r[2], 'release_year': r[3]} for r in rows]

def add_game_to_db(title, genre, release_year):
    client = create_connection()
    client.execute(
        "INSERT INTO Juego (title, genre, release_year) VALUES (?, ?, ?)",
        (title, genre, release_year)
    )
    client.close()

def get_game_by_id(game_id):
    client = create_connection()
    rows = client.execute(
        "SELECT id, title, genre, release_year FROM Juego WHERE id = ?",
        (game_id,)
    )
    client.close()
    if rows:
        r = rows[0]
        return {'id': r[0], 'title': r[1], 'genre': r[2], 'release_year': r[3]}
    return None

def update_game_in_db(game_id, title, genre, release_year):
    client = create_connection()
    client.execute(
        "UPDATE Juego SET title = ?, genre = ?, release_year = ? WHERE id = ?",
        (title, genre, release_year, game_id)
    )
    client.close()

def delete_game_from_db(game_id):
    client = create_connection()
    client.execute(
        "DELETE FROM Juego WHERE id = ?",
        (game_id,)
    )
    client.close()
