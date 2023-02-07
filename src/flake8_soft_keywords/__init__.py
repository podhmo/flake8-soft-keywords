from __future__ import annotations
import typing as t
import sys
import ast


_KEYWORDS = None


class Error(t.NamedTuple):
    lineno: int
    col: int
    message: str
    type_: str


class SK0(Error):
    """soft keyword is used"""


def _soft_reserved_keywords() -> frozenset[str]:
    global _KEYWORDS
    if _KEYWORDS is None:
        _KEYWORDS = frozenset(vars(sys.modules[sum.__module__]).keys())
    return _KEYWORDS


class Checker:
    """preventing the assignment with the name in soft keywords"""

    # off_by_default = True

    def __init__(self, tree: ast.Module):
        self.tree = tree
        self.reserved_words = _soft_reserved_keywords()

    def run(self) -> t.Generator[Error, None, None]:
        for node in ast.walk(self.tree):
            if hasattr(node, "targets") and isinstance(node, ast.Assign):  # slow?
                # assign:: <targets...> = <value>
                for x in node.targets:
                    found_name = self._check(x)
                    if found_name is not None:
                        yield SK0(
                            lineno=x.lineno,
                            col=x.col_offset,
                            message=f"SK0 soft keyword is used: {found_name}",
                            type_=SK0,
                        )

    def _check(self, node: ast.Name | ast.Tuple) -> str | None:
        if hasattr(node, "id"):  # ast.Name
            if node.id in self.reserved_words:
                return node.id
            return None
        elif hasattr(node, "elts"):  # ast.Tuple
            for x in node.elts:
                v = self._check(x)
                if v is not None:
                    return v
        # more nodes are existed?
        return None
