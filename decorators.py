def logtime(func):
    def wrapper():
        print("antes")
        val = func()
        print("depois")
        return val
    return wrapper

@logtime
def hello():
    print("hello")

hello()