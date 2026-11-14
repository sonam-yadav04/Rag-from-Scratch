from app.ingestion.models import PageContent


def test_page_content_fields():
    p = PageContent(text="hello", source="a.pdf", page=2)
    assert (p.text, p.source, p.page) == ("hello", "a.pdf", 2)


def test_equal_records_compare_equal():
    a = PageContent("x", "a.pdf", 1)
    b = PageContent("x", "a.pdf", 1)
    assert a == b