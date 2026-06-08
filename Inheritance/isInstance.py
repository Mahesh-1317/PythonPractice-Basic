class Vehicle:
    pass
class LandVehicle(Vehicle):
    pass
class TrackedVehicle(LandVehicle):
    pass

vehicle = Vehicle()
land_vehicle = LandVehicle()
trackedVehicle = TrackedVehicle()

for obj in [Vehicle,land_vehicle,trackedVehicle]:
    for cls in [Vehicle,LandVehicle,TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()