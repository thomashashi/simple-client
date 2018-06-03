from flask import Flask
from flask import render_template
import requests
import upstream

app = Flask(__name__)

def get_products():
    products = requests.get(upstream.get_product_addr())
    print(products.status_code)
    print(products.text)
    return products.json()

def get_listings():
    listings = requests.get(upstream.get_product_addr())
    print(listings.status_code)
    print(listings.text)
    return listings.json()

@app.route('/healthz')
def healthz():
    return 'OK'

template = """<html>
      <body>
        <h1>Welcome!</h2>
        <h3>Products:</h3>
        <ul>
            {% for prod in prod_list %}
              <li>prod</li>
            {% endfor %}
        </ul>
        <h3>Listings:</h3>
        <ul>
            {% for listing in listings_list %}
              <li>prod</li>
            {% endfor %}
        </ul>
      </body>
    </html>
"""

@app.route('/')
def index():
    products = get_products()
    listings = get_listings()
    return render_template(template, prod_list=products, listings_list=listings)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
