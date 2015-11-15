#! /usr/bin/env python3
import argparse
import sys
import requests
import json
import codecs
import vk


def save_mode_execute(id):
    pass


def diff_mode_execute(id):
    params = {'user_id': id,
              'fields': ['first_name', 'last_name']}
    response = requests.get('https://api.vk.com/method/friends.get', params=params)
    print(response.content)


def main():
    argv = ['8758515', '-d']  #sys.argv
    # argv = [8758515, '-s']  #sys.argv
    # argv = [8758515, '-d']  #sys.argv
    parser = argparse.ArgumentParser(description='Enter user id and mode')
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('-s', '--save', action='store_true')
    mode_group.add_argument('-d', '--diff', action='store_true')
    parser.add_argument('id', type=int)
    # parser.print_help()
    args = parser.parse_args(argv)
    if args.save:
        save_mode_execute(args.id)
    else:
        diff_mode_execute(args.id)

if __name__ == "__main__":
    main()
