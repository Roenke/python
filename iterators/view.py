#! /usr/bin/env python3


def main():
    d = {
        1: 50,
        2: "Second"
    }

    for key, value in d.items():
        if key == 1:
            value += 30

    # value не изменился: d[1] = 50
    print(d[1])


if __name__ == "__main__":
    main()
