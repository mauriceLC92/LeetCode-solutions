from typing import List


def maximumWealth(accounts: List[List[int]]) -> int:
    account_totals = []

    for account in accounts:
        account_totals.append(sum(account))

    return max(account_totals)


accounts = [[1, 2, 3], [3, 2, 1]]

# maximumWealth(accounts)


"""
Nice one liner solution
"""


def maximumWealth(accounts: List[List[int]]) -> int:
    return max(map(sum, accounts))
