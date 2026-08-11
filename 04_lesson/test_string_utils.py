import pytest
from string_utils import StringUtils

utils = StringUtils()

# ===================== capitalize =====================


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("04 апреля 2023", "04 апреля 2023"),
    ("S", "S"),
    ("123", "123"),
])
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", "   "),
    ("skyPro", "Skypro"),
])
def test_capitalize_negative(input_str, expected):
    assert utils.capitalize(input_str) == expected

# ===================== trim =====================


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("   hello world", "hello world"),
])
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
    ("   skypro   ", "skypro   "),
])
def test_trim_negative(input_str, expected):
    assert utils.trim(input_str) == expected

# ===================== contains =====================


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("12345", "3", True),
    ("hello", "h", True),
])
def test_contains_positive(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", False),
    (" ", " ", True),
    ("abc", "", False),
])
def test_contains_negative(string, symbol, expected):
    assert utils.contains(string, symbol) == expected

# ===================== delete_symbol =====================


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("123123", "2", "1313"),
    ("a b c", " ", "abc"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "x", "SkyPro"),
    ("", "a", ""),
    ("   ", " ", ""),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected
