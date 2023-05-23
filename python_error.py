def test_exception(num):
    try:
        print("try...")
        r = 10 / num
        print("result:", r)
    except RuntimeError as e:
        print("except:", e)
    else:
        print("else...")
    finally:
        print("finally...")
    print("END")
    
def test_raise_exception():
    try:
        raise RuntimeError("my error")
    except RuntimeError as e:
        print("RuntimeError")
    finally:
        print("finally...")
    print("END")


test_exception(1)
test_raise_exception()