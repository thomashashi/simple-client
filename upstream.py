

# At some point this could be dynamic.
# But for now, use the local proxy
def get_listing_addr():
    return 'http://localhost:10002/listing'


def get_product_addr():
    return 'http://localhost:10001/product'