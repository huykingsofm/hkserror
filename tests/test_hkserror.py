from hkserror import HTypeError, HKSError
import hkserror

def test_version():
    assert hkserror.__version__ == "0.0.2"

def error():
    a = 7
    raise HTypeError("A", a, float)

def test_htypeerror():
    a = 5
    try:
        error()
    except HKSError as e:
        print(str(e))


def test_hkserror():
    try:
        raise HKSError("huy")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    test_htypeerror()
