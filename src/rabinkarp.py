def build_hash(s):
    s_hash = 0
    for i, c in enumerate(s):
        s_hash += pow(26, len(s) - i - 1) * (ord(c) - 96)

    return s_hash


def calculate_hash(hs, nc, oc, l):
    return 26 * (hs - (pow(26, l - 1) * (ord(oc) - 96))) + (ord(nc) - 96)


def find_matches_rabinkarp(str, substr):
    substr_len = len(substr)
    substr_hash = build_hash(substr)

    start_str = str[0:substr_len]

    res = []

    n_hash = build_hash(str[0:substr_len])

    if substr_hash == n_hash:
        res.append(0)

    ei = substr_len

    while ei < len(str):
        n_hash = calculate_hash(n_hash, str[ei], str[ei - substr_len], substr_len)

        if n_hash == substr_hash:
            if str[ei - substr_len + 1 : ei + 1] == substr:
                res.append(ei - substr_len + 1)
        ei += 1

    return res


def find_matches(str, substr):
    si = 0
    ei = len(substr)
    result = []
    while ei <= len(str):
        s = str[si:ei]
        if s == substr:
            result.append(si)

        si += 1
        ei += 1

    return result
