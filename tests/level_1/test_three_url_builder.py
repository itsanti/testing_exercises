from functions.level_1.three_url_builder import build_url


def test_build_url():
    host_name = 'localhost'
    relative_url = 'about'

    assert build_url(host_name, relative_url) == f'{host_name}/{relative_url}'
    assert build_url('', relative_url) == f'/{relative_url}'
    assert build_url(host_name, '') == f'{host_name}/'
    assert build_url(host_name, relative_url, {'a': 1}) == f'{host_name}/{relative_url}?a=1'
    assert build_url(host_name, '', {'a': 1, 'b': 2}) == f'{host_name}/?a=1&b=2'
