import random
from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate

# Sample food data (UserID, FoodID, Rating)
food_data = [
    ('User1', 'Pizza', 5),
    ('User1', 'Burger', 4),
    ('User1', 'Sushi', 3),
    ('User2', 'Pizza', 4),
    ('User2', 'Burger', 5),
    ('User2', 'Sushi', 2),
    # Add more data here
]

# Create a Surprise Dataset
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(food_data, reader)

# Split the dataset into training and testing sets
trainset = data.build_full_trainset()

# Choose an algorithm (SVD in this case)
algo = SVD()

# Train the model
algo.fit(trainset)

# Recommend food items for a specific user
user_id = 'User1'

# Generate a list of all possible food items
all_food_items = list(set(food for _, food, _ in food_data))

# Filter out the food items the user has already rated
unrated_food_items = [food for food in all_food_items if food not in trainset.ur[trainset.to_inner_uid(user_id)]]

# Predict ratings for unrated food items
predictions = [(food, algo.predict(user_id, food).est) for food in unrated_food_items]

# Sort predictions by estimated rating in descending order
predictions.sort(key=lambda x: x[1], reverse=True)

# Get the top N recommended food items
top_n = 3
top_food_recommendations = predictions[:top_n]

# Display recommendations
print(f"Top {top_n} food recommendations for {user_id}:")
for i, (food, rating) in enumerate(top_food_recommendations):
    print(f"{i + 1}: {food} (Estimated Rating: {rating:.2f})")
