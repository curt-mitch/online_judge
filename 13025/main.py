import sys
import datetime


if __name__ == '__main__':
    date = '29/05/2013'
    day, month, year = map(int, date.split('/'))
    d = datetime.datetime(year, month, day)
    formatted_date = d.strftime('%B %d, %Y %A')
    print(formatted_date)
exit(0)
