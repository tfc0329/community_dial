data = [
    {"timestamp": "2024-11-24T19:00:00Z", "category": "Commercial", "typology": "Supermarkets", "keywords": ["fresh produce", "discounts"]},
    {"timestamp": "2024-11-10T14:30:00Z", "category": "Commercial", "typology": "Restaurants", "keywords": ["fast food", "family-friendly"]},
    {"timestamp": "2024-11-15T10:00:00Z", "category": "Public Spaces", "typology": "Parks", "keywords": ["green space", "playground"]},
    {"timestamp": "2024-11-20T16:45:00Z", "category": "Public Spaces", "typology": "Playgrounds", "keywords": ["swings", "slides"]},
    {"timestamp": "2024-12-05T10:15:00Z", "category": "Retail Spaces", "typology": "Boutiques", "keywords": ["luxury", "handmade"]},
    {"timestamp": "2024-12-10T11:30:00Z", "category": "Commercial", "typology": "Supermarkets", "keywords": ["organic", "bulk items"]},
    {"timestamp": "2024-12-20T15:00:00Z", "category": "Retail Spaces", "typology": "Malls", "keywords": ["shopping center", "clothing"]}
]

from collections import defaultdict
from datetime import datetime
import json

# Initialize nested defaultdict
result = defaultdict(lambda: {"categories": defaultdict(lambda: {"typologies": defaultdict(lambda: {"count": 0, "keywords": defaultdict(int)})})})

# Process the data
for entry in data:
    # Extract the month-year
    month_year = datetime.fromisoformat(entry["timestamp"].replace("Z", "")).strftime("%Y-%m")
    category = entry["category"]
    typology = entry["typology"]
    keywords = entry["keywords"]

    # Increment the count for the typology
    result[month_year]["categories"][category]["typologies"][typology]["count"] += 1

    # Track keyword frequency
    for keyword in keywords:
        result[month_year]["categories"][category]["typologies"][typology]["keywords"][keyword] += 1

# Convert to a regular dictionary
final_data = {
    month: {
        "categories": {
            category: {
                "typologies": {
                    typology: {
                        "count": data["count"],
                        "keywords": dict(data["keywords"])
                    }
                    for typology, data in details["typologies"].items()
                }
            }
            for category, details in month_details["categories"].items()
        }
    }
    for month, month_details in result.items()
}

# Save to a JSON file
with open("monthly_frequency_with_keywords.json", "w") as file:
    json.dump(final_data, file, indent=4)

print("Data processed and saved with keywords!")
