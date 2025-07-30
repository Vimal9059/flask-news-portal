from flask import Flask, render_template, request
import feedparser
import requests

app = Flask(__name__)

RSS_FEEDS = {
    'us': 'https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en',
    'in': 'https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en',
    'ca': 'https://news.google.com/rss?hl=en-CA&gl=CA&ceid=CA:en',
    'gb': 'https://news.google.com/rss?hl=en-GB&gl=GB&ceid=GB:en',
    'sg': 'https://news.google.com/rss?hl=en-SG&gl=SG&ceid=SG:en',
    'nz': 'https://news.google.com/rss?hl=en-NZ&gl=NZ&ceid=NZ:en',
}


def update_noip_dns():
    import requests

    public_ip = requests.get("https://ifconfig.me/ip").text.strip()
    headers = {
        "Authorization": "Basic bG9ob3hlNTQ1NkAwdGlyZXMuY29tOlZpbWFsQDEyMw==",
        "User-Agent": "topglobalnews-updater/1.0 (by Vimal)"
    }
    url = f"https://dynupdate.no-ip.com/nic/update?hostname=topglobalnews.zapto.org&myip={public_ip}"
    response = requests.get(url, headers=headers)
    return response.text

@app.route('/')
def home():
    country = request.args.get('country', 'us')
    feed = feedparser.parse(RSS_FEEDS.get(country, RSS_FEEDS['us']))
    articles = feed.entries
    return render_template('index.html', articles=articles, country=country)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
