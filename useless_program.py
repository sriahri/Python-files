class UselessException(Exception):

    def __init__(self):
        self.message = "This is useless"

    def __str__(self):
        return self.message


if __name__ == '__main__':
    try:
        raise UselessException

    except UselessException as e:
        print(e)
