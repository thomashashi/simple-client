import os

def get_listing_addr():
    return "{0}/listing".format(os.getenv('LISTING_URI','http://localhost:10002'))


def get_product_addr():
    return "{0}/product".format(os.getenv('PRODUCT_URI', 'http://localhost:10001'))
