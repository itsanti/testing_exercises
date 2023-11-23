from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize('купил', 'купила', 'male') == 'купил'
    assert genderalize('купил', 'купила', 'female') == 'купила'
    assert genderalize('купил', 'купила', '222333') == 'купила'
