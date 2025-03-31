
# Tris AI

An AI that learns by playing! This AI knows the basic moves of the game, how to win and how not to let you win, but it doesn't know the techniques, which is why it has been given a memory, so each encounter will make it stronger!

## How it work?
The logic is simple. The first move of the AI is random in order to have somewhat varied matches. Afterwards, the AI will check the moves made in the game, and will look in its diagrams for a winning game that matches the current one and go to repeat it. If there are no archived won games it will check the lost ones, and choose a move at random from those available, excluding those that led to a defeat!

## How con i use it?
### Online free version
You can use it from my site for free, but note that it is already trained: https://ilnonop.odoo.com/games/tris-ia. The site will be available from 5 to 11 UTC time

### Download
You have two options for downloading
- CLI version
- GUI (web server)
  
**CLI version:** If you want to use the CLI version, all you have to do is download main.py and whoila! That's it!

**WEB version:** Need flask to work. Download the web-app.py script and start it, then connect to 127.0.1:5000 and play!

**Download pre-trained template:** To download the pre-trained files go to the "ia-data" folder of this repository, download them and put them in the "ia-data" folder on your computer in the same directory as the script

## Other
That's it! Enjoy the game! If you notice any problems please signal!
