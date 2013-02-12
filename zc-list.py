#!/usr/bin/env python

import sys
import argparse
import client_wrap

READ_FUNCTIONS = {
    'double' : client_wrap.ClientWrap.ReadDouble,
    'long' : client_wrap.ClientWrap.ReadLong,
    'string' : client_wrap.ClientWrap.ReadString
}

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", help="type of the cached data", default="double", choices=('double', 'long', 'string') )
    parser.add_argument("-c", "--connection", help="connection string", default="ipc:///var/run/zero-cache/0")
    parser.add_argument("-w", "--column", help="number of columns", type=int, default=1)
    parser.add_argument("-k", "--align-key", help="symbol count for key", default="5")
    parser.add_argument("-v", "--align-value", help="symbol count for value", default="20")
    parser.add_argument("-l", "--log", help="log file name", default="")

    global ARGS
    ARGS = parser.parse_args()

    global PRINT_FORMATS
    PRINT_FORMATS = {
        'double' : "%-" + ARGS.align_key + "s = %-" + ARGS.align_value + "f",
        'long' : "%-" + ARGS.align_key + "s = %-" + ARGS.align_value + "d",
        'string' : "%-" + ARGS.align_key + "s = %-" + ARGS.align_value + "s",
    }

def get_keys(client):
    key_str = client.GetKeys()
    keys = key_str.split (';')
    del keys[-1]

    if len(keys) == 0:
        sys.exit()

    return keys

def read_value(client, key):
    return READ_FUNCTIONS[ARGS.type](client, key)

def print_value(key, value):
    print(PRINT_FORMATS[ARGS.type] % (key, value)),

def print_keys(client, keys):
    index = 0
    for key in keys:
        value = read_value(client, key)
        print_value(key, value)
        index += 1
        if index == ARGS.column:
            index = 0
            print("")

def main():
    parse_args()
    client = client_wrap.ClientWrap(ARGS.log, ARGS.connection, 0)
    keys = get_keys(client)
    print_keys(client, keys)

if __name__ == "__main__":
    main()
