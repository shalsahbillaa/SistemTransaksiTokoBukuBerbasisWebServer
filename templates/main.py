from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
	return redirect("https://www.youtube.com/watch?v=0toekpcePH4")

if __name__ == "__main__":
	app.run(debug = True)