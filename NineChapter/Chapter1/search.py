# -*- coding: utf-8 -*-

# Subset
def subset(full_set):
    if len(full_set) == 0:
        return []

    result = []
    subset_helper(result, [], full_set, 0)
    return result


def subset_helper(result, cur_sub, full_set, pos):
    result.append(cur_sub[:])

    for i in range(pos, len(full_set)):
        cur_sub.append(full_set[i])
        subset_helper(result, cur_sub, full_set, i + 1)
        cur_sub.pop()


# Unique Subset
def uniq_subset(full_set):
    if len(full_set) == 0:
        return []

    result = []
    full_set = sorted(full_set)
    uniq_subset_helper(result, [], full_set, 0)
    return result


def uniq_subset_helper(result, cur_sub, full_set, pos):
    result.append(cur_sub[:])

    for i in range(pos, len(full_set)):
        if i != pos and full_set[i] == full_set[i - 1]:
            continue

        cur_sub.append(full_set[i])
        uniq_subset_helper(result, cur_sub, full_set, i + 1)
        cur_sub.pop()


# Permutations
def permutations(full_set):
    if len(full_set) == 0:
        return []

    result = []
    permutations_helper(result, [], [], full_set)
    return result


def permutations_helper(result, cur_p, used_pos, full_set):
    if len(cur_p) == len(full_set):
        result.append(cur_p[:])
        return

    for i in range(0, len(full_set)):
        if i in used_pos:
            continue

        cur_p.append(full_set[i])
        used_pos.append(i)
        permutations_helper(result, cur_p, used_pos, full_set)
        cur_p.pop()
        used_pos.pop()

# N Queens


# Palindrome Partitioning


# Combination Sum


# Combination Sum II


# Word Ladder


# Word Ladder II


# 拓扑排序


if __name__ == "__main__":
    input_set = [1, 2, 2]
    res = subset(input_set)
    print res

    res = uniq_subset(input_set)
    print res

    input_set = [1, 2, 3]
    res = permutations(input_set)
    print res
