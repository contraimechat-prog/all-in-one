import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    if x <= 0:
        return 0
    if x > 0:
        return x


def ELU(x, a):
    if x <= 0:
        return a * (math.exp(x) - 1)
    else:
        return x


def is_number(x):
    try:
        float(x)

    except ValueError:
        return False
    return True


def check_function(func_name):

    function_name = ["sigmoid", "relu", "elu"]
    if func_name not in function_name:
        return print("ten_function_user khong hop le")


def activate_function():
    x = float(input("Nhap so x"))
    func = input("nhap ten function")
    is_number(x)
    check_function(func)
    if func == "sigmoid":
        print(f"sigmoid: f({x}) = {sigmoid(x)} ")

    if func == "relu":
        print(f"relu: f({x}) = {relu(x)} ")

    if func == "elu":
        print(f"elu: f({x}) = {ELU(x)} ")


activate_function()
