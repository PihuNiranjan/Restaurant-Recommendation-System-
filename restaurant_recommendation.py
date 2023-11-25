# Simulated restaurant data (name, cuisine, ratings)
restaurants = [
    {"name": "Restaurant A", "cuisine": "Italian", "ratings": 4.5},
    {"name": "Restaurant B", "cuisine": "Mexican", "ratings": 4.0},
    {"name": "Restaurant C", "cuisine": "Indian", "ratings": 4.8},
    {"name": "Restaurant D", "cuisine": "Italian", "ratings": 4.2},
    {"name": "Restaurant E", "cuisine": "Mexican", "ratings": 3.7},
    {"name": "Restaurant F", "cuisine": "Indian", "ratings": 4.6},
    {"name": "Restaurant G", "cuisine": "Chinese", "ratings": 4.3},
    {"name": "Restaurant H", "cuisine": "Seafoods", "ratings": 4.8},

    
    # Add more restaurants with their respective details
]

#function for recommendations the favourite resturants
def recommend_restaurants(foodtype, minrating):
    recommended_restaurants = []
    for restaurant in restaurants:
        if foodtype.capitalize() == restaurant["cuisine"].capitalize() and restaurant["ratings"] >= minrating:
            recommended_restaurants.append(restaurant["name"])

    if recommended_restaurants:
        print(f"\nRecommended restaurants serving {foodtype.capitalize()} cuisine with ratings >= {minrating}:")
        for i, restaurant in enumerate(recommended_restaurants, start=1):
            print(f"{i}. {restaurant}")
    else:
        print(f"Sorry, no restaurants found serving {foodtype.capitalize()} cuisine with ratings >= {minrating}.")

# Example usage
print("\n\t Welcome To KHAOO PEEO\n")
user_food_type = input("Enter the type of food: ")
user_min_rating = float(input("\nEnter your minimum preferred rating (from 1 to 5): "))

recommend_restaurants(user_food_type, user_min_rating)
