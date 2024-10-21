import itertools

def combine(primary_list: list[str], secondary_list: list[str], separator: str = " ") -> list[str]:
    """
    Combine two lists into a single list with a separator.
    
    Args:
        primary_list (list[str]): The first list.
        secondary_list (list[str]): The second list.
        separator (str, optional): The separator used to join elements. Defaults to a space (" ").

    Returns:
        list[str]: The combined list.
    """
    if not primary_list or not secondary_list:
      return primary_list or secondary_list
    return [f"{item1}{separator}{item2}" for item1, item2 in itertools.product(primary_list, secondary_list)]

def split_number(number: str) -> list[str]:
    """
    Split a number string into parts according to the Indian numbering system.

    Args:
        number (str): The number to split.

    Returns:
        list[str]: The list of constituent parts.
    """
    length = len(number)
    parts = [number[-3:]] + [
        number[max(length - i - 2, 0):length - i] for i in range(3, min(length, 9), 2)
    ]

    if length > 9:
        parts += [number[:length - 9][::-1][i:i + 1][::-1] for i in range(len(number[:-9]))]

    return list(filter(None, parts))

