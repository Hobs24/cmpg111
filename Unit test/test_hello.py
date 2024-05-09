from hello import hello

#(==) here looking to test a return value from hello() function
def test_hello():
    hello("Saul") == "hello, Saul"