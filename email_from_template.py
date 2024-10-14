if __name__ == '__main__':
    template = open("email_template.txt", 'r')
    emails = open("emails.csv", 'r')
    lines = template.readlines()
    mail = emails.readlines()
    for i in mail:
        mail_template = ''.join(lines)
        name, mail_id = map(str, i.split(','))
        mail_template = mail_template.replace('{email}', mail_id.strip('\n'))
        mail_template = mail_template.replace('{first_name}', name.title())

        print(mail_template)
        print()
