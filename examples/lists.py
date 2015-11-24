#! /usr/bin/env python3

def my_function():
    print('I in function')


def my_many_args_function(*args):
    print('many args function. agrs =', args)


def main():
    a = ['sdfsdf', 'spbau', 34, 452]
    print('origin:', a)

    a[0:2] = [2, 'wayway']
    print('switch 0-2:', a)
    
    a[1:3] = []
    print('remove 1-3:', a)

    a[1:1] = ['inserted']
    print('insert after 1:', a)

    a.append('append')
    print('append: ', a)

    a.remove(2)
    print('remove 2:', a)

    a.extend(["ext1", "ext2"])
    print('extend:', a)

    a.insert(0, 'inserted to head')
    print("insert to head:", a)

    a.pop()
    print("pop():", a)

    a.pop(0)
    print('pop(0):', a)

    print('')

    b = ['find_me', 'find_me']
    print('origin', b)

    print('.count("find_me") =', b.count('find_me'))

    print('.index("find_me") = ', b.index('find_me'))

    print('')

    print('tuple example: ', ('first_elem', 'second elem', 3))

    print('tuples in unmutable')

    print('')

    d = { 'str_key' : 'str_value', 4: 5, 'key_str': 43224 }
    print('dictionary: ', d)

    d['new_key'] = 'new_value'
    print('insert key:', d)

    d['new_key'] = 'updated_value'
    print('update key', d)

    del d['new_key']
    print('delete key', d)

    print('you can you .keys():', d.keys())
    print('or values()', d.values())

    try:
        print(d['not_value'])
    except KeyError:
        print('value not found')

    my_function()
    # note. Functions can be overwrited

    my_many_args_function(1,2,3,4)
    my_many_args_function(2,3)
    my_many_args_function(2,)



if(__name__ == "__main__"):
    main()
