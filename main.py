from flask import Flask
import random
app = Flask(__name__)
RANDOM_NUMBER = random.randint(1, 9)

print(RANDOM_NUMBER)


@app.route('/')
def home():
    return '<h1> Guess a number between 0 and 9 </h1><img src="https://media.giphy.com/media/l378khQxt68syiWJy/giphy.gif" ' \
           'alt="number between 1 and 9" width="500" height="600">'


@app.route("/<int:number>")
def guess(number):
    if number == RANDOM_NUMBER:
        return "<h1> You Win!! </h1>"
    elif number > RANDOM_NUMBER:
        return "<h1> Too High </h1>"
    else:
        return "<h1> Too Low </h1>"






if __name__ == "__main__":
    app.run(debug=True)