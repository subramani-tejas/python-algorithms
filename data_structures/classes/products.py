from webbrowser import get


class Product:
    def __init__(self, price) -> None:
        self.price = price

    # if we need validation of data we can use
    # gett/setter func and add setter above - where data validation logic is
    # this is 'unpythonic'; something a java programmer would write
    # def get_price(self):
    #     return self.__price

    # def set_price(self, price):
    #     if price < 0:
    #         raise ValueError("Price can't be negative!")
    #     self.__price = price

    #  ##########
    # getter equivalent (if no setter, treat like read only property)
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price can't be negative!")
        self.__price = price

    # in python use property
    # price = property(get_price, set_price)


mouse = Product(10.99)
# mouse.set_price(11.99)
print(f"Mouse price: ${mouse.price}")
