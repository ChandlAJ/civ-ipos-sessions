#
#
# # Create a Graph Class:
# # Implement a Graph class to represent the map.
# # The Graph class should allow adding locations as vertices and connections between them as edges.
# # Add Locations and Connections:
# # Add a few locations with specific names and latitudes.
# # Connect these locations to simulate a map.
# # Display the Map:
# # Print the connections between locations to visualize the map structure.
#
# from dataclasses import dataclass
# # Define a Location Data Class
# # Include name and latitude/longitude attributes.
# class Location:
#     name: str
#     # latitude: float
#     # longitude: float
#
# class Graph:
#     def __init__(self):
#         # Dictionary to store location names as keys and lists of connected locations as values
#         pass
#
#     def add_location(self, location):
#         # Create an empty list for each location's connections
#         # Each location is now a vertice in the graph object
#         pass
#
#
#     def add_connection(self, location1_name, location2_name):
#         pass
#         # Search the dicitonary keys for the two locations
#
#             # Add the connection bidirectionally
#             # If both keys are found connect them by adding each to the Locations list
#             # Check if location 2 is in the vertice for location 1
#
#                 # If location 2 is not there add to the location 1 list
#
#             # Check if location 2 is in the vertice for location 1
#
#                 # If location 2 is not there add to the location 1 list
#
#         # else:
#         #     print(f"One or both locations '{location1_name}' and '{location2_name}' do not exist in the graph.")
#
#
# # Example usage:
# def main():
#     # Step 1: Create 3 Locations exzmple
#     location1 = Location(name="LocationA", latitude=40.7128, longitude=30.7008)
#
#     # Step 2: Create a Graph and Add Locations
#     graph = Graph()
#
#     # Step 3: Add Connections - example usage
#     graph.add_connection("LocationA", "LocationB")
#
#
#     # Step 4: Display the Graph (Map)
#     print("Map representation:")
#     # graph.display()
#
# if __name__ == "__main__":
#     main()


import array

my_array = array.array("i", [1, 2, 3, 4, 5])

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

stack.pop()
print(stack)

# Define a class for each staff member as a node within the org chart
class Node:
    def __init__(self, name, title):
        self.name = name                  # Staff member's name
        self.title = title                # Staff member's job title or position
        self.subordinates = []            # List of all direct reports for staff member

    def add_subordinate(self, node):
        self.subordinates.append(node)    # Add a staff member under supervision of the staff member

# Adding staff members and their role/position using Node class
ceo = Node("Alex Chandler", "CEO")
director = Node("Jimi Hendrix", "Director")
cfo = Node("Robert Plant", "CFO")
customer_service_manager = Node("Jim Morrison", "Customer Service Manager")
operations_manager = Node("Jimmy Page", "Operations Manager")
finance_officer = Node("Mick Jagger", "Finance Officer")

# Building the tree structure by assigning subordinates to staff/positions
ceo.add_subordinate(director)
ceo.add_subordinate(cfo)
director.add_subordinate(customer_service_manager)
director.add_subordinate(operations_manager)
cfo.add_subordinate(finance_officer)

# # Display the full org chart
# ceo.display()

#
# def display(self, level=0):
#     indent = "  " * level
#     print(f"{indent}- {self.name} ({self.title})")
#     for subordinate in self.subordinates:
#         subordinate.display(level + 1)


# Define a class to represent the German train network between major cities
class TrainGraph:
    def __init__(self):
        self.routes = {}  # Create list to store connections of adjacent cities

    def add_city(self, city):
        if city not in self.routes:
            self.routes[city] = []

    def add_connection(self, city1, city2, travel_time):
        # Add connection in both direction between cities with travel time
        self.routes[city1].append((city2, travel_time))
        self.routes[city2].append((city1, travel_time))

# Create the graph data structure
germany_trains = TrainGraph()

# Add cities to the train network
cities = ["Berlin", "Munich", "Hamburg", "Leipzig"]
for city in cities:
    germany_trains.add_city(city)

# Add train connections between cities with approximate travel times
germany_trains.add_connection("Berlin", "Leipzig", 1.5)
germany_trains.add_connection("Berlin", "Hamburg", 2.0)
germany_trains.add_connection("Berlin", "Munich", 4.0)
germany_trains.add_connection("Leipzig", "Munich", 4.5)
germany_trains.add_connection("Hamburg", "Munich", 5.5)

# # Display the network
# germany_trains.show_network()

# def show_network(self):
#     for city, connections in self.routes.items():
#         print(f"{city} 🚉")
#         for dest, time in connections:
#             print(f"  ↳ {dest} ({time} hrs)")