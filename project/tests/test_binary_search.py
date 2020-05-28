from binary_search.binary_search import list_patentially_contain_a_value, binary_search


def test_list_patentially_contain_a_value():
    test_list = [11, 12, 13, 14]
    assert not list_patentially_contain_a_value(test_list, 10)
    assert not list_patentially_contain_a_value(test_list, 15)
    assert list_patentially_contain_a_value(test_list, 11)
    assert list_patentially_contain_a_value(test_list, 12)
    assert list_patentially_contain_a_value(test_list, 14)


def test_binary_search():
    test_list = [11, 12, 13, 14]
    existed_value = 13
    nonexistent_value = 33
    assert binary_search(test_list, existed_value)
    assert not binary_search(test_list, nonexistent_value)
