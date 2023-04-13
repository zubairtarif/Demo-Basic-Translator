from flask import Flask, render_template, request, flash
import translators as ts

app = Flask(__name__)
app.secret_key = "abc"

@app.route("/")
def translate():
	welcome_message = "Enter Your translation prompt"
	return render_template("index.html", welcome = welcome_message, prompt="", message ="") #because we saved an index file udner templates folder, flask will be able to find it

@app.route("/Translation", methods=["POST", "GET"])#this should be same as the action specified in html
def translation(): 
	input_text = request.form['name_input']

	translated = ts.translate_text(input_text, translator='bing', to_language='en')
	return render_template("index.html",welcome = "", prompt=input_text, message =translated)

if __name__ == "__main__":
	print("**** Flask server is starting. This message is shown in terminal. ****\n")
	app.run(port=7200)