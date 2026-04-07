def function():
    value = 100

    def add():
        nonlocal value
        value +=20
        print(value)
    add()

    def subtract():
        nonlocal value
        value -= 50
        print(value)
    subtract()
function()