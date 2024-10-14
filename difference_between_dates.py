s1 = input()
s2 = input()

date1 = int(s1.split('/')[0])
month1 = int(s1.split('/')[1])
year1 = int(s1.split('/')[2])
date2 = int(s2.split('/')[0])
month2 = int(s2.split('/')[1])
year2 = int(s2.split('/')[2])
diff_year = year2 - year1
diff_month = month2 - month1
diff_days = date2 - date1
print(str(diff_year)+'Y', str(diff_month)+'M', str(diff_days)+'D')