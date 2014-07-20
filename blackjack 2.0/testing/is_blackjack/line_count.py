def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
    
print 'full:  ' + str(file_len('test_cases_full.txt'))

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
    
print 'bj:    ' + str(file_len('test_cases_bj.txt'))

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
    
print 'no_bj: ' + str(file_len('test_cases_no_bj.txt'))