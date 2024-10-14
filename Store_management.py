class Product:
    def __init__(self, product_no, product_name, product_category, product_price):
        self.product_no = product_no
        self.product_name = product_name
        self.product_category = product_category
        self.product_price = product_price
    class Store:
        def __init__(self, store_name, product_list):
            self.store_name = store_name
            self.product_list = product_list
        def categorizeProductsAlphabetically():
            pass