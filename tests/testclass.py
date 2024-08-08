class Test:
    def __init__(name, function, args, value):
        self.name = name
        self.function = function
        self.args = args
        self.value = value

def TEST(Tests):
    for test in Tests:
        try:
            val = test.function(test.args)
            assert(val == test.value, f"Returned incorrect value, value should be {test.value}")
            print("=== TEST PASSED ===\nTest {test.name} PASSED.")
            print("FUNCTION: {test.function.__name__}\nARGUMENTS: {test.args}\nRETURNED: {val}\nEXPECTED: {test.value}")
        except Exception as e:
            print("=== TEST FAILED ===\nTest {test.name} FAILED.")
            print("FUNCTION: {test.function.__name__}\nARGUMENTS: {test.args}\nRETURNED: {val}\nEXPECTED: {test.value}")
            print("EXCEPTION: {e}")
