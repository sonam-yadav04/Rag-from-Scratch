
from app.ingestion.cleaner import clean_text


def test_remove_extra_spaces():
    result = clean_text("Hello     World")
    assert result == "Hello World"


def test_remove_null_characters():
    result = clean_text("Hello\x00World")
    assert result == "HelloWorld"


def test_normalize_line_endings():
    result = clean_text("Hello\r\nWorld")
    assert result == "Hello\nWorld"


def test_remove_excessive_blank_lines():
    result = clean_text("Hello\n\n\n\nWorld")
    assert result == "Hello\n\nWorld"


def test_strip_whitespace():
    result = clean_text("   Hello World   ")
    assert result == "Hello World"


def test_empty_text():
    assert clean_text("") == ""


def test_whitespace_only():
    assert clean_text("   \n   ") == ""
