import os
import random
import uuid
import time
import threading
import requests
from flask import Flask, render_template_string, request, redirect, url_for, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = "s3cr3t_key"

games = {}

# Funzione helper per registrare il risultato in un file
def log_result(file_path, game_moves):
    try:
        with open(file_path, "r") as file:
            data = file.readlines()
    except Exception:
        data = []
    trovato = False
    nuova_lista = []
    for ln in data:
        campi = ln.strip().split("|")
        if len(campi) == 3 and (campi[0] + "|" + campi[1] == game_moves):
            n = int(campi[2]) + 1
            nuova_lista.append(game_moves + "|" + str(n) + "\n")
            trovato = True
        else:
            nuova_lista.append(ln)
    if not trovato:
        nuova_lista.append(game_moves + "|1\n")
    with open(file_path, "w") as file:
        file.writelines(nuova_lista)

# Classe che incapsula lo stato della partita
class Game:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_score = 0
        self.ai_score = 0
        self.draw_score = 0
        self.reset_round(new_game=True)
        self.turn_precedente = self.turn

    def reset_round(self, new_game=False):
        # Inizializza la board (array di 10 elementi, indice 0 ignorato)
        self.board = [str(i) for i in range(10)]
        # Determina casualmente il turno iniziale ("0" = giocatore, "1" = IA)
        if new_game:
            self.turn = random.choice(["0", "1"])
        else:
            self.turn = "0" if self.turn_precedente == "1" else "1"
            self.turn_precedente = self.turn
        self.moves = self.turn + "|"
        self.turn_count = 0
        self.victory = False
        self.winner = None

    def check_victory(self):
        b = self.board
        if b[1] == b[2] == b[3]:
            self.victory = True
            self.winner = b[1]
        elif b[4] == b[5] == b[6]:
            self.victory = True
            self.winner = b[4]
        elif b[7] == b[8] == b[9]:
            self.victory = True
            self.winner = b[7]
        elif b[1] == b[4] == b[7]:
            self.victory = True
            self.winner = b[1]
        elif b[2] == b[5] == b[8]:
            self.victory = True
            self.winner = b[2]
        elif b[3] == b[6] == b[9]:
            self.victory = True
            self.winner = b[3]
        elif b[1] == b[5] == b[9]:
            self.victory = True
            self.winner = b[1]
        elif b[3] == b[5] == b[7]:
            self.victory = True
            self.winner = b[3]
        self.turn_count += 1
        if self.turn_count == 9 and not self.victory:
            self.victory = True
            self.winner = None  # Pareggio
        return self.victory

    def make_move(self, move, player):
        marker = "X" if player == "player" else "O"
        if self.board[move] == str(move):
            self.board[move] = marker
            self.moves += str(move)
            self.turn = "1" if self.turn == "0" else "0"
            return True
        return False

    def ai_move(self):
        # Logica per l'IA (ispirata al codice originale)
        partita = self.moves
        migliore = "0|0|0"
        mossa = "0"
        b = self.board
        if self.turn_count == 0:
            mosse_possibili = [str(i) for i in range(1, 10)]
            mossa = random.choice(mosse_possibili)
            return int(mossa)
        # Prova a fare punto
        if b[1] == b[2] and b[3] == "3" and b[1] == "O":
            mossa = "3"
        elif b[2] == b[3] and b[1] == "1" and b[2] == "O":
            mossa = "1"
        elif b[3] == b[1] and b[2] == "2" and b[3] == "O":
            mossa = "2"
        if b[4] == b[5] and b[6] == "6" and b[4] == "O":
            mossa = "6"
        elif b[5] == b[6] and b[4] == "4" and b[5] == "O":
            mossa = "4"
        elif b[4] == b[6] and b[5] == "5" and b[6] == "O":
            mossa = "5"
        if b[7] == b[8] and b[9] == "9" and b[7] == "O":
            mossa = "9"
        elif b[8] == b[9] and b[7] == "7" and b[8] == "O":
            mossa = "7"
        elif b[7] == b[9] and b[8] == "8" and b[9] == "O":
            mossa = "8"
        if b[1] == b[4] and b[7] == "7" and b[1] == "O":
            mossa = "7"
        elif b[4] == b[7] and b[1] == "1" and b[4] == "O":
            mossa = "1"
        elif b[1] == b[7] and b[4] == "4" and b[1] == "O":
            mossa = "4"
        if b[2] == b[5] and b[8] == "8" and b[2] == "O":
            mossa = "8"
        elif b[5] == b[8] and b[2] == "2" and b[5] == "O":
            mossa = "2"
        elif b[2] == b[8] and b[5] == "5" and b[2] == "O":
            mossa = "5"
        if b[3] == b[6] and b[9] == "9" and b[3] == "O":
            mossa = "9"
        elif b[6] == b[9] and b[3] == "3" and b[6] == "O":
            mossa = "3"
        elif b[3] == b[9] and b[6] == "6" and b[3] == "O":
            mossa = "6"
        if b[1] == b[5] and b[9] == "9" and b[1] == "O":
            mossa = "9"
        elif b[5] == b[9] and b[1] == "1" and b[5] == "O":
            mossa = "1"
        elif b[1] == b[9] and b[5] == "5" and b[1] == "O":
            mossa = "5"
        if b[3] == b[5] and b[7] == "7" and b[3] == "O":
            mossa = "7"
        elif b[5] == b[7] and b[3] == "3" and b[5] == "O":
            mossa = "3"
        elif b[3] == b[7] and b[5] == "5" and b[3] == "O":
            mossa = "5"
        if mossa != "0":
            return int(mossa)
        # Se non trova mosse vincenti, prova a bloccare
        if mossa == "0":
            if b[1] == b[2] and b[3] == "3":
                mossa = "3"
            elif b[2] == b[3] and b[1] == "1":
                mossa = "1"
            elif b[3] == b[1] and b[2] == "2":
                mossa = "2"
            if b[4] == b[5] and b[6] == "6":
                mossa = "6"
            elif b[5] == b[6] and b[4] == "4":
                mossa = "4"
            elif b[4] == b[6] and b[5] == "5":
                mossa = "5"
            if b[7] == b[8] and b[9] == "9":
                mossa = "9"
            elif b[8] == b[9] and b[7] == "7":
                mossa = "7"
            elif b[7] == b[9] and b[8] == "8":
                mossa = "8"
            if b[1] == b[4] and b[7] == "7":
                mossa = "7"
            elif b[4] == b[7] and b[1] == "1":
                mossa = "1"
            elif b[1] == b[7] and b[4] == "4":
                mossa = "4"
            if b[2] == b[5] and b[8] == "8":
                mossa = "8"
            elif b[5] == b[8] and b[2] == "2":
                mossa = "2"
            elif b[2] == b[8] and b[5] == "5":
                mossa = "5"
            if b[3] == b[6] and b[9] == "9":
                mossa = "9"
            elif b[6] == b[9] and b[3] == "3":
                mossa = "3"
            elif b[3] == b[9] and b[6] == "6":
                mossa = "6"
            if b[1] == b[5] and b[9] == "9":
                mossa = "9"
            elif b[5] == b[9] and b[1] == "1":
                mossa = "1"
            elif b[1] == b[9] and b[5] == "5":
                mossa = "5"
            if b[3] == b[5] and b[7] == "7":
                mossa = "7"
            elif b[5] == b[7] and b[3] == "3":
                mossa = "3"
            elif b[3] == b[7] and b[5] == "5":
                mossa = "5"
        if mossa != "0":
            return int(mossa)
        try:
            with open("./ia_data/win.txt", "r") as file:
                for ln in file:
                    if ln.startswith(partita):
                        parts = ln.strip().split("|")
                        if len(parts) >= 3 and int(parts[2]) > int(migliore.split("|")[2]):
                            migliore = ln.strip()
        except:
            pass
        mossa = migliore.replace(partita, "")[0] if migliore != "0|0|0" else "0"
        if mossa != "0":
            return int(mossa)
        if mossa == "0":
            mosse_possibili = [str(i) for i in range(1, 10) if b[i] == str(i)]
            try:
                with open("./ia_data/lose.txt", "r") as file:
                    for ln in file:
                        if ln.startswith(partita):
                            da_rimuovere = ln.replace(partita, "")[0]
                            if da_rimuovere in mosse_possibili:
                                mosse_possibili.remove(da_rimuovere)
            except:
                pass
            if not mosse_possibili:
                mosse_possibili = [str(i) for i in range(1, 10) if b[i] == str(i)]
            mossa = random.choice(mosse_possibili)
        return int(mossa)

# Template per la pagina iniziale (nuova partita)
index_template = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Tic Tac Toe - Nuova Partita</title>
    <style>
      body { text-align: center; font-family: Arial, sans-serif; }
      input[type="text"] { font-size: 1.2em; padding: 5px; }
      input[type="submit"] { font-size: 1.2em; padding: 5px 10px; }
    </style>
  </head>
  <body>
    <h1>Benvenuto a Tic Tac Toe!</h1>
    <form action="{{ url_for('new_game') }}" method="post">
      Inserisci il tuo nome: <input type="text" name="player_name" required>
      <input type="submit" value="Nuova Partita">
    </form>
  </body>
</html>
"""

# Template per la pagina di gioco
game_template = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Tic Tac Toe - Gioco</title>
    <style>
      body { text-align: center; font-family: Arial, sans-serif; }
      table { width: 100%; max-width: 400px; margin: auto; border-collapse: collapse; table-layout: fixed; }
      td { border: 1px solid #333; height: 100px; font-size: 2em; vertical-align: middle; }
      form { margin: 0; padding: 0; }
      button { display: block; width: 100%; height: 100%; padding: 0; margin: 0; font-size: inherit; border: none; background: none; cursor: pointer; }
      .error { color: red; font-weight: bold; }
    </style>
  </head>
  <body>
    <h1>Tic Tac Toe - {{ game.player_name }}</h1>
    <p>{{ game.player_name }}: {{ game.player_score }} | IA: {{ game.ai_score }} | Pareggi: {{ game.draw_score }}</p>
    <p>Turno: {% if game.turn == "0" %}{{ game.player_name }}{% else %}IA{% endif %}</p>
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <div class="error">
          {% for message in messages %}
            <p>{{ message }}</p>
          {% endfor %}
        </div>
      {% endif %}
    {% endwith %}
    <table>
      {% for row in [0,1,2] %}
      <tr>
        {% for col in [0,1,2] %}
          {% set pos = row * 3 + col + 1 %}
          <td>
            {% if game.board[pos] == pos|string and game.turn == "0" and not game.victory %}
              <form action="{{ url_for('make_move', game_id=game_id) }}" method="post">
                <input type="hidden" name="move" value="{{ pos }}">
                <button type="submit">&nbsp;</button>
              </form>
            {% else %}
              {{ game.board[pos] if game.board[pos] in ['X','O'] else '' }}
            {% endif %}
          </td>
        {% endfor %}
      </tr>
      {% endfor %}
    </table>
    {% if game.victory %}
      {% if game.winner == "X" %}
        <h2>{{ game.player_name }} vince!</h2>
      {% elif game.winner == "O" %}
        <h2>IA vince!</h2>
      {% else %}
        <h2>Pareggio!</h2>
      {% endif %}
      <form action="{{ url_for('new_round', game_id=game_id) }}" method="post">
        <input type="submit" value="Nuova Partita">
      </form>
    {% endif %}
    {% if game.turn == "1" and not game.victory %}
      <script>
        setTimeout(function(){
           window.location.href = "{{ url_for('ai_move_route', game_id=game_id) }}";
        }, 500);
      </script>
    {% endif %}
  </body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(index_template)

@app.route("/new_game", methods=["POST"])
def new_game():
    player_name = request.form.get("player_name")
    game_id = str(uuid.uuid4())
    game = Game(player_name)
    games[game_id] = game
    if game.turn == "1":
        time.sleep(0.5)
        ai_move = game.ai_move()
        game.make_move(ai_move, "ai")
        game.check_victory()
    return redirect(url_for("game_page", game_id=game_id))

@app.route("/game/<game_id>")
def game_page(game_id):
    game = games.get(game_id)
    if not game:
        return "Partita non trovata", 404
    return render_template_string(game_template, game=game, game_id=game_id)

@app.route("/game/<game_id>/move", methods=["POST"])
def make_move(game_id):
    game = games.get(game_id)
    if not game:
        return "Partita non trovata", 404
    if game.victory:
        return redirect(url_for("game_page", game_id=game_id))
    move_str = request.form.get("move")
    if not move_str or not move_str.isdigit():
        flash("Mossa non valida: devi selezionare una casella!")
        return redirect(url_for("game_page", game_id=game_id))

    move = int(move_str)
    if move < 1 or move > 9 or game.board[move] not in [str(move), move]:
        flash("Mossa non valida!")
        return redirect(url_for("game_page", game_id=game_id))

    game.make_move(move, "player")
    game.check_victory()
    if game.victory:
        if game.winner == "X":
            game.player_score += 1
            # Quando vince il giocatore, registra la sconfitta dell'IA in lose.txt
            log_result("./ia_data/lose.txt", game.moves)
        elif game.winner is None:
            game.draw_score += 1
    return redirect(url_for("game_page", game_id=game_id))

@app.route("/game/<game_id>/ai_move")
def ai_move_route(game_id):
    game = games.get(game_id)
    if not game:
        return "Partita non trovata", 404
    if not game.victory and game.turn == "1":
        time.sleep(0.5)
        ai_move = game.ai_move()
        game.make_move(ai_move, "ai")
        game.check_victory()
        if game.victory:
            if game.winner == "X":
                game.player_score += 1
                log_result("./ia_data/lose.txt", game.moves)
            elif game.winner == "O":
                game.ai_score += 1
                log_result("./ia_data/win.txt", game.moves)
            else:
                game.draw_score += 1
    return redirect(url_for("game_page", game_id=game_id))

@app.route("/game/<game_id>/new_round", methods=["POST"])
def new_round(game_id):
    game = games.get(game_id)
    if not game:
        return "Partita non trovata", 404
    game.reset_round(new_game=False)
    if game.turn == "1":
        time.sleep(0.5)
        ai_move = game.ai_move()
        game.make_move(ai_move, "ai")
        game.check_victory()
    return redirect(url_for("game_page", game_id=game_id))

# Funzione per eseguire una richiesta GET ogni 5 minuti
def ping():
    while True:
        try:
            requests.get("https://hc-ping.com/0732949d-243a-4029-b20f-aacb11f9125d")
        except Exception as e:
            print("Ping fallito:", e)
        time.sleep(300)

if __name__ == "__main__":
    ping_thread = threading.Thread(target=ping, daemon=True)
    ping_thread.start()
    app.run(debug=True, host="0.0.0.0")
