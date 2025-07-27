from flask import Flask, request, render_template
import requests

app = Flask(__name__)
API_KEY = "9ae6894b8f5a41d598e1140cd7d58627"  # Replace with your NewsAPI key

@app.route("/", methods=["GET", "POST"])
def index():
    country = "us"
    headlines = []

    if request.method == "POST":
        country = request.form.get("country")

    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("status") == "ok":
        headlines = data.get("articles")

    return render_template("index.html", articles=headlines, country=country)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
