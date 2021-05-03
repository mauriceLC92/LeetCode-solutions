def kidsWithCandies(candies, extraCandies):
    candie_tracker = []
    for value in candies:
        if value + extraCandies >= max(candies):
            candie_tracker.append(True)
        else:
            candie_tracker.append(False)

    return candie_tracker


candies = [12, 1, 12]
extraCandies = 10

kidsWithCandies(candies, extraCandies)