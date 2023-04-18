from potantial import Potantial

def assertListEqual(list1:list, list2:list) -> bool:
    return len(list1) == len(list2) and all([a == b for a, b in zip(sorted(list1), sorted(list2))])

def test_Potantials():
    assert assertListEqual(Potantial("10000000146").potantials, ["10000000146"])
    assert assertListEqual(Potantial("1000000146").potantials, ["10000000146"])
    assert assertListEqual(Potantial("1000000014").potantials, ["10000000146", "10000020014", "10002000014", "10200000014", "10000000214"])
    assert assertListEqual(Potantial("1000000014645").potantials, ["10000000146"])
    assert assertListEqual(Potantial("10007500000146").potantials, ["10750000014", "10000000146", "10007500014"])
    assert assertListEqual(Potantial("1a0B0/00000146").potantials, ["10000000146"])
    assert assertListEqual(Potantial("10000001146").potantials, [])

test_Potantials()