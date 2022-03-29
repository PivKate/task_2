from pesel import Pesel


def validate_pesel(number: int) -> bool:
    return Pesel.validate(number)


def test_pesel_is_not_valid():
    assert not validate_pesel(45432101239)
    assert not validate_pesel(15332011239)
    assert not validate_pesel(89120113439)


def test_pesel_is_valid():
    assert validate_pesel(84080574787)
    assert validate_pesel(87032998925)
