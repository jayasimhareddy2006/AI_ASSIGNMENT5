# ==========================================
# KNOWLEDGE GRAPH PROJECT
# ==========================================
knowledge_graph = {
    "Hyderabad": {

        "hasPlace": [
            "Charminar",
            "Golconda Fort",
            "Ramoji Film City"
        ],
        "hasFood": [
            "Hyderabadi Biryani",
            "Haleem"
        ],

        "locatedIn": "Telangana"
    },

    "Goa": {
        "hasPlace": [
            "Baga Beach",
            "Fort Aguada"
        ],
        "hasFood": [
            "Fish Curry",
            "Prawn Fry"
        ],
        "locatedIn": "Goa"
    },

    "Delhi": {
        "hasPlace": [
            "India Gate",
            "Red Fort"
        ],
        "hasFood": [
            "Chole Bhature",
            "Butter Chicken"
        ],
        "locatedIn": "Delhi"
    }
}

print("\n===================================")
print("KNOWLEDGE GRAPH")
print("===================================")

for city in knowledge_graph:
    print("\nEntity:", city)
    for relation in knowledge_graph[city]:

        print(
            relation,
            "->",
            knowledge_graph[city][relation]
        )

print("\n===================================")
