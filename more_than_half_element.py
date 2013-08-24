#!/usr/bin/python
#encoding:utf8


def more_than_half_element(list):
    count = 0
    candidate = ''
    for element in list:
        if count = 0:
            candiate = element
            count = 1
        else:
            if element != candiate:
                count = count -1
            else:
                count = count + 1
    return count > 0
