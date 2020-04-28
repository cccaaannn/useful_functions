def __exclude_list_from_list(items, exclude_list):
    for exclude in exclude_list:
        if exclude in items: 
            items.remove(exclude)
    return items

def __exclude_list_from_list2(items, exclude_list):
    items = list(filter(lambda x: x not in exclude_list, items))
    return items