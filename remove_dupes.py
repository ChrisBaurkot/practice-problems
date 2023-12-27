stocks = ["Apple", "Sony", "Nike", "Samsung", "Disney", "Apple", "Sony","Peloton", "Chipotle", "Chipotle"]
letters = ['a', 'b', 'a', 'c', 'l', 'c']

def drop_dupes(list):
    # loop through the list
    # drop duplicates from the list
    # return the list without duplicates

    for x in list:
        count = list.count(x)

        if count > 1:
            for i in range(count - 1):
                list.remove(x)

    return list

print(drop_dupes(stocks))
print(drop_dupes(letters))