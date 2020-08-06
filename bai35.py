def dictTest2():
    dict2 = dict()
    for i in range(1, 21):
        dict2[i] = i*i
    return dict2.keys()

print(dictTest2())