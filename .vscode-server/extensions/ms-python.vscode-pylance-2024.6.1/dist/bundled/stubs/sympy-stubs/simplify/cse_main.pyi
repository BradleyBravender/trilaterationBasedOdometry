from collections import defaultdict
from typing import Any

from sympy.core.containers import OrderedSet

basic_optimizations = ...

def reps_toposort(r) -> list[Any]: ...
def cse_separate(r, e) -> list[list[Any]]: ...
def cse_release_variables(r, e) -> tuple[Any, Any] | tuple[list[Any], Any]: ...
def preprocess_for_cse(expr, optimizations): ...
def postprocess_for_cse(expr, optimizations): ...

class FuncArgTracker:
    def __init__(self, funcs) -> None: ...
    def get_args_in_value_order(self, argset) -> list[Any]: ...
    def get_or_add_value_number(self, value): ...
    def stop_arg_tracking(self, func_i) -> None: ...
    def get_common_arg_candidates(self, argset, min_func_i=...) -> defaultdict[Any, int] | dict[Any, int]: ...
    def get_subset_candidates(self, argset, restrict_to_funcset=...) -> OrderedSet: ...
    def update_func_argset(self, func_i, new_argset) -> None: ...

class Unevaluated:
    def __init__(self, func, args) -> None: ...
    def __str__(self) -> str: ...
    def as_unevaluated_basic(self): ...
    @property
    def free_symbols(self) -> set[Any]: ...

    __repr__ = ...

def match_common_args(func_class, funcs, opt_subs) -> None: ...
def opt_cse(exprs, order=...) -> dict[Any, Any]: ...
def tree_cse(exprs, symbols, opt_subs=..., order=..., ignore=...) -> tuple[list[Any], list[Any]]: ...
def cse(
    exprs, symbols=..., optimizations=..., postprocess=..., order=..., ignore=..., list=...
) -> (
    tuple[Any, str]
    | tuple[Any, list[Any] | set[Any] | tuple[Any, ...]]
    | tuple[Any, dict[Any, Any]]
    | tuple[Any, Any]
    | tuple[list[Any], Any]
    | tuple[list[Any], list[Any]]
): ...
