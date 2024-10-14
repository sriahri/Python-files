def domain_count():
    domain_list = {}
    mail_list = list(map(str, input().split(', ')))
    for i in range(len(mail_list)):
        mail = mail_list[i]
        user, domain = mail.split('@')
        domain = domain.replace('.com', '')
        if domain in domain_list:
            domain_list[domain] += 1
        else:
            domain_list[domain] = 1
    for domain, count in domain_list.items():
        print('{} - {}'.format(domain, count))


if __name__ == '__main__':
    domain_count()