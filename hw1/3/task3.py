#! /usr/bin/env python3
import argparse
import json
import codecs
import pickle

import requests


class Friend:
    def __init__(self, friend, from_json=True):
        if from_json:
            self.__id = friend['uid']
            self.__first_name = friend['first_name']
            self.__last_name = friend['last_name']

    def __str__(self):
        return '%d %s %s' % (self.__id, self.__first_name, self.__last_name)

    def get_id(self):
        return self.__id


def load(filename):
    file = open(filename, 'rb')
    result = set()
    while file:
        result.add(pickle.load(file))
    return result


def save(filename, friends):
    file = open(filename, 'wb')
    for friend in friends:
        pickle.dump(str(friend), file, protocol=pickle.HIGHEST_PROTOCOL)
    # file.writelines([str(x) for x in sorted(friends, key=lambda x: x.get_id())])
    file.close()


def pull_friends(id):
    params = {'user_id': id,
              'fields': ['first_name', 'last_name']}
    response = requests.get('https://api.vk.com/method/friends.get', params=params)
    decoded_content = codecs.decode(response.content)

    return json.loads(decoded_content)


def save_mode_execute(id):
    answer = pull_friends(id)

    old_info = load('%s.vk' % id)

    print(old_info)


def diff_mode_execute(id):
    answer = pull_friends(id)
    friends = set()
    for friend_raw in answer['response']:
        friends.add(Friend(friend_raw))

    save('%s.vk' % id, friends)


def main():
    argv = ['8758515', '-s']  # sys.argv
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
