def message(friends):
    for friend in friends:
        print("Hello there, {}, how are you today?".format(friend))


def send_messages_8_8(friends):
    sent_messages = []
    for friend in friends:
        print("Hello there, {}, how are you today?".format(friend))
        sent_messages.append(friend)
        friends.remove(friend)
    return sent_messages, friends


def send_messages_8_9(friends):
    sent_messages = []
    original_friends = friends.copy()
    for friend in friends:
        print("Hello there, {}, how are you today?".format(friend))
        sent_messages.append(friend)
        friends.remove(friend)
    return original_friends, sent_messages


if __name__ == '__main__':
    friends = ['Jack', 'John', 'Alice', 'Bob', 'Charles', 'Danny', 'Steve']
    message(friends)
    print()

    print()
    sent_messages, friends_from = send_messages_8_8(friends)
    print("Sent messages: {}".format(sent_messages))
    print("Friends: {}".format(friends_from))
    print()

    print()
    original, sent_messages = send_messages_8_9(friends)
    print("Sent messages: {}".format(sent_messages))
    print("Friends: {}".format(friends_from))
