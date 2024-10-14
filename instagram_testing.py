class InstagramAccount:
    def __init__(self, first_name, last_name, age, mobile):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.mobile = mobile
        self.followers = []

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_mobile(self, mobile):
        self.mobile = mobile

    def get_mobile(self):
        return self.mobile

    def set_followers(self, followers):
        self.followers = followers

    def get_followers(self):
        return self.followers

    def add_follower(self, follower):
        self.followers.append(follower)

    def remove_follower(self, follower):
        if follower in self.followers:
            self.followers.remove(follower)

    def get_username(self):
        return self.first_name + self.last_name

    def __str__(self):
        return '''first name = {}
last name = {}
age = {}
mobile number = {}
followers = {}
'''.format(self.get_first_name(), self.get_last_name(), self.get_age(), self.get_mobile(), self.followers)


def write_to_file(account):
    file = open('instagram_accounts.txt', 'a')
    file.write(account.get_username() + '\n')
    file.write(str(account) + '\n')
    file.close()


if __name__ == '__main__':
    insta_user1 = InstagramAccount("John", "Smith", "23", "1234567890")
    insta_user2 = InstagramAccount("Jack", "Jones", "21", "1267857889")
    insta_user3 = InstagramAccount("Selene", "Gomez", "28", "6547896542")
    insta_user4 = InstagramAccount("Danny", "Bose", "22", "234987654")
    insta_user5 = InstagramAccount("James", "Gordon", "29", "675438976")
    insta_user1.add_follower('James')
    insta_user1.add_follower('Danny')
    insta_user1.add_follower('Selene')
    insta_user2.add_follower('Jack')
    insta_user3.add_follower('Danny')
    insta_user4.add_follower('James')
    insta_user5.add_follower('Jack')
    print(insta_user1.get_username())
    print(insta_user1)
    print(insta_user2)
    print(insta_user3)
    print(insta_user4)
    print(insta_user5)
    write_to_file(insta_user1)
    write_to_file(insta_user2)
    write_to_file(insta_user3)
    write_to_file(insta_user4)
    write_to_file(insta_user5)
