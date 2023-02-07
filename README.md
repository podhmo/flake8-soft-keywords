# flake8-soft-keywords
flake8 plugin that preventing assignment with the name in soft keywords

```console
$ flake8 -v _examples/*.py
flake8.checker            MainProcess    176 INFO     Making checkers
flake8.main.application   MainProcess    221 INFO     Finished running
flake8.main.application   MainProcess    222 INFO     Reporting errors
flake8.main.application   MainProcess    222 INFO     Found a total of 3 violations and reported 3
_examples/00bad.py:1:11: E231 missing whitespace after ','
_examples/00bad.py:2:5: SK0 soft keyword is used: dict
_examples/00bad.py:4:5: SK0 soft keyword is used: sum
```