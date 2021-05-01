from hkserror import HTypeError, HKSError

def test_htypeerror():
    a = 5
    try:
        raise HTypeError("a", a, float, None)
    except HKSError as e:
        print(e)


def test_hkserror():
    try:
        raise HKSError("huy")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    test_hkserror()
