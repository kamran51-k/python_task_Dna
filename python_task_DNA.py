def DNA():
    string1 = input('bir metn daxil edin: ')
    string2 = input('bir metn daxil edin: ')
    choose = input('bir element secin: add,minus ')
    if choose == 'add':
        add1 = input(' dash(-) hansi stringe elave olunsun? string1 yoxsa string2: ')
        add_index = int(input('secilen stringde hansi indekse artirsin?: '))
        if len(string1)-1 < add_index or len(string2)-1 < add_index:
                print('error')  
        elif add1 == 'string1':
            c = string1[:add_index] + '-' + string1[add_index:]
            print(c)
        elif add1 == 'string2':
            d = string2[:add_index] + '-' + string2[add_index:]
            print(d)
    if choose == 'minus':
        minus1 = input('hansi stringden silinsin? string1 yoxsa string2: ')
        remove_index = int(input('hansi indexden dashi silmek istiyirsiniz?: '))
        if len(string1)-1 < remove_index or len(string2)-1 < remove_index:
            print('error')
        elif minus1 == 'string1':  
            replace_string= string1.replace('-','')
            print(replace_string)
        elif minus1 == 'string2':  
            replace_string1 = string2.replace('-','')
            print(replace_string1)
DNA()            