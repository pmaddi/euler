def ham(n, m):
    return 1


def test_ham():
    assert ham(5, 10**8) == 1105


if __name__ == '__main__':
    print(ham(100, 10**9))
