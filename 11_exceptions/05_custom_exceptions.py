def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichai"]:
        raise ValueError("Unsupported chai flavor...")
    print(f"brewing {flavor} chai...")


brew_chai("mint")

class OutOfIngredientsError(Exception):
    pass

def make_chai(milk,sugar):
    if milk ==0 or sugar ==0:
        raise OutOfIngredientsError("Cannot make chai without milk or sugar")
    print("making chai...")

make_chai(1,0)