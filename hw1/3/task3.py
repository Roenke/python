#! /usr/bin/env python3
import argparse
import pickle
import os

import requests
import requests.exceptions


class Friend:
    def __init__(self, friend):
        self.__id = friend['uid']
        self.__first_name = friend['first_name']
        self.__last_name = friend['last_name']

    def __str__(self):
        return '%d %s %s' % (self.__id, self.__first_name, self.__last_name)

    def __hash__(self):
        return self.__id

    def __eq__(self, other):
        return self.get_id() == other.get_id()

    def get_id(self):
        return self.__id


def load(filename):
    os.path.isfile(filename)
    file = open(filename, 'rb')
    result = pickle.load(file)
    file.close()
    return result


def save(filename, friends):
    file = open(filename, 'wb')
    pickle.dump(friends, file)
    file.close()


def pull_friends(user_id):
    params = {'user_id': user_id,
              'fields': ['first_name', 'last_name']}
    response = requests.get('https://api.vk.com/method/friends.get', params=params)

    friends = set()
    json = response.json()
    if 'error' in json:
        raise Exception(json['error']['error_msg'])
    for friend in response.json()['response']:
        friends.add(Friend(friend))

    return friends


def save_mode_execute(user_id):
    actual_friends = pull_friends(user_id)

    save('%s.vk' % user_id, actual_friends)


def diff_mode_execute(user_id):
    actual_friends = pull_friends(user_id)

    old_info = load('%s.vk' % user_id)

    deleted = old_info.difference(actual_friends)
    added = actual_friends.difference(old_info)

    if len(deleted) == 0 and len(added) == 0:
        print('No changes')
    elif len(deleted) != 0:
        print('\nDeleted friends:')
        for deleted_friend in deleted:
            print(deleted_friend)
        if len(added) != 0:
            print('New friends:')
            for new_friend in added:
                print(new_friend)


def create_parser():
    parser = argparse.ArgumentParser(description='Enter user id and mode')
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument('-s', '--save', action='store_true')
    mode_group.add_argument('-d', '--diff', action='store_true')
    parser.add_argument('id', type=int)
    return parser


def main():
    argv = ['8758515', '-d']  # sys.argv
    parser = create_parser()

    try:
        args = parser.parse_args(argv)
        if args.save:
            save_mode_execute(args.id)
        else:
            diff_mode_execute(args.id)
    except requests.exceptions.RequestException as e:
        print(e)
        exit(1)
    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
