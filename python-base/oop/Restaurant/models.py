"""Classes storage"""
from datetime import datetime


class Restaurant:
    """main class for Restaurant"""

    def __init__(self):
        self.work_time = {
            "Monday": {"open": [12, 00], "close": [22, 00]},
            "Tuesday": {"open": [12, 00], "close": [22, 00]},
            "Wednesday": {"open": [12, 00], "close": [22, 00]},
            "Thursday": {"open": [12, 00], "close": [22, 00]},
            "Friday": {"open": [12, 00], "close": [22, 00]},
            "Saturday": {"open": [10, 00], "close": [23, 00]},
            "Sunday": {"open": [10, 00], "close": [23, 00]},
        }
        self.restaurant_name = "Oie bien Nourrie"
        self.budget = 420_000
        self.work_status = False
        self.change_restaurant_status()

    def change_restaurant_status(self):
        """Change restaurant status"""
        now = datetime.now()
        weekday = datetime.today().strftime("%A")

        open_time = now.replace(hour=self.work_time[weekday]['open'][0],
                                minute=self.work_time[weekday]['open'][1])

        close_time = now.replace(hour=self.work_time[weekday]['close'][0],
                                 minute=self.work_time[weekday]['close'][1])

        self.time_checker(open_time, now, close_time)

    def time_checker(self, open_time, now, close_time):
        """Time checker"""
        if open_time < now < close_time:
            self.work_status = True
        else:
            self.work_status = False



class RestaurantHall(Restaurant):
    """Class of Restaurant Hall"""

    def __init__(self):
        super().__init__()
        self.amount_tables = 17
        self.amount_visitors = 0

    def add_visitors(self, visitors: int):
        """Add visitors to restaurant"""
        if self.work_time:
            if self.get_free_table > 0:
                if self.get_free_table - int(visitors) >= 0:
                    self.amount_visitors += int(visitors)
                    res = 1
                else:
                    print(f'To mani visitors. We have only {self.get_free_table} tables')
                    res = 2
            else:
                print('Sorry, no free tables.')
                res = 3
        else:
            print('Restaurant is closet now')
            res = 5
        return res

    def pop_visitors(self, visitors: int):
        """Visitor leave restaurant"""

        if self.amount_visitors - visitors >= 0:
            self.amount_visitors -= visitors
            print("We were glad to see you, come again!")
        else:
            print("A children was born in the restaurant!")
            self.amount_visitors = 0

    @property
    def get_free_table(self) -> int:
        """Get free table"""
        free_table = self.amount_tables - self.amount_visitors
        return free_table


class FoodStorage(Restaurant):
    """Class for Food Storage"""

    def __init__(self):
        super().__init__()
        self.food_list = {
                        "fish": {'amount': 10, 'price': 250, 'freshness': True},
                        "beef": {'amount': 20, 'price': 170, 'freshness': True},
                        "pork": {'amount': 5, 'price': 120, 'freshness': True},
                        "potato": {'amount': 20, 'price': 25, 'freshness': True},
                        "onion": {'amount': 7, 'price': 11, 'freshness': True},
                        "flour": {'amount': 20, 'price': 30, 'freshness': True},
                        "cereals": {'amount': 25, 'price': 32, 'freshness': True},
                        "butter": {'amount': 8, 'price': 90, 'freshness': True},
                        "dairy_products": {'amount': 35, 'price': 400, 'freshness': True},
                        "fruits": {'amount': 16, 'price': 90, 'freshness': True},
                        "alcohol": {'amount': 420, 'price': 200, 'freshness': True}
                    }

    def add_products(self, products: dict):
        """products -> dict:
        products{
        'amount': int(),
        'freshness': Bool,
        'price': int()}
        """
        name = list(products)[0]
        if products["freshness"]:
            # Good price or no
            if self.food_list.get(name, False):
                min_coef = self.food_list[name]["price"]
                max_coef = self.food_list[name]["price"] * 1.1
                if min_coef < products["price"] < max_coef:
                    if products["price"] < self.budget:
                        print("Good price< take all!")
                        self.food_list[name]["amount"] += products["amount"]
                    else:
                        print("I don't have enough money")
                else:
                    print("Too expensive")
            else:
                if products["price"] < self.budget:
                    print("Good price< take all!")
                    self.food_list[name] = {'amount': products["amount"],
                                            'price': products["price"],
                                            'freshness': True}

                else:
                    print("I don't have enough money")
        else:
            # Buy for half price
            if products["price"] == self.food_list[name]["price"] / 2:
                print("Ok, we will buy")
                if self.food_list.get(name, False):
                    self.food_list["amount"] += products["amount"]
                else:
                    self.food_list[name] = {'amount': products["amount"],
                                            'price': products["price"],
                                            'freshness': False}
            else:
                print("How dare you suggest that to us?")

    def pop_products(self, product: str, amount: int):
        """take product from food storage"""

        if product in self.food_list:
            if self.food_list[product]["amount"] >= amount:
                print(f"You took {amount} of {product}")
                self.food_list[product]["amount"] -= amount
            else:
                templ = self.food_list[product]["amount"]
                print(f'Not enough of {product}. Is storage only {templ}')
        else:
            print("This product is not in storage")


