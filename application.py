from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route('/')
def receiver():
    return render_template('receiver.html')

@app.route('/sender')
def sender():
	return render_template('sender.html')

if __name__ == '__main__':
    app.run()
else:
	application = app