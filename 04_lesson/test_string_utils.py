import pytest
from string_utils import StringUtils
string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected_output", [
    (" sky", "sky"), (" ", "")
])
def test_trim_positive(input_str, expected_output):
    result = string_utils.trim(input_str)
    assert result == expected_output


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "p", True),
    ("skypro", "u", False),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "o", "skypr"),
    ("SkyPro", "Pro", "Sky"),
    ("symbol", "bol", "sym"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("5123", "5123"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected_output", [
    (" sky ", "sky "),
    ])
def test_trim_negative(input_str, expected_output):
    result = string_utils.trim(input_str)
    assert result == expected_output


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "s", True),
    ("skypro", "S", False)
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "w", "skypro"),
    ("SkyPro", "Hro", "SkyPro"),
    ("symbol", "bal", "symbol")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
