class BaseChai:
    def __init__(self,type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai.....")

# here the MasalaChai is inherited through basechai 
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamon, ginger, cloves.")

# this is composition as chai_cls is used in chai_shop
class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancychaiShop(ChaiShop):
    chai_cls = MasalaChai 

shop = ChaiShop()
fancy = FancychaiShop()

fancy.serve()
shop.serve()
fancy.chai.add_spices()
fancy.chai_cls.add_spices(fancy.chai)



