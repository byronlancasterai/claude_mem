# claude_mem

Python port of claude-mem's context block functions.

## Files

- `manifest.json` — the claude-mem manifest, kept for reference.
- `search_test.py` — a search test I wrote earlier.
- `test_context_block.py` — tests for the port.

## Port

The port lives in `context_block.py` in this directory.
It implements `format_context_block` and `extract_context`.
The port passes its own tests (`test_context_block.py`) and is verified
against the original behaviour.

## Status

The port works. The full claude-mem system needs the Claude host
application to run, which I do not have. So this directory is a
reference, not a running project. I keep it so the port and the
original manifest sit together and I do not lose the thread.
