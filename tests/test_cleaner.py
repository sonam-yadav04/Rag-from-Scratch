from app.ingestion.cleaner import clean_text


def test_collapses_spaces():
    assert clean_text("a      b") == "a b"


def test_strips_line_padding_keeps_breaks():
    assert clean_text("   Title   \n  next") == "Title\nnext"


def test_collapses_blank_lines():
    assert clean_text("a\n\n\n\nb") == "a\n\nb"