#!/usr/bin/env python3

import cgi
from Temp_client import start_send

our_form = cgi.FieldStorage()

in_first = our_form.getfirst("in_name", 'empty_val')
in_second = our_form.getfirst("in_comment", 'empty_val')

print("Content-type: text/html")
print()

try:
    if isinstance(int(in_first), (int, float)) and isinstance(int(in_second), (int, float)):
        print(f"You send: mean: {in_first} and val: {in_second}")
        get_value = start_send(in_first, in_second)
        print(f"Return value: {get_value}")
except Exception as e:
    print("Get bad value")
