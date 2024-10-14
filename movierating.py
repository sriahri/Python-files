ratings = {'Cruella': 7.5, 'A Quiet Place': 7.5, 'In the Heights': 8.0}

if __name__ == '__main__':
    sumr = 0
    count = 0
    for m, r in ratings.items():
        sumr += r
        count += 1

    print('Average movie rating: {:.2f}'.format(sumr / count))
