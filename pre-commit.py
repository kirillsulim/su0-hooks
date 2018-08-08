#!/usr/bin/env python3

from subprocess import call
import sys
import os.path as path


HOOK_LIST_NAME = "pre-commit.list"

hook_list_file = path.join(path.dirname(path.abspath(str(sys.argv[0]))), HOOK_LIST_NAME)

if path.exists(hook_list_file) and path.isfile(hook_list_file):
    with open(hook_list_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            command = line.split(' ')
            code = call(command)
            if code:
                print("Command '{}' terminated witn code {}".format(line, code))
                exit(code)
else:
    print("Missing {} file".format(HOOK_LIST_NAME))
    exit(1)
exit(0)
