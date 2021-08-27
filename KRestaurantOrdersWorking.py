def non_empty_sum_test(current_item_price, current_index):
    new_temp_list = list_of_ways_to_sum[current_index - current_item_price][:]
    new_temp_list[item_price_list.index(current_item_price)] += 1
    if list_of_ways_to_sum[current_index] != list_of_ways_to_sum[0] and \
            new_temp_list != list_of_ways_to_sum[current_index]:
        list_of_ways_to_sum[current_index] = 'Ambiguous'
    else:
        list_of_ways_to_sum[current_index] = list_of_ways_to_sum[current_index - current_item_price][:]
        list_of_ways_to_sum[current_index][item_price_list.index(current_item_price)] += 1
input()
item_price_input = input()
item_price_list = item_price_input.split(' ')
item_price_list = [int(price) for price in item_price_list]
input()
order_total_price_input = input()
order_total_price_list = order_total_price_input.split(' ')
order_total_price_list = [int(price) for price in order_total_price_list]
largest_price = max(order_total_price_list)
list_of_ways_to_sum = [[0 for item in item_price_list] for price in range(largest_price + 1)]
for price_sum in range(largest_price + 1):
    for menu_item in [item for item in item_price_list if price_sum >= item]:
        if list_of_ways_to_sum[price_sum - menu_item] == 'Ambiguous':
            list_of_ways_to_sum[price_sum] = 'Ambiguous'
        elif list_of_ways_to_sum[price_sum - menu_item] != list_of_ways_to_sum[0]:
            non_empty_sum_test(menu_item, price_sum)

        elif price_sum == menu_item:
            if list_of_ways_to_sum[price_sum] != list_of_ways_to_sum[0]:
                list_of_ways_to_sum[price_sum] = 'Ambiguous'
            else:
                list_of_ways_to_sum[price_sum][item_price_list.index(menu_item)] += 1
for orderPrice in order_total_price_list:
    if list_of_ways_to_sum[orderPrice] == list_of_ways_to_sum[0]:
        print("Impossible")
    elif list_of_ways_to_sum[orderPrice] == 'Ambiguous':
        print("Ambiguous")
    else:
        sumToPrint = ''
        for menuItemIndex, item in enumerate(list_of_ways_to_sum[orderPrice]):
            sumToPrint += (str(menuItemIndex + 1) + ' ') * item
        print(sumToPrint.rstrip())