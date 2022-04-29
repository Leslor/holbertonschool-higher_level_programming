#!/usr/bin/python3


if __name__ == "__main__":
    """program that prints all the names
    defined by the compiled module hidden_4.pyc """
    import hidden_4
    list_d = [i for i in dir(hidden_4) if i[:2] != "__"]
    print("\n".join(map(str, list_d)))
    # print("\n".join(list_d))
