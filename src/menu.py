""" Code for menu module.
"""

def menu(**kwargs):
    while funct_ := input("Enter Keyword:\n"):
        if funct_ in kwargs.keys():
            print(kwargs[funct_]())
            break
        print(f"'{funct_}' is not a Valid Keyword.")
