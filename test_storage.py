import os
import sys
import json

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from storage import MemoryStore

TEST_PATH = '/tmp/test_memories.json'

def setup():
    if os.path.exists(TEST_PATH):
        os.remove(TEST_PATH)

def test_add_and_load():
    setup()
    store = MemoryStore(TEST_PATH)
    idx = store.add('first memory')
    assert idx == 0
    assert store.get_all() == ['first memory']
    # reload from disk
    store2 = MemoryStore(TEST_PATH)
    assert store2.get_all() == ['first memory']

def test_update():
    setup()
    store = MemoryStore(TEST_PATH)
    store.add('old text')
    store.update(0, 'new text')
    assert store.get_all() == ['new text']
    assert store.update(99, 'fail') == False

def test_delete():
    setup()
    store = MemoryStore(TEST_PATH)
    store.add('keep')
    store.add('drop')
    store.delete(1)
    assert store.get_all() == ['keep']
    assert store.delete(99) == False

def test_get_block():
    setup()
    store = MemoryStore(TEST_PATH)
    store.add('alpha')
    store.add('beta')
    block = store.get_block()
    assert block == '<memory>\nalpha\n\nbeta\n</memory>'
    store.delete(0)
    assert store.get_block() == '<memory>\nbeta\n</memory>'

def test_empty_block():
    setup()
    store = MemoryStore(TEST_PATH)
    assert store.get_block() == ''

def run():
    tests = [test_add_and_load, test_update, test_delete, test_get_block, test_empty_block]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            print(f'PASS {t.__name__}')
            passed += 1
        except AssertionError as e:
            print(f'FAIL {t.__name__}: {e}')
            failed += 1
    print(f'{passed} passed, {failed} failed')

if __name__ == '__main__':
    run()
