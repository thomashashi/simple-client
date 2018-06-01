from flask import Flask
import requests

app = Flask(__name__)

def get_products():
    products = requests.get('http://product.service.consul')
    print(products.status_code)
    print(products.text)
    return products.json()

def get_listings():
    listings = requests.get('http://listing.service.consul')
    print(listings.status_code)
    print(listings.text)
    return listings.json()

@app.route('/healthz')
def healthz():
    return 'OK'

@app.route('/')
def index():
    return """
    <html>
      <body>
        <h1>Welcome!</h2>
        <h3>Products:</h3>
        <ul>
            {% for prod in get_products() %}
              <li>prod</li>
            {% endfor %}
        </ul>
        <h3>Listings:</h3>
        <ul>
            {% for listing in get_listings() %}
              <li>prod</li>
            {% endfor %}
        </ul>
      </body>
    </html>"""

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
