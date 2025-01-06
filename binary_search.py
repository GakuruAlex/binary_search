from typing import List
def binary_search(cards: List[int], query: int)-> int:
    """_Determine the index of a given number in a list of sorted integers in descending order_

    Args:
        cards (List[int]): _List of integers in descending order_
        query (int): _Number whose position is to be determined_

    Returns:
        int: _Position of the given number_
    """
    low, high = 0, len(cards) - 1
    mid = (high - low) // 2
    while mid < len(cards):
        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            high = mid
        else:
            low = mid
        
    return -1