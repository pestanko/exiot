from exiot import dict_get, dict_set, dict_rec_subst, obj_get_props_dict


def test_dict_set_single_level():
    result = dict_set({}, "hello", "world")
    assert result["hello"] == "world"


def test_dict_set_two_levels():
    result = dict_set({}, "foo.bar", "world")
    assert result["foo"]['bar'] == "world"


def test_dict_get_single_level():
    d = {'hello': 'world'}
    result = dict_get(d, 'hello')
    assert result == "world"


def test_dict_get_two_level():
    d = {'hello': {'world': 'everyone'}}
    result = dict_get(d, 'hello.world')
    assert result == "everyone"


def test_dict_get_list_level():
    d = {'hello': {'world': 'everyone'}}
    result = dict_get(d, ['hello', 'world'])
    assert result == "everyone"


def test_dict_get_non_existing():
    d = {'hello': {'world': 'everyone'}}
    result = dict_get(d, 'hello.snitzel')
    assert result is None


def test_dict_get_non_existing_single():
    d = {'hello': {'world': 'everyone'}}
    result = dict_get(d, 'snitzel')
    assert result is None
    result = dict_get(d, 'snitzel', default='nitzel')
    assert result is 'nitzel'


def test_dict_get_key_none():
    d = {'hello': {'world': 'everyone'}}
    result = dict_get(d, None)
    assert result is d


def test_custom_template_simple():
    d = {
        'api': 'api.example.com',
        'api_url': 'https://${api}/path',
        'hello': 1,
        'world': '${hello}'
    }
    result = dict_rec_subst(d)
    print(result)

    assert result['api'] == d['api']
    assert result['api_url'] == 'https://api.example.com/path'
    assert result['hello'] == 1
    assert result['world'] == '1'


def test_obj_get_props_dict_simple():
    class _A:
        @property
        def a(self) -> str:
            return 'Hello'

    instance = _A()
    res = obj_get_props_dict(instance)
    assert 'a' in res
    assert res['a'] == 'Hello'
