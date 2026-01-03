class Distance:
    
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self, other):
        total_cm = self.cm + other.cm
        total_m = self.m + other.m + total_cm // 100  # Convert extra cm to m
        total_cm = total_cm % 100
        total_km = self.km + other.km + total_m // 1000  # Convert extra m to km
        total_m = total_m % 1000
        return Distance(total_km, total_m, total_cm)

    
    def __sub__(self, other):
        
        self_total_cm = self.km * 100000 + self.m * 100 + self.cm
        other_total_cm = other.km * 100000 + other.m * 100 + other.cm
        diff_cm = self_total_cm - other_total_cm

        if diff_cm < 0:
            diff_cm = -diff_cm

        km = diff_cm // 100000
        m = (diff_cm % 100000) // 100
        cm = diff_cm % 100
        return Distance(km, m, cm)

    
    def show(self):
        print(f"{self.km} km, {self.m} m, {self.cm} cm")

    def __del__(self):
        print("Distance object destroyed")

d1 = Distance(8, 350, 35)
d1.show()
d2 = Distance(5, 900, 45)
d2.show()

d3 = d1 + d2
print("Addition result:")
d3.show()

d4 = d1 - d2
print("Subtraction result:")
d4.show()