#!/usr/bin/env python

import client_wrap

def main():
    client = client_wrap.ClientWrap("get_test.log", "ipc:///var/run/zero-cache/0", 0)

    key_str = client.GetKeys()
    keys = key_str.split (';')
    del keys[-1]

    if len(keys) == 0:
        return

    print keys

if __name__ == "__main__":
    main()
