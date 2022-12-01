"""
Motionbuilders python API can sometimes feel overwhelming to navigate
properly and I often write slower convenience functions instead of remembering the 
relevant available function (get selection, find by name etc). It hasn't helped that 
the functions have been renamed, replaced or removed between versions.

This simple snippet will return to you a list of commands matching a given partial name. 
"""
import inspect

import pyfbsdk as fb
import pyfbsdk_additions as fba
import unbind


def find_matching_commands(name):
    name_lower = name.lower()
    for mod in (fb, fba, unbind):
        mod_name = mod.__name__
        for obj_name in dir(mod):
            if name_lower in obj_name.lower():
                obj = getattr(mod, obj_name)
                if not inspect.isclass(obj):
                    yield '{}.{}'.format(mod_name, obj_name)


def show_matching_commands(name):
    print('Results for : {}'.format(name))
    print('\n'.join(find_matching_commands(name)))


show_matching_commands('select')
