import sys
import json

sys.path.insert(0, '.')
from context_block import format_context_block, extract_context


def handle_request(request: dict) -> dict:
    """Handle a single MCP-style JSON-RPC request."""
    method = request.get("method", "")
    params = request.get("params", {})
    req_id = request.get("id")

    if method == "format_context":
        result = format_context_block(params.get("text", ""))
    elif method == "extract_context":
        result = extract_context(params.get("block", ""))
    elif method == "health_check":
        result = {"status": "ok", "version": "0.1.0"}
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
