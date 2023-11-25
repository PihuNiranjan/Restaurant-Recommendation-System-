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

    return recommended_restaurants



# Function of Running Test cases
def run_test_cases():
    test_cases = [
        {"food_type": "Italian", "rating": 4.9},   #-----> Non-existent cuisine
        {"food_type": "Mexican", "rating": 3.5},
        {"food_type": "Indian", "rating": 4.7},
        {"food_type": "Chinese", "rating": 4.0},  
    ]

    for i, test_case in enumerate(test_cases, start=1):
        food_type = test_case["food_type"]
        rating = test_case["rating"]

        recommendations = recommend_restaurants(food_type, rating)
        if recommendations:
            print(f"\nTest Case {i}: Recommended restaurants serving {food_type.capitalize()} cuisine with ratings >= {rating}:")
            for id, restaurant in enumerate(recommendations, start=1):
                print(f"{id}. {restaurant}")
        else:
            print(f"\nTest Case {i}: Sorry, no restaurants found serving {food_type.capitalize()} cuisine with ratings >= {rating}.")

# Run test cases
run_test_cases()