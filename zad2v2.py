import re
import datetime


def check_digits(pesel):
    if re.match('^[0-9]{11}$', str(pesel)):
        return True


def check_length(pesel):
    if len(str(pesel)) == 11:
        return True


def check_birth(pesel):
    pesel = str(pesel)

    year = int(pesel[-11:-9])
    month = int(pesel[-9:-7])
    day = int(pesel[-7:-5])

    if month > 80:
        year += 1800
        month -= 80
    elif month > 60:
        year += 2200
        month -= 60
    elif month > 40:
        year += 2100
        month -= 40
    elif month > 20:
        year += 2000
        month -= 20
    else:
        year += 1900

    now = datetime.date.today()
    birthDate = datetime.date(year, month, day)

    if birthDate > now:
        return False
    else:
        return True


def check_checksum(pesel):
    pesel = str(pesel)
    weights = (9, 7, 3, 1, 9, 7, 3, 1, 9, 7)
    check = sum(w * int(n) for n, w in zip(pesel[-11:-1], weights))
    check = check % 10
    if check == int(pesel[-1]):
        return True


def validate_pesel(number: int) -> bool:
    all_function = [
        check_digits,
        check_length,
        check_birth,
        check_checksum

    ]

    check_pesel = []
    for fn in all_function:
        fn_result = fn(number)
        if fn_result:
            check_pesel.append(fn_result)
        else:
            check_pesel.append(False)
    print(check_pesel)

    if False not in check_pesel:
        return True
    else:
        return False


def test_pesel_is_valid():
    assert validate_pesel(84080574787)
    assert validate_pesel(87032998925)


def test_pesel_is_not_valid():
    assert not validate_pesel(45432101239)
    assert not validate_pesel(15032011239)
    assert not validate_pesel(89120113439)
