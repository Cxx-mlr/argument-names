from argument_names import argument_names

@argument_names(function=lambda a, b: print(f"{a=}, {b=}"))
def sum(a: int, b: int) -> int:
    return a + b

def test_sum():
    assert True