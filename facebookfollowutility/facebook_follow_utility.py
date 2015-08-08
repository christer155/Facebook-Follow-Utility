__author__ = 'Ryan'

import argparse


class Friend:
    def __init__(self, name, following):
        self.name = name
        self.following = following


def process_arguments():
    parser = argparse.ArgumentParser(description='Get input for facebook follow utility. To get the correct text file '
                                                 'you must go to Facebook > News Feed Preferences > People > '
                                                 'Alphabetical Order and then copy all the results.')
    parser.add_argument('-f', dest="text_file_path", type=str,
                        help='Full file path pointing towards text file with the necessary info for the script.')
    return parser.parse_args()


def read_friend_text(lines):
    name = lines[0][:-1]
    following = len(lines[2]) == 10
    friend = Friend(name, following)
    return friend


def load_friends_from_file(filepath):
    friends = []
    with open(filepath) as file:
        line_collection = []
        for line in file:
            if len(line_collection) > 2:
                friends.append(read_friend_text(line_collection))
                line_collection.clear()
                continue
            line_collection.append(line)
    return friends


def main():
    args = process_arguments()

    friends = load_friends_from_file(args.text_file_path)

    following_friends = []
    not_following_friends = []

    for friend in friends:
        if friend.following:
            following_friends.append(friend)
        else:
            not_following_friends.append(friend)

    print("Total Friends count: %d" % len(friends))
    print("Following friends count: %d: " % len(following_friends))
    print("Not Following friends count: %d: " % len(not_following_friends))

    print()

    print("Following:")
    for friend in following_friends:
        print("\t", friend.name)

    print()

    print("Not Following:")
    for friend in not_following_friends:
        print("\t", friend.name)


if __name__ == "__main__":
    main()
