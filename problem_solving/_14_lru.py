def lru (str):

    lru_ret = []

    for i in str:

        if i in lru_ret:
            del lru_ret[lru_ret.index(i)]
            lru_ret.append(i)
        else:
            lru_ret.append(i)
    return lru_ret

if __name__ == "__main__":
    print('-'.join(lru(["A", "B", "C", "D", "E", "D", "Q", "Z", "C"])))