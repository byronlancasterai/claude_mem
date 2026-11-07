from context_block import format_context_block, extract_context


def test_format_empty():
    assert format_context_block("") == ""


def test_format_single():
    result = format_context_block("User asked about pyglet.")
    assert "User asked about pyglet." in result
    assert "<memory>" in result
    assert "</memory>" in result


def test_format_multiple():
    result = format_context_block("Fact 1.\n\nFact 2.")
    assert "Fact 1." in result
    assert "Fact 2." in result
    assert "<memory>" in result


def test_extract_roundtrip():
    original = "Some context."
    block = format_context_block(original)
    extracted = extract_context(block)
    assert original == extracted


def test_extract_empty_block():
    assert extract_context("") == ""


def test_extract_wrong_tags():
    assert extract_context("<context>foo</context>") == ""


def test_extract_whitespace_stripped():
    block = "<memory>\n  padded  \n</memory>"
    assert extract_context(block) == "padded"
