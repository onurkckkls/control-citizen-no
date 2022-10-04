from citizenNo import CitizenNo


def test_CitizenNo():
    assert CitizenNo.control("10000000146") == True
    assert CitizenNo.control(10000000146) == True
    assert CitizenNo.control("11111111110 ") == True
    assert CitizenNo.control("11111111110a") == False
    assert CitizenNo.control("11111a11110") == False
    assert CitizenNo.control("01111111110") == False
    assert CitizenNo.multiControl("10000000146", 11111111110) == [True, True]
    assert CitizenNo.multiControl("10000000146", 11111111110, 11111111111) == [
        True,
        True,
        False,
    ]


test_CitizenNo()
