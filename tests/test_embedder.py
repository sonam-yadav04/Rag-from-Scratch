import pytest

from app.retrieval.embedder import embed_query, embed_texts


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def test_dimension_is_384():
    assert len(embed_texts(["hello"])[0]) == 384


def test_vectors_are_unit_length():
    assert dot(*[embed_texts(["some text"])[0]] * 2) == pytest.approx(1.0, abs=1e-4)


def test_empty_list_returns_empty():
    assert embed_texts([]) == []


def test_empty_question_raises():
    with pytest.raises(ValueError):
        embed_query("   ")


def test_order_is_preserved():
    batch = embed_texts(["apple fruit", "car engine"])
    single = embed_texts(["car engine"])[0]
    assert dot(batch[1], single) == pytest.approx(1.0, abs=1e-4)


def test_related_text_scores_higher_than_unrelated():
    a = embed_query("I have 2 years of backend experience")
    b = embed_query("Worked on FastAPI services for two years")
    c = embed_query("The weather in Bengaluru is rainy")
    assert dot(a, b) > dot(a, c)