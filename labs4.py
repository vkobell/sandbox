class Car:
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0  #TODO: Declare purchase_price attribute //1
        self.current_value = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)
    
    def print_info(self):
        print(f"Car's information:")
        print(f"  Model year: {self.model_year}")
        print(f"  Purchase price: ${self.purchase_price}")
        print(f"  Current value: ${self.current_value}") #TODO: Define print_info() method to output model_year, purchase_price, and current_value //2


if __name__ == "__main__":    
    year = int(input()) 
    price = int(input())
    current_year = int(input())
    
    my_car = Car()
    my_car.model_year = year
    my_car.purchase_price = price
    my_car.calc_current_value(current_year)
    my_car.print_info()
    