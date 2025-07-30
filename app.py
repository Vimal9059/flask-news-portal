from flask import Flask, render_template, requests
import feedparser

app = Flask(__name__)

RSS_FEEDS = {
    'us': 'https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en',
    'in': 'https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en',
    'ca': 'https://news.google.com/rss?hl=en-CA&gl=CA&ceid=CA:en',
    'gb': 'https://news.google.com/rss?hl=en-GB&gl=GB&ceid=GB:en',
    'sg': 'https://news.google.com/rss?hl=en-SG&gl=SG&ceid=SG:en'
}

@app.route('/')
def home():
    country = request.args.get('country', 'us')
    feed = feedparser.parse(RSS_FEEDS.get(country, RSS_FEEDS['us']))
    articles = feed.entries
    return render_template('index.html', articles=articles, country=country)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
