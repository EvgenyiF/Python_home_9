def get_separ(a):
    
    if a == 1:
        return "\n"
    if a == 2:
        return ":"
    if a == 3:
        return "-"
    if a == 4:
        return "*"
    # raise ValueError('Undefined unit: {}'.format(a))