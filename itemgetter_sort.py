from operator import itemgetter

fall_enroll = [('MTH 165', 'GG', 18),
               ('MTH 244', 'GG', 10),
               ('MTH 169', 'AK', 20),
               ('MTH 169', 'MO', 18)]

output_list = sorted(fall_enroll, key=lambda x: (x[0], x[1], -x[2]))

print(*output_list, sep='\n')