class Kitchen(Restaurant):
    """Kitchen class"""

    def __init__(self):
        super(Kitchen, self).__init__()
        self.current_dish = None
        self.kitchenware = {"cup": 70,
                            "bowl": 20,
                            "glass": 50,
                            "plate": 50,
                            "saucer": 20,
                            }
        self.dirty_dishes = {}
        self.current_dish = []

    def take_order(self, dish: list):
        """takle order"""
        self.current_dish = dish

    def make_food(self, customers: int):
        """Make food"""
        res = False
        if self.current_dish and customers > 0:
            i = 0
            while i < customers:
                for key in self.kitchenware.items():
                    if self.kitchenware[key[0]] > 0:
                        self.kitchenware[key[0]] -= 1
                        # make dirty dish
                        if key in self.dirty_dishes:
                            self.dirty_dishes[key[0]] += 1
                        else:
                            self.dirty_dishes[key[0]] = 1
                    else:
                        print(f"All {key} is dirty! We need wash kitchenware!")
                        self.wash_up()
                i += 1
            food = self.current_dish.pop()
            res = food

        else:
            print("Didn't order anything, bring your order first!")
        return res

    def wash_up(self):
        """Wash kitchenware"""

        if len(self.dirty_dishes) > 0:
            for dish, amount in self.dirty_dishes.items():
                self.kitchenware[dish] += amount
            self.dirty_dishes = {}
            print("All kitchenware is clear!")
        else:
            print('Nothing to wash. All kitchenware is clear!')


class Employees:
    """main class for staff"""

    def __init__(self):
        self.name = str()
        self.salary = int()
        self.position = str()
        self.timetable = {
            "Monday": {"begin": [00, 00], "finish": [00, 00]},
            "Tuesday": {"begin": [00, 00], "finish": [00, 00]},
            "Wednesday": {"begin": [00, 00], "finish": [00, 00]},
            "Thursday": {"begin": [00, 00], "finish": [00, 00]},
            "Friday": {"begin": [00, 00], "finish": [00, 00]},
            "Saturday": {"begin": [00, 00], "finish": [00, 00]},
            "Sunday": {"begin": [00, 00], "finish": [00, 00]},
        }
        self.status = None

    def add_employer(self):
        """Add employer"""
        self.status = True

    def fire_employer(self):
        """ Fire employer"""
        self.status = False


class Chef(Employees):
    """Class fo Chef
    his name Grzegorz Bzhenchishchikiewicz"""

    def __init__(self, name, salary):
        super().__init__()
        self.name = name
        self.salary = salary
        self.position = 'chef'
        self.menu = None

    def make_menu(self, food_storage) -> dict:
        """Create a menu from products available in the warehouse
        food_storage: <models.FoodStorage object>"""

        menu = dict()

        for food, value in food_storage.items():
            amount, price, _ = value.values()
            menu[food] = {'price':  price * 3, "amount": amount / 10}
        self.menu = menu
        return menu

    def make_dishes(self, dish_name: str) -> bool:
        """Make dish"""
        res = False
        if dish_name in self.menu:
            res = True
        return res


class Cook(Employees):
    """Class fo Cook"""

    def __init__(self, name, salary):
        super().__init__()
        self.name = name
        self.salary = salary
        self.position = 'cook'
        self.current_dish = None

    def cook_food(self, dish_name):
        """Cook cooks food :-)"""
        self.current_dish = dish_name


class Waiter(Employees):
    """Class fo Waiter"""

    def __init__(self, name, salary):
        super().__init__()
        self.name = name
        self.salary = salary
        self.position = 'waiter'
        self.order_list = []

    def take_order(self, order_list: tuple) -> bool:
        """Take oder from customer
        order_list: tuple = ('dish', 'customer_name')"""
        self.order_list = order_list
        return True

    def delivery_order(self, order_list):
        """Delivery order to customer"""

        if order_list in self.order_list:
            self.order_list.remove(order_list)
            res = True
        else:
            res = False
            print('The dish is not ready yet')
        return res


class Delivery:
    """Delive order"""

    def __init__(self, order):
        self.order = order

    def send_order(self):
        """Send order"""
        res = self.create_order()
        return res

    def create_order(self):
        """ Create order"""
        res = self.order
        return res



class Customer:
    """Class of Customer"""

    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

    @staticmethod
    def make_order(menu):
        """Make order"""
        return menu

    def add_phone(self, phone):
        """Add phone"""
        self.phone = phone


class AccessibleMenu:
    """Accessible Menu"""

    def __init__(self, menu):
        self.menu = menu

    def get_menu(self):
        """Get menu
        Creates a dictionary in which the key is the number and the argument is the name of the dish
        """
        res = self.create_menu()
        return res

    def create_menu(self):
        """Create menu"""

        num_menu = {}
        for num, key in enumerate(self.menu):
            print(f"{num}. {key} price:{self.menu[key]['price']} ")
            num_menu[num] = key
        return num_menu


class Order:
    """Order class"""

    def __init__(self, customer):
        self.order = []
        self.customer = customer

    def send_to_customer(self):
        """Send order to customer"""
        print(f'Its dish for {self.customer}')

    @staticmethod
    def send_to_kitchen():
        """Send order to kitchen"""
        print('Kitchen take you order/')
