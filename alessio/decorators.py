
def count_chars(func):
    def printer(text):
        resp = func(text)
        return f"[{len(resp)} chars] -> {resp}"
    return printer

@count_chars
def say_hello(name):
    return f"Ciao {name}"

print(say_hello("Marco"))