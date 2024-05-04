from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def picker():
	button_names = ['button1', 'button2', 'button3', 'button4', 'button5']

	if request.method == 'POST':
		# This retrieves which button was pressed
		button_pressed = request.form['action']
		return f"You pressed: {button_pressed}"
	else:
		return render_template('picker.html', prompt="testprompt", button_names=button_names)

@app.route('/answer', methods=['GET', 'POST'])

def answer():
	given_answer = "testanswer"
	links = ['link1', 'link2', 'link3', 'link4', 'link5']

	return render_template('answer.html', Algorithm=given_answer, links=links)



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
