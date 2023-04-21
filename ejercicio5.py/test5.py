def test_insert(tree):
    tree.insert(5)
    assert tree.search(5) == True
    tree.insert(7)
    assert tree.search(7) == True
    tree.insert(3)
    assert tree.search(3) == True
    tree.insert(4)
    assert tree.search(4) == True

def test_delete(tree):
    tree.delete(5)
    assert tree.search(5) == False
    tree.delete(7)
    assert tree.search(7) == False
    tree.delete(3)
    assert tree.search(3) == False
    tree.delete(4)
    assert tree.search(4) == False

def test_height(tree):
    assert tree.height() == 0
    tree.insert(5)
    assert tree.height() == 1
    tree.insert(7)
    assert tree.height() == 2
    tree.insert(3)
    assert tree.height() == 2
    tree.insert(4)
    assert tree.height() == 3

def test_occurrences(tree):
    tree.insert(5)
    tree.insert(7)
    tree.insert(3)
    tree.insert(4)
    tree.insert(4)
    tree.insert(4)
    assert tree.count_occurrences(5) == 1
    assert tree.count_occurrences(7) == 1
    assert tree.count_occurrences(3) == 1
    assert tree.count_occurrences(4) == 3

def test_count_parity(tree):
    tree.insert(5)
    tree.insert(7)
    tree.insert(3)
    tree.insert(4)
    tree.insert(2)
    tree.insert(8)
    assert tree.count_parity() == (3, 3)
