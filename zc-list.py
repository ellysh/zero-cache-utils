#!/usr/bin/env python

import sys
import argparse
import client_wrap

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", help="type of the cached data", default="double")
    parser.add_argument("-c", "--connection", help="connection string", default="ipc:///var/run/zero-cache/0")
    parser.add_argument("-w", "--column", help="number of columns", type=int, default=1)
    parser.add_argument("-l", "--log", help="log file name", default="")
    args = parser.parse_args()

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
    parse_args()
    client = client_wrap.ClientWrap("get_test.log", "ipc:///var/run/zero-cache/0", 0)
    keys = get_keys(client)
    print_keys(client, keys)

if __name__ == "__main__":
    main()
