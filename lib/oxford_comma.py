def oxford_comma(items):
    # if length of list is 2+, change the last item to "and item"
    if len(items) > 1:
        items[-1] = "and " + items[-1]

    # if length of list is 3+, convert to string and add commas
    if len(items) > 2:
        return ", ".join(items)

    # if length is not greater than 1, convert to string
    else:
        return " ".join(items)
