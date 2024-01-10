
##############
#My Functions#
##############

def get_from_repository(R: str, func_definition: str) -> "":
    start = R.find(func_definition)
    end = R[start+1:].find("\n"*3)+1+start
    return (R[start:end])


def hello():
    print("Hello World")


def how():
    print("How are you?")


def some_def():
    print("-"*30)
    print("Some random function")
    print("-"*30)


