"""Basic tests for codrill."""

from codrill import snippets_of_funcs, callables_of_module, Exercises


def _sample_func(x, y):
    """Add two numbers together."""
    return x + y


def _another_func(items):
    """Return the first item of a list."""
    return items[0]


import types

_test_module = types.ModuleType('_test_module')
_test_module.__name__ = '_test_module'
_test_module._sample_func = _sample_func
_test_module._sample_func.__module__ = '_test_module'
_test_module._another_func = _another_func
_test_module._another_func.__module__ = '_test_module'


def test_callables_of_module():
    callables = list(callables_of_module(_test_module))
    names = {f.__name__ for f in callables}
    assert '_sample_func' in names
    assert '_another_func' in names


def test_snippets_of_funcs_with_list():
    funcs = [_sample_func, _another_func]
    snippets = list(snippets_of_funcs(funcs))
    assert len(snippets) == 2
    assert 'Add two numbers together' in snippets[0]


def test_snippets_of_funcs_with_module():
    snippets = list(snippets_of_funcs(_test_module))
    assert len(snippets) >= 2


def test_exercises_class():
    funcs = [_sample_func, _another_func]
    e = Exercises(funcs)
    assert len(e.snippets) == 2
