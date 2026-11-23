def word_count_dict(sentences: list) -> dict:
    d={}

    lst=[j for i in sentences for j in i]

    for i in lst:
        d[i]=lst.count(i)


    return d