class DNS:
    def __init__(self, dns_name, IPA):
        self.dns_name = dns_name
        self.IPA = IPA

    def get_res(self):
        return self.IPA

    def __str__(self):
        return 'DNS: {}, IPA: {}\n'.format(self.dns_name, self.IPA)


if __name__ == '__main__':
    choice = 'None'
    dns_objects = []
    while choice.lower() != 'q':
        commands = input().split()
        if commands[0].lower() == 'u':
            if len(commands) == 3:
                obj = DNS(commands[1], commands[2])
                dns_objects.append(obj)
            else:
                print('Bad command')
        elif commands[0].lower() == 'l':
            for i in dns_objects:
                if i.dns_name == commands[1]:
                    print(i.get_res())
                    break
            else:
                print('None')
        elif commands[0].lower() == 'q':
            import sys
            sys.exit(0)
