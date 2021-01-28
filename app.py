from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")
  
@app.route("/dashboard/")
def dashboard():
  return render_template("dashboard.html")

@app.route("/map/")
def map():
  return render_template("map.html")

@app.route("/D3/")
def D3():
  return render_template("D3.html")
  
if __name__ == "__main__":
  app.run(debug=True)