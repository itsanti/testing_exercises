from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    text = 'ldsflsdf ldsfl sdlf sdf'

    assert change_copy_item('', 7) == ''
    assert change_copy_item('abc', 7) == 'abc'

    assert change_copy_item('abc', 20) == f'Copy of abc'

    assert change_copy_item('ldsflsdf ldsfl sdlf sdf') == f'Copy of {text}'
    assert change_copy_item(f'Copy of {text}') == f'Copy of {text} (2)'
    assert change_copy_item(f'Copy of {text} (2)') == f'Copy of {text} (3)'
