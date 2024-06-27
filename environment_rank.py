def total_rank(data):
    total_rank = [data['水质类别']]
    total_rank.append(PH_rank(data['pH']))
    total_rank.append(DOC_rank(data['溶氧量']))
    total_rank.append(MNO4_rank(data['高锰酸盐指数']))
    total_rank.append(NH4_rank(data['氨氮']))
    total_rank.append(N_rank((data['总氮'])))
    return total_rank



def PH_rank(data):
    if data < 6 or data > 9:
        return 'Ⅴ'
    else:
        return 'Ⅰ'


def DOC_rank(data):
    if data > 7.5:
        return 'Ⅰ'
    elif data > 6:
        return 'Ⅱ'
    elif data > 5:
        return 'Ⅲ'
    elif data > 3:
        return 'Ⅳ'
    else:
        return 'Ⅴ'


def MNO4_rank(data):
    if data < 2:
        return 'Ⅰ'
    elif data < 4:
        return 'Ⅱ'
    elif data < 6:
        return 'Ⅲ'
    elif data < 10:
        return 'Ⅳ'
    else:
        return 'Ⅴ'


def NH4_rank(data):
    if data < 0.15:
        return 'Ⅰ'
    elif data < 0.5:
        return 'Ⅱ'
    elif data < 1.0:
        return 'Ⅲ'
    elif data < 1.5:
        return 'Ⅳ'
    else:
        return 'Ⅴ'


def N_rank(data):
    if data < 1.0:
        return 'Ⅰ'
    elif data < 2.0:
        return 'Ⅱ'
    elif data < 3.5:
        return 'Ⅲ'
    elif data < 5:
        return 'Ⅳ'
    else:
        return 'Ⅴ'
