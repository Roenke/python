#! /usr/bin/env python3
import argparse
import pickle

import requests


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

    print('New friends:')
    for new_friend in added:
        print(new_friend)

    print('\nDeleted friends:')
    for deleted_friend in deleted:
        print(deleted_friend)


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

    args = parser.parse_args(argv)
    if args.save:
        save_mode_execute(args.id)
    else:
        diff_mode_execute(args.id)


if __name__ == "__main__":
    main()
