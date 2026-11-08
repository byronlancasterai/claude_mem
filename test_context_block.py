from context_block import format_context_block, extract_context, summarise_memories


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


def test_summarise_empty():
    assert summarise_memories([]) == ""


def test_summarise_single():
    result = summarise_memories(["one"])
    assert extract_context(result) == "one"


def test_summarise_multiple():
    result = summarise_memories(["first", "second", "third"])
    extracted = extract_context(result)
    assert "first" in extracted
    assert "second" in extracted
    assert "third" in extracted
    assert extracted.count("\n\n") == 2


def test_summarise_strips_whitespace():
    result = summarise_memories(["  padded  ", "  more  "])
    extracted = extract_context(result)
    assert extracted == "padded\n\nmore"


def test_summarise_skips_blanks():
    result = summarise_memories(["keep", "", "  ", "also"])
    extracted = extract_context(result)
    assert extracted == "keep\n\nalso"


def test_summarise_roundtrip():
    memories = ["alpha", "beta", "gamma"]
    block = summarise_memories(memories)
    extracted = extract_context(block)
    assert extracted == "alpha\n\nbeta\n\ngamma"
