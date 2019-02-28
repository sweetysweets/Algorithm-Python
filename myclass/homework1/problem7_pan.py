def all_lis(nums, B, peak_index, lis, all_lis_list):
    if B[peak_index] == 1:
        lis.append(nums[peak_index])
        lis.reverse()
        all_lis_list.append(lis)
    else:
        curr_len = B[peak_index]
        lis.append(nums[peak_index])
        for i in range(peak_index):
            if B[i] == curr_len-1 and nums[i] < nums[peak_index]:
                curr_lis = lis.copy()
                all_lis(nums, B, i, curr_lis, all_lis_list)


def all_lds(nums, C, peak_index, lds, all_lds_list):
    if C[peak_index] == 1:
        lds.append(nums[peak_index])
        all_lds_list.append(lds)
    else:
        curr_len = C[peak_index]
        lds.append(nums[peak_index])
        for i in range(peak_index, len(nums)):
            if C[i] == curr_len-1 and nums[i] < nums[peak_index]:
                curr_lds = lds.copy()
                all_lds(nums, C, i, curr_lds, all_lds_list)


if __name__ == '__main__':
    nums = [int(x) for x in input().split(" ")]

    n = len(nums)
    B = [0] * n
    C = [0] * n
    for i in range(n):
        B[i] = 1
        for j in range(i):
            if nums[j] < nums[i] and B[j] + 1 > B[i]:
                B[i] = B[j] + 1

    for i in range(n - 1, -1, -1):
        C[i] = 1
        for j in range(n - 1, i - 1, -1):
            if nums[j] < nums[i] and C[j] + 1 > C[i]:
                C[i] = C[j] + 1

    max_len = 0
    div = []
    for i in range(n):
        len_i = B[i] + C[i] - 1
        if len_i > max_len:
            max_len = len_i
            div.clear()
            div.append(i)
        elif len_i == max_len:
            div.append(i)

    for peak_index in div:
        all_lis_list = []

        all_lis(nums, B, peak_index, [], all_lis_list)
        all_lds_list = []
        all_lds(nums, C, peak_index, [], all_lds_list)

        for i in range(len(all_lis_list)):
            for j in range(len(all_lds_list)):
                lis = all_lis_list[i].copy()
                lds = all_lds_list[j].copy()
                lis.extend(lds[1:])
                one = [str(x) for x in lis]
                one_str = " ".join(one)
                print(one_str)