# Global Constant
_calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,
             "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
             "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102
             }


# Input loop
def addFood():
    new_item = input("Enter food item to add, or ’q’ to exit: ")
    while new_item != "q":
        new_item_calories = int(input("Enter calories for " + new_item + ": "))
        _calories[new_item] = new_item_calories

        def add_calories(_calories):
            total_calories = 0
            for item in _calories:
                total_calories = total_calories + _calories[item]
            return total_calories

        def foodnamer(_calories):
            food_item_names = []
            for item in _calories:
                food_item_names.append(item)
            return food_item_names

        total_calories = add_calories(_calories)
        avg_calories = total_calories / len(_calories)

        print("\nFood Items:", sorted(foodnamer(_calories)))
        print("Total Calories:", total_calories,
              "\nAverage Calories: %0.1f\n" % avg_calories)
        new_item = input("Enter food item to add, or ’q’ to exit: ")


def main():
    addFood()


if __name__ == "__main__":
    main()
