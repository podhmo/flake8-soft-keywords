from __future__ import annotations
import typing as t

if t.TYPE_CHECKING:
    import ast


class Plugin:
    """preventing the assignment with the name in soft keywords"""

    # off_by_default = True

    def __init__(self, tree: ast.Module):
        self.tree = tree

    def run(self) -> t.Generator[str]:
        yield from []
