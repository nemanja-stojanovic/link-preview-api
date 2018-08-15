from flask import Flask
from flask_cors import CORS
from flask import jsonify
import requests
import bs4

app = Flask(__name__)
CORS(app)

@app.route("/<path:url>", methods=['GET'])
def link_preview(url):
    response = requests.get(url)
    response.raise_for_status()
    page = bs4.BeautifulSoup(response.content, 'lxml')
    meta_descriptions = page.select('meta[name="description"]')
    meta_images = page.select('meta[name="image"]')
    meta_titles = page.select('meta[property="og:title"]')
    if len(meta_descriptions) > 0:
        meta_description = meta_descriptions[0]
        description = meta_description.attrs['content']
    else:
        description = 'N/A'
    if len(meta_images) > 0:
        meta_image = meta_images[0]
        image = meta_image.attrs['content']
    else:
        image = 'N/A'
    if len(meta_titles) > 0:
        meta_title = meta_titles[0]
        title = meta_title.attrs['content']
    else:
        title = 'N/A'
    return jsonify({'description': description, 'image': image, 'title': title})

if __name__ == '__main__':
    app.run()