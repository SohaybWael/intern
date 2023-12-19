#1 - Definition : A peak is a pattern in an array where there is a sequence of adjacent integers that are strictly increasing until they reach a peak (highest value), and then they become strictly decreasing.
#2 - Requirements for a Peak : To form a peak, at least three integers are required. This is because you need a minimum of one strictly increasing element, the peak, and one strictly decreasing element after the peak.
#3 - Example of a Peak : For example, the integers 1, 4, 10, 2 form a peak because : 
    #a) 1 < 4 < 10 (strictly increasing)
    #b) 10 is the peak
    #c) 10 > 4 > 1 (strictly decreasing)


def longestPeak(array):
    longest_peak = 0
    peak_itself = []
    for i in range(1, len(array) - 1):
        is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not is_peak:
            continue
        left = i - 2
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1
        right = i + 2
        while right < len(array) and array[right] < array[right - 1]:
            right += 1
        current_peak_itself = array[left + 1:right]
        if len(current_peak_itself) > len(peak_itself):
            peak_itself = current_peak_itself
        current_peak = right - left - 1
        longest_peak = max(longest_peak, current_peak)
    return longest_peak, peak_itself





print(longestPeak([1, 2, 3, 3, 4, 4, -3, 2, 3, 0]))