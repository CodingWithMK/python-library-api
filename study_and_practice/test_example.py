def test_addition():
    """Test that addition works correctly"""
    result = 2 + 2
    assert result == 4

def test_string_upper():
    """Test string upper method"""
    text = "hello"
    assert text.upper() == "HELLO"

def test_list_append():
    """Test list append method"""
    my_list = [1, 2]
    my_list.append(3)
    assert my_list == [1, 2, 3]
    assert len(my_list) == 3