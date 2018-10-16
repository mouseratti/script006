from .lab3 import get_russion_cell_phones

fixtures = (
    [
        "+79236765X97",
        "89136645101",
        "83812640423",
        "8(904)541-02-03",
        "+1(555)345-11-21",
        "+8(3812) 360-263",
        "904-333-22-12",
        "9333026455",
        "+7 923 676 5099",
    ],
    [
        "+79136645101",
        "+79045410203",
        "+79043332212",
        "+79333026455",
        "+79236765099",
    ]



)


def test_get_russion_cell_phones():
    assert get_russion_cell_phones(fixtures[0]) == fixtures[1]