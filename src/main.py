import sys
import json
import os

sys.path.insert(0, '.')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from context_block import format_context_block, extract_context
from storage import MemoryStore


def handle_request(request: dict) -> dict:
    """Handle a single MCP-style JSON-RPC request."""
    method = request.get("method", "")
    params = request.get("params", {})
    req_id = request.get("id")

    store = MemoryStore()

    if method == "format_context":
        result = format_context_block(params.get("text", ""))
    elif method == "extract_context":
        result = extract_context(params.get("block", ""))
    elif method == "health_check":
        result = {"status": "ok", "version": "0.1.0"}
    elif method == "add_memory":
        mid = store.add(params.get("text", ""), params.get("tags", []))
        result = {"id": mid, "status": "added"}
    elif method == "update_memory":
        ok = store.update(params.get("id", ""), params.get("text", ""))
        result = {"status": "updated" if ok else "not_found"}
    elif method == "delete_memory":
        ok = store.delete(params.get("id", ""))
        result = {"status": "deleted" if ok else "not_found"}
    elif method == "get_all":
        result = {"memories": store.get_all()}
    elif method == "get_block":
        result = {"block": store.get_block()}
    else:
        return {"id": req_id, "error": {"code": -32601, "message": f"Unknown method: {method}"}}

    return {"id": req_id, "result": result}


def main():
    """Read JSON-RPC requests from stdin, write responses to stdout."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
        except json.JSONDecodeError as e:
            print(json.dumps({"error": {"code": -32700, "message": str(e)}}), flush=True)
            continue
        response = handle_request(request)
        print(json.dumps(response), flush=True)


if __name__ == "__main__":
    main()
