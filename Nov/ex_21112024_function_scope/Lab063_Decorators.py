
def add_before_ui_After_ui (func):
    def wrapper():
        print ("Before running the UI TC")
        print ("start the browser")
        func()
        print ("End the UI Test case run")
        print ("Quit the browser")
    return wrapper()


@add_before_ui_After_ui
def test_ui():
    print(" >>> I will test the UI")