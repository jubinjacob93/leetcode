# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a personal LeetCode solutions repository. Solutions are written in Python 3 and generated/managed via the [LeetCode VS Code extension](https://marketplace.visualstudio.com/items?itemName=LeetCode.vscode-leetcode) (`@lc app=leetcode`).

## File naming convention

Files follow the pattern `<problem-number>.<kebab-case-title>.py`, e.g. `70.climbing-stairs.py`.

## File structure

Each solution file is structured as:

```python
#
# @lc app=leetcode id=<id> lang=python3
#
# [<id>] <Problem Title>
#

# @lc code=start
class Solution:
    def methodName(self, ...):
        ...
# @lc code=end
```

The solution logic lives entirely between the `@lc code=start` and `@lc code=end` markers. LeetCode-provided type stubs (`TreeNode`, `ListNode`, etc.) are commented out above the `Solution` class for reference but are not re-defined.

## Running a solution

There is no test harness in this repo. To verify a solution, run it directly:

```
python <filename>.py
```

Or submit via the LeetCode VS Code extension.

## Problem categories covered so far

- **Dynamic Programming**: 70, 91, 198, 746
- **Binary Trees**: 104, 226, 543
- **Linked Lists**: 21
