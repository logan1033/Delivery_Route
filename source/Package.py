######################################################################
# Package Object to store data.
######################################################################
class Package:
    def __init__(self, id: int, street: str, city: str, state: str, zipcode: str, deadline: str,
                 weight: int, notes: str, status: str):
        self.id: int = id
        self.street: str = street
        self.city: str = city
        self.state: str = state
        self.zipcode: str = zipcode
        self.deadline: str = deadline
        self.weight: int = weight
        self.notes: str = notes
        self.status: str = status

    def __str__(self):
        return "| ID: %i | Address: %s | City: %s | State: %s | Zipcode: %s | Deadline: %s | Mass: %i | Notes: %s | Status: %s |" % (
        self.id, self.street, self.city, self.state, self.zipcode, self.deadline, self.weight, self.notes, self.status)
