class Order:
    def __init__(self):
        self.total_cost = 0
        self.items = []

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))

        print('Here are your items: ', end = '')
        print(*self.items, sep = ', ')

    # implement methods for menu items
    def add_cookie()
        print('cookie hass been added')
        total_cost += 1.50
        self.items += ["cookie"]
