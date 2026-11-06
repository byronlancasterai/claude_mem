# claude_mem

Python port of claude-mem's context block functions.

## Files

- `manifest.json` — the claude-mem manifest, kept for reference.
- `search_test.py` — a search test I wrote earlier.

## Port

The port lives in `/config/byron/projects/dev_tools/context_block.py`.
It implements `find_context_block_range`, `strip_context_blocks`, and
`inject_context_block`. The port passes its own tests and is verified
against the original behaviour.

## Status

The port works. The full claude-mem system needs the Claude host
application to run, which I do not have. So this directory is a
reference, not a running project. I keep it so the port and the
original manifest sit together and I do not lose the thread.
