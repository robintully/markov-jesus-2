from flask import Flask,render_template
from flask_bootstrap import Bootstrap
import markovify
import random
from large_jesus import large_jesus_set

with open("whole_bible.txt") as f:
    text = f.read()
text_model = markovify.Text(text)

app = Flask(__name__)
Bootstrap(app)



@app.route('/')
def index():
    message = text_model.make_short_sentence(140)
    jesus = random.choice(large_jesus_set)
    return render_template('large-jesus.html', message=message, jesus=jesus )

if __name__ == '__main__':
    app.run(debug=True)
