#!/usr/bin/env python

import sys
import client_wrap

def get_keys(client):
    key_str = client.GetKeys()
    keys = key_str.split (';')
    del keys[-1]

    if len(keys) == 0:
        sys.exit()

    return keys

def print_keys(client, keys):
    for key in keys:
        value = client.ReadLong(key)
        print "%s = %d" % (key, value)

def main():
    client = client_wrap.ClientWrap("get_test.log", "ipc:///var/run/zero-cache/0", 0)

    keys = get_keys(client)

    print_keys(client, keys)

if __name__ == "__main__":
    main()
