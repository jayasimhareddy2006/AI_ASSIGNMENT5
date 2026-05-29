# ==========================================
# AI BASED TRAVEL PLANNER
# ==========================================
tourist_places = {
    "Goa": [
        "Baga Beach",
        "Calangute Beach",
        "Fort Aguada",
        "Dona Paula",
        "Anjuna Beach"
    ],

    "Hyderabad": [
        "Charminar",
        "Golconda Fort",
        "Ramoji Film City",
        "Hussain Sagar",
        "Birla Mandir"
    ],

    "Delhi": [
        "India Gate",
        "Red Fort",
        "Qutub Minar",
        "Lotus Temple",
        "Akshardham"
    ],

    "Bangalore": [
        "Lalbagh Garden",
        "Cubbon Park",
        "Bangalore Palace",
        "ISKCON Temple",
        "Bannerghatta Zoo"
    ]
}

food_recommendations = {

    "Goa": [
        "Fish Curry",
        "Prawn Fry",
        "Bebinca",
        "Vindaloo"
    ],

    "Hyderabad": [
        "Hyderabadi Biryani",
        "Haleem",
        "Double Ka Meetha"
    ],

    "Delhi": [
        "Chole Bhature",
        "Butter Chicken",
        "Paratha"
    ],

    "Bangalore": [
        "Masala Dosa",
        "Idli",
        "Vada",
        "Bisi Bele Bath"
    ]
}

daily_cost = {

    "Goa": 6000,
    "Hyderabad": 4000,
    "Delhi": 5000,
    "Bangalore": 4500
}


# ==========================================
# DISPLAY KNOWLEDGE BASE
# ==========================================

def show_destinations():

    print("\nAvailable Destinations:")

    for city in tourist_places:
        print("-", city)


# ==========================================
# TRAVEL PLANNER
# ==========================================

def plan_trip():

    print("\n===================================")
    print("AI BASED TRAVEL PLANNER")
    print("===================================")
    show_destinations()
    destination = input(
        "\nEnter Destination: "
    ).strip()
    if destination not in tourist_places:
        print("\nDestination not found.")
        return
    budget = int(
        input("Enter Budget (₹): ")
    )
    days = int(
        input("Enter Number of Days: ")
    )
    estimated_cost = (
        daily_cost[destination] * days
    )
    print("\n===================================")
    print("PERSONALISED TRAVEL PLAN")
    print("===================================")

    print("\nDestination:")
    print(destination)

    print("\nTourist Places:")

    for i, place in enumerate(
            tourist_places[destination],
            start=1):

        print(f"{i}. {place}")

    print("\nFood Recommendations:")

    for i, item in enumerate(
            food_recommendations[destination],
            start=1):

        print(f"{i}. {item}")
    print("\nTrip Duration:")
    print(days, "Days")

    print("\nEstimated Cost:")
    print("₹", estimated_cost)

    if budget >= estimated_cost:

        print(
            "\n✓ Trip is within your budget."
        )
        print(
            "Remaining Budget: ₹",
            budget - estimated_cost
        )
    else:
        print(
            "\n✗ Budget is insufficient."
        )
        shortage = (
            estimated_cost - budget
        )
        print(
            "Additional Amount Needed: ₹",
            shortage
        )
    print("\n===================================")
# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":
    while True:
        plan_trip()
        choice = input(
            "\nPlan another trip? (y/n): "
        ).lower()
        if choice != "y":
            print(
                "\nThank you for using AI Travel Planner."
            )
            break
