import crypto


def test():
    password = ""
    if not password:
        return 3
    if password != crypto.unencrypt(""):
        return 1
    return 2


print(test())