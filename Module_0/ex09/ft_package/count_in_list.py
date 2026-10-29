"""Provide a helper that counts occurrences in a list."""


def count_in_list(lst, item):
    """Return how many times item appears in lst."""
    return sum(1 for x in lst if x == item)
