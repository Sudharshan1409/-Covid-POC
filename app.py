from flask import Flask,render_template

app=Flask(__name__)

from project_part_1 import part1
from project_part_2 import part2
from project_part_3 import part3

app.register_blueprint(part1)
app.register_blueprint(part2)
app.register_blueprint(part3)

@app.route('/')
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True, port=3000)