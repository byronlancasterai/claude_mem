import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from context_block import append_to_context, extract_context

class MemoryStore:
    def __init__(self, path: str):
        self.path = path
        self.memories = []
        self.load()

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                try:
                    self.memories = json.load(f)
                except json.JSONDecodeError:
                    self.memories = []
        else:
            self.memories = []

    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self.memories, f, indent=2)

    def add(self, text: str) -> int:
        idx = len(self.memories)
        self.memories.append({
            'id': idx,
            'text': text.strip(),
            'active': True
        })
        self.save()
        return idx

    def update(self, memory_id: int, text: str) -> bool:
        if 0 <= memory_id < len(self.memories):
            self.memories[memory_id]['text'] = text.strip()
            self.save()
            return True
        return False

    def delete(self, memory_id: int) -> bool:
        if 0 <= memory_id < len(self.memories):
            self.memories[memory_id]['active'] = False
            self.save()
            return True
        return False

    def get_all(self) -> list[str]:
        return [m['text'] for m in self.memories if m['active']]

    def get_block(self) -> str:
        active = self.get_all()
        if not active:
            return ""
        combined = "\n\n".join(active)
        return f"<memory>\n{combined}\n</memory>"
