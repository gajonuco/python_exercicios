import sys
import os

# Adiciona o diretório 'src' ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import pytest
from unique_in_order import unique_in_order

def test_empty_sequence():
    assert unique_in_order("") == []
    assert unique_in_order([]) == []
    assert unique_in_order(()) == []

def test_single_element_sequence():
    assert unique_in_order("A") == ["A"]
    assert unique_in_order(["A"]) == ["A"]
    assert unique_in_order(("A",)) == ["A"]

def test_reduce_duplicate():
    assert unique_in_order("AA") ==["A"]
    assert unique_in_order("AAAABBBCCDAABBB")== ["A", "B", "C", "D", "A", "B"]


def test_case_sensitivity():
    assert unique_in_order("ABBCcA") == ["A", "B", "C", "c", "A"]

def test_different_element_types():
    assert unique_in_order([1, 2, 3, 3, -1]) == [1, 2, 3, -1]
    assert unique_in_order(["a", "b", "b", "a"]) == ["a", "b", "a"]
