#!/usr/bin/env python

import sys
import argparse
import client_wrap

WRITE_FUNCTIONS = {
    'double' : client_wrap.ClientWrap.WriteDouble,
    'long' : client_wrap.ClientWrap.WriteLong,
    'string' : client_wrap.ClientWrap.WriteString
}

def parse_args():
    parser = argparse.ArgumentParser(description="This is utility to set new value for the specified key in the cache")
    parser.add_argument("-t", "--type", help="type of the cached data", default="double", choices=('double', 'long', 'string'))
    parser.add_argument("-c", "--connection", help="connection string", default="ipc:///var/run/zero-cache/0")
    parser.add_argument("-k", "--key", help="key string", required=True)
    parser.add_argument("-v", "--value", help="cached value", required=True)
    parser.add_argument("-l", "--log", help="log file name", default="")

    global ARGS
    ARGS = parser.parse_args()

def write_value(client, key, value):
    return WRITE_FUNCTIONS[ARGS.type](client, key, value)

def main():
    parse_args()
    client = client_wrap.ClientWrap(ARGS.log, ARGS.connection, 0)
    write_value(client, ARGS.key, ARGS.value)

if __name__ == "__main__":
    main()
