class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, cost):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.cost = cost
        self.premium_amount = self.calculate_premium()

    def calculate_premium(self):
        if self.vehicle_type.lower() == "two wheeler":
            return self.cost * 0.02
        elif self.vehicle_type.lower() == "four wheeler":
            return self.cost * 0.06
        else:
            return 0

    def display_details(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Cost: ${self.cost:.2f}")
        print(f"Premium Amount: ${self.premium_amount:.2f}")


vehicle1 = Vehicle("V123", "Two Wheeler", 50000)
vehicle2 = Vehicle("V456", "Four Wheeler", 300000)

vehicle1.display_details()
vehicle2.display_details()
