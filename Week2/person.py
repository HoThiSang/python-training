from datetime import date

class Person: 
    name = "Hanna"
    year_of_birth = 0

    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    def calculate_age(self):
        '''calculate age'''
        current_year = date.today().year
        return current_year - self.year_of_birth

    def print_person(self):
        '''display user's information'''
        return f"Name : {self.name} and {self.calculate_age()} years old"


def main():
    '''Main function'''
    person = Person("Hame", 2002)

    print(person.print_person())


if __name__ == "__main__":
    main()
 
