# TEMPORARY FILE TO PASS BOOTDEV TESTS

# Boot.dev `bootdev run` looks for a `tests.py` file in the root directory and to make sure it exits with code 0, as shown from the console output below. My actual tests will be run with `uv run -m unittest` and should automatically find all `test*.py` files, which I am organizing under the `tests` direcotry
# 3.2 - Maze Tests
# ╭──────────────────────────────╮
# │ Run your maze creation tests │
# ╰┬─────────────────────────────╯
#  > Command: python3 tests.py
#  ├─  ?  Expect exit code 0