import re


def is_valid_email(email_address):
    res = re.search(r'^[a-zA-Z]{1,8}[0-9]{0,4}@jediacademy.edu$', email_address)
    if res:
        return True
    return False


if __name__ == '__main__':
    email_addresses = ['lskywal05@jediacademy.edu', 'byoda@jediacademy.edu', 'mwindu@jediacademy.edu',
                       'maul@jediacademy.eduasdf', 'vader99999@jediacademy.edu', 'darthsidious@jediacademy.edu',
                       'r2d2@jediacademy.edu', 'vader@sithschool.edu']

    for email in email_addresses:
        print('{}: {}'.format(email, is_valid_email(email)))
