from flask import Flask, render_template
from getdata import GetData

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detik-populer')
def detik_popular():
    html_parser = GetData("https://www.detik.com/terpopuler?", "{'tag_from':'wp_cb_mostPopular_more'}").html_parser()

    popular_area = html_parser.find(attrs={'class': 'grid-row list-content'})
    popular_titles = popular_area.findAll(attrs={'class': 'media__title'})
    popular_images = popular_area.find_all(attrs={'class': 'media__image'})

    return render_template('detik_popular.html', images=popular_images)

@app.route('/idr_rate')
def idr_rate():
    dt_src = GetData("http://www.floatrates.com/daily/idr.json","").doc_req()
    json_data = dt_src.json()

    return render_template('idr_rate.html', json_datas = json_data.values())


if __name__ == '__main__':
    app.run(debug=True)
