
##############
#My Functions#
##############

def get_from_repository(repository: str, get: str) -> "":
    start = repository.find(get)
    end = repository[start+1:].find("\n"*3)+1+start
    return (repository[start:end])


def hello():
    print("Hello World")


def how():
    print("How are you?")


def some_def():
    print("-"*30)
    print("Some random function")
    print("-"*30)


