from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "It's alive!"

@app.route('/home2/')
def home2():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['height'] = request.args.get('height')
    kwargs['color'] = request.args.get('color')
    return render_template('chapter_9.html', **kwargs)

app.run(port=5000, debug=True)

# http://localhost:5000/home2/?color=red&thing=eat&height=200
