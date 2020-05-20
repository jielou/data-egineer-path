class ProductivitySystem:
    def track(self, employees, hours):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            result = employee.work(hours)
            print(f"{employee.name}: {result}")
        print("")

#redegisn for avoiding diamond problem
class ManagerRole:
    def work(self, hours):
        return f"screams and yells for {hours} hours"

class SecretaryRole:
    def work(self, hours):
        return f"expends for {hours} hours doing office paperwork"

class SalesRole:
    def work(self, hours):
        return f"expends for {hours} hours on the phone"

class FactoryRole:
    def work(self, hours):
        return f"manufactures gadgets for {hours} hours"