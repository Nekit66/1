def z1():
    class Restaurant:

        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")


    newRestaurant = Restaurant('The Blue Bistro', 'французская')

    print(f"Название ресторана: {newRestaurant.restaurant_name}")
    print(f"Тип кухни: {newRestaurant.cuisine_type}")

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()



def z2():
    class Restaurant:

        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}n")

    restaurant1 = Restaurant('The Blue Bistro', 'французская')
    restaurant2 = Restaurant('Sakura Sushi', 'японская')
    restaurant3 = Restaurant('Taqueria El Pastor', 'мексиканская')

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

def z3():
    class Restaurant:

        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f"Рейтинг: {self.rating}")

        def set_rating(self, new_rating):
            self.rating = new_rating

    restaurant = Restaurant('The Blue Bistro', 'французская', 4)

    restaurant.describe_restaurant()

    restaurant.set_rating(5)

    restaurant.describe_restaurant()


z3()