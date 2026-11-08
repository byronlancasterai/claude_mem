def format_context_block(context_str: str) -> str:
    """
    Format a context string into a block.
    """
    if not context_str.strip():
        return ""
    return f"<memory>\n{context_str.strip()}\n</memory>"

def extract_context(block: str) -> str:
    """
    Extract content from a formatted context block.
    """
    if not block.startswith("<memory>") or not block.endswith("</memory>"):
        return ""
    content = block[len("<memory>"):-len("</memory>")].strip()
    return content

def summarise_memories(memories: list[str]) -> str:
    """
    Combine a list of memory strings into a single context block.
    Each memory is separated by a blank line.
    """
    if not memories:
        return ""
    combined = "\n\n".join(m.strip() for m in memories if m.strip())
    return format_context_block(combined)
