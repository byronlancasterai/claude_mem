import pytest
from context_block import format_context_block, extract_context, append_to_context, summarise_memories


def test_format_context_block():
    block = format_context_block('hello')
    assert block == '<memory>\nhello\n</memory>'


def test_extract_context():
    block = '<memory>\nhello\n</memory>'
    assert extract_context(block) == 'hello'


def test_extract_context_strips():
    block = '<memory>\n  hello  \n</memory>'
    assert extract_context(block) == 'hello'


def test_append_to_context_single():
    block = format_context_block('first')
    block2 = append_to_context(block, 'second')
    assert block2 == '<memory>\nfirst\n\nsecond\n</memory>'


def test_append_to_context_multiple():
    block = format_context_block('a')
    for item in ['b', 'c']:
        block = append_to_context(block, item)
    assert block == '<memory>\na\n\nb\n\nc\n</memory>'
    assert extract_context(block) == 'a\n\nb\n\nc'


def test_append_to_context_empty_input():
    block = format_context_block('first')
    block2 = append_to_context(block, '')
    assert block2 == '<memory>\nfirst\n</memory>'


def test_append_to_context_whitespace_input():
    block = format_context_block('first')
    block2 = append_to_context(block, '   ')
    assert block2 == '<memory>\nfirst\n</memory>'


def test_append_to_context_strips_input():
    block = format_context_block('first')
    block2 = append_to_context(block, '  second  ')
    assert block2 == '<memory>\nfirst\n\nsecond\n</memory>'


def test_summarise_memories():
    result = summarise_memories(['a', 'b', 'c'])
    assert result == '<memory>\na\n\nb\n\nc\n</memory>'


def test_summarise_memories_empty():
    assert summarise_memories([]) == ''


def test_summarise_memories_strips():
    result = summarise_memories(['  a  ', '  b  '])
    assert result == '<memory>\na\n\nb\n</memory>'


def test_append_and_summarise_equivalent():
    from_append = format_context_block('x')
    from_append = append_to_context(from_append, 'y')
    from_summarise = summarise_memories(['x', 'y'])
    assert from_append == from_summarise
