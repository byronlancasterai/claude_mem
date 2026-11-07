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
