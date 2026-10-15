def rank_transform(values: list) -> list:
    x = sorted(values)
    rank = {}
    c = 1

    for i in sorted(set(x)):
        count = x.count(i)
        rank[i] = (c + c + count - 1) / 2
        c += count

    return [rank[k] for k in values]