"""
Simple example of selecting a model branch (with optional type filtering).

https://discourse.techart.online/t/motionbuilder-python-select-branches/15462
"""
import pyfbsdk as fb


def recursiveSelect(node, types=None):
     if (not types or isinstance(node, types)) and not node.Selected:
        node.Selected = True
    for child in node.Children:
        recursiveSelect(child)


recursiveSelect(root)  # Select all children in hierarchy
recursiveSelect(root, types=fb.FBModelSkeleton)  # Select all Skeleton children
