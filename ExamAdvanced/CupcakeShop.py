def stock_availability(my_list, action, *args):
    sell_products = []
    if action == 'delivery':
        for el in args:
            my_list.append(el)

    elif action == 'sell':
        if not args:
            my_list.pop(0)

        for el in args:
            sell_products.append(el)

        for el in sell_products:
            if str(el).isdigit():
                while el:
                    my_list.pop(0)
                    el -= 1
            else:
                while el in my_list:
                    my_list.remove(el)

    return my_list