chai_type = "Plain"

def front_desk():
    chai_type = "Masala"

    def kitchen():
        global chai_type
        chai_type = "Irani"
    kitchen()
    print("At front desk: ", chai_type)


front_desk()
print("Final global chai: ", chai_type)