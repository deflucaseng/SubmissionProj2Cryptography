from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def home():
	button_names = ['button1', 'button2', 'button3', 'button4', 'button5']

	if request.method == 'POST':
		# This retrieves which button was pressed
		button_pressed = request.form['action']
		return f"You pressed: {button_pressed}"
	else:
		return render_template('picker.html', prompt="testprompt", button_names=button_names)





if __name__ == '__main__':
    app.run(debug=True)
