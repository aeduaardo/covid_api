from flask import Flask, jsonify
from scraping import Scraping

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

scp = Scraping()


@app.route('/national')
def nationalPanorama():
    return jsonify(scp.nationalPanorama())

@app.route('/world')
def worldPanorama():
    return jsonify(scp.worldPanorama())


if __name__ == '__main__':
    app.run()
