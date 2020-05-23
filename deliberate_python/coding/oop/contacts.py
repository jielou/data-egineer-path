from representations import AsDictionaryMixin

class _AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1:Address("121 admin rd", "concord", "NH", "03301"),
            2:Address("67 paperwork ave", "Manchester", "NH", "03101"),
            3:Address("167 hay ave", "Manchester", "NH", "03101"),
            4:Address("627 highland ave", "Pittsburgh", "PA", "03101"),
            5:Address("674 penn ave", "New York", "NY", "03101"),
        }
    
    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(f"invliad employee id {employee_id}")
        return address



class Address(AsDictionaryMixin):
    def __init__(self, street, city, state, zipcode, street2=""):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.street2 = street2

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f"{self.city}, {self.state} {self.zipcode}")
        return "\n".join(lines)

# address = Address("123 Snake street", "Monticello", "KY", 97856)
# print(address)

_address_book = _AddressBook()

def get_employee_address(employee_id):
    return _address_book.get_employee_address(employee_id)
