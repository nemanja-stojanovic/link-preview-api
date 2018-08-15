from flask import Flask
from flask import jsonify
import requests
import bs4

app = Flask(__name__)

@app.route("/link_preview/<path:url>", methods=['GET'])
def link_preview(url):
    response = requests.get(url)
    response.raise_for_status()
    page = bs4.BeautifulSoup(response.content, 'lxml')
    meta_descriptions = page.select('meta[name="description"]')
    content = None
    if len(meta_descriptions) > 0:
        meta_description = meta_descriptions[0]
        content = meta_description.attrs['content']
    else:
        content = 'N/A'
    return jsonify({'description': content})

if __name__ == '__main__':
    app.run()