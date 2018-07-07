import json
import pickle
import os
import sqlite3
from abc import *


class DBConn(metaclass=ABCMeta):

    def dbconn(self):

        conn = sqlite3.connect('inventory.db')
        c = conn.cursor()
        return c, conn


class Product(DBConn):

    def __init__(self, p_id, prod_name, price, quantity):
        self.id = p_id
        self.price = price
        self.prod_name = prod_name
        self.quantity = quantity

        self.prod_dict = {}
        self.items = {}

    def add_product(self):
        self.prod_dict.setdefault('prod_name', None)
        self.prod_dict.setdefault('price', None)
        self.prod_dict.setdefault('quantity', None)

        self.prod_dict["prod_name"] = self.price
        self.prod_dict["price"] = self.price
        self.prod_dict["quantity"] = self.quantity

        self.items[self.id] = self.prod_dict

    def view_product(self):
        return self.prod_dict

    def view_items(self):
        return self.items

    def save_product(self):
        db, save = super(Product, self).dbconn()
        try:
            with open('data.json', 'r+') as outfile:
                inventory = json.load(outfile)
                inventory.update(self.items)
                outfile.seek(0)
                outfile.truncate()
                json.dump(inventory, outfile)

                db.execute("INSERT INTO inventories (id, product_name, price, quantity) VALUES (?,?,?,?)",
                           (self.id, self.prod_name, self.price, self.quantity))

                save.commit()

        except ValueError:

            if os.stat("data.json").st_size == 0:
                with open('data.json', 'w') as outfile:
                    json.dump(self.items, outfile)
            else:
                print("Operation could not be performed.Make sure you have a valid Json or DB file")

        finally:
            save.close()

        with open('total_dictionary.pickle', 'wb') as handle:
            pickle.dump(self.prod_dict, handle)


class Inventory(DBConn):

    def __init__(self):
        pass

    def get_product(self, p_id):

        select = (p_id,)
        with open('data.json', 'rb') as f:
            product = json.load(f)

        db, save = super(Inventory, self).dbconn()

        db.execute("SELECT * FROM inventories WHERE id =?", select)

        print ("Selected id from DB ", db.fetchone())

        print("Product id from json file: ", product[p_id])

        save.close()

    def get_products(self):
        db, save = super(Inventory, self).dbconn()

        db.execute('SELECT * FROM inventories')

        print ("Our inventory list from DB: ", db.fetchall())

        save.close()

    def inv_value(self, product):
        value = 0
        worth = 0

        with open('data.json', 'rb') as f:
            products = json.load(f)

            for prod in products.keys():
                value += float(products[prod]["price"])

        db, save = super(Inventory, self).dbconn()

        def prod_value(prod):
            prod_name = (prod, )
            db.execute('SELECT price FROM inventories WHERE product_name =?', prod_name)

            product_value = [float(prod_val[0]) for prod_val in db.fetchall()]
            print("product value", sum(product_value))

        if product:
            prod_value(product)

        query = db.execute('SELECT price FROM inventories')

        for price in query.fetchall():
            item = float(price[0])
            worth += item

        save.close()

        print("Our inventory worth is ", worth)

        return "The value of our inventory is {} CAD".format(value)


if __name__ == "__main__":

    new_product = Product("1", "milk", "50.00", "10")
    new_product.add_product()
    print(new_product.view_product())
    print(new_product.view_items())
    new_product.save_product()

    new_product1 = Product("2", "egg", "30.00", "20")
    new_product1.add_product()
    print(new_product1.view_product())
    new_product1.save_product()

    user = Inventory()
    user.get_product("1")
    user.get_products()
    print(user.inv_value("milk"))
