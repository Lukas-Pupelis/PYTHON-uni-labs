from pymongo import MongoClient
import json

# Setup MongoDB connection
client = MongoClient('localhost', 27017)
db = client['mydatabase']
collection = db['restaurants']

# Load and insert JSON data into MongoDB
def load_data(filepath):
    with open(filepath, 'r') as file:
        data = [json.loads(line) for line in file if line.strip()]
        collection.insert_many(data)

# Queries
def execute_queries():
    # Query 1: Retrieve all documents
    all_documents = list(collection.find())
    print("All Documents:", all_documents)

    # Query 2: Retrieve specific fields
    specific_fields = list(collection.find({}, {'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1}))
    print("Specific Fields:", specific_fields)

    # Query 3: Exclude `_id` field
    exclude_id = list(collection.find({}, {'_id': 0, 'restaurant_id': 1, 'name': 1, 'borough': 1, 'cuisine': 1}))
    print("Exclude _id Field:", exclude_id)

    # Query 4: Filter by Borough (Bronx)
    bronx_restaurants = list(collection.find({'borough': 'Bronx'}))
    print("Bronx Restaurants:", bronx_restaurants)

    # Query 5: Filter by Grade Scores
    high_score_restaurants = list(collection.aggregate([
        {'$unwind': '$grades'},
        {'$match': {'grades.score': {'$gte': 80, '$lte': 100}}}
    ]))
    print("Restaurants with High Scores:", high_score_restaurants)

    # Query 6: Sort by Cuisine Ascending and Borough Descending
    sorted_restaurants = list(collection.find().sort([('cuisine', 1), ('borough', -1)]))
    print("Sorted by Cuisine and Borough:", sorted_restaurants)

# Main execution logic
if __name__ == '__main__':
    filepath = 'restaurants.json'  # Use relative path for the file in the same directory
    load_data(filepath)
    execute_queries()
