if __name__ == '__main__':
    f = open("mbox-short.txt", 'r')
    lines = f.readlines()
    from_mails = {}
    for i in lines:
        if i.strip().lower().startswith("from"):
            mail_type, name, mail_id = i.strip().split()
            if name in from_mails:
                from_mails[name] += 1
            else:
                from_mails[name] = 1

    maximum_count = 0
    result_name = ""
    for i in from_mails.keys():
        if from_mails[i] > maximum_count:
            maximum_count = from_mails[i]
            result_name = i

    print("The person sent maximum number of mails is {}".format(result_name))