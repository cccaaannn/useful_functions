exclude_list = ["aa","bb"]
items = ["aa","bb","cc","dd","ee"]


def __exclude_list_from_list(items, exclude_list):
    for exclude in exclude_list:
        if exclude in items: 
            items.remove(exclude)
    return items


# exclude_list_from_list with filter
items = list(filter(lambda x: x not in exclude_list, items))

# exclude_list_from_list with list comprehension
items = [item for item in items if item not in exclude_list] 
