# Travel Planner - Python OOP Project

class Destination:
    def __init__(self, city, country):
        self.city = city
        self.country = country

    def show_destination(self):
        print(self.city + ", " + self.country)


class Trip:
    def __init__(self, trip_id, destination, days, budget):
        self.trip_id = trip_id
        self.destination = destination
        self.days = days
        self.budget = budget

    def show_trip(self):
        print("\nTrip ID:", self.trip_id)
        print("Destination:", end=" ")
        self.destination.show_destination()
        print("Duration:", self.days, "days")
        print("Budget: Rs.", self.budget)


class TravelPlanner:
    def __init__(self):
        self.trips = []

    def add_trip(self, trip):
        self.trips.append(trip)
        print("Trip added successfully!")

    def show_all_trips(self):
        if len(self.trips) == 0:
            print("No trips planned yet.")
        else:
            for trip in self.trips:
                trip.show_trip()

    def search_trip(self, trip_id):
        for trip in self.trips:
            if trip.trip_id == trip_id:
                trip.show_trip()
                return

        print("Trip not found.")


def main():
    planner = TravelPlanner()

    destination1 = Destination("Varanasi", "India")
    destination2 = Destination("Srinagar", "India")

    trip1 = Trip("T101", destination1, 3, 5000)
    trip2 = Trip("T102", destination2, 5, 12000)

    planner.add_trip(trip1)
    planner.add_trip(trip2)

    print("\nMy Travel Plans")
    planner.show_all_trips()

    print("\nSearch a Trip")
    planner.search_trip("T101")


if __name__ == "__main__":
    main()
