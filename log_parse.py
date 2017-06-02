#!/usr/bin/python3
import re
"""
Parse a log file in a given format.
Part 1: Based on date and time get a count of total messages
"""
def log_parse1(filename):
    dates_dic = {}
    with open(filename, 'r') as content:
        lines = content.readlines()
        for line in lines:
            tokens = re.split(" ", line, maxsplit=3)
            key = tokens[0] + " " + tokens[1] + " " + tokens[2][:5]
            if key in dates_dic:
                dates_dic[key] += 1
            else:
                dates_dic[key] = 1

    # returning for using in the next function
    return dates_dic

"""
Part 2: The idea is to make a dictionary of processes, where name of the process
will be key and its value will be a dictionary of dates where each unique date
will be a key and its value will be the count i.e. the number of times each date
is repeating.
"""
def log_parse2(filename):
    process_dic = {}
    with open(filename, 'r') as content:
        lines = content.readlines()
        for line in lines:
            tokens = re.split(" ", line, maxsplit=4)
            # from tokens take out process
            key = tokens[4].split()[0]
            date_time = tokens[0] + " " + tokens[1] + " " + tokens[2][:5]
            if key in process_dic:
                # get value of the key
                value = process_dic[key]
                # check if date_time is added or its a new date_time
                if date_time in value:
                    value[date_time] += 1
                else:
                    value[date_time] = 1
            else:
                # initialize a dictionary with new date_ti,e entry
                process_dic[key] = {date_time:1}

    """
    for the first printing part, use the first dictionary with dates as keys
    and values as count.
    for second part, iterate on the process_dic and get each each process count
    based on dates
    """
    dates_dic = log_parse1(filename)

    msg = "timestamp,totalmessages,"
    for key in process_dic.keys():
        msg += key + ","
    print(msg[:-1])

    dates_dic = sorted(dates_dic.items(), key=lambda x:x[0])
    for date in dates_dic:
        msg = date[0] + "," + str(date[1]) + ","
        for key,val in process_dic.items():
            # get dictionary of date_time and find the date and its count
            if date[0] in process_dic[key]:
                msg += str(process_dic[key][date[0]]) + ","
            else:
                # if no date in the dictionary, put 0
                msg += "0,"
        print(msg[:-1])


if __name__ == "__main__":
    log_parse2('log')


"""
output:
Jun 2 10:01,9,3,6,0
Jun 2 10:02,3,0,0,3
Jun 2 10:03,3,3,0,0
"""
