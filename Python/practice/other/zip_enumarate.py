

if __name__=='__main__':
    ids = [1,2,3]
    names = ['a','b','c']
    for id, name in zip(ids,names):
        print((id,name))

    ages = [12,13,14,15]
    for age, pos in enumerate(ages):
        print((age,pos))

    # BELOW IS BAD : range(len
    for i in range(len(ages)):
        print((i,ages[i]))
    for i in ages.iter
    persons = {
        'x': 10,
        'y': 20,
        'z': 30
    }
    for k,v in persons.items():
        print((k,v))