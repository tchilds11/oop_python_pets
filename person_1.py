class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.greeting_count = 0
        self.friend = friend


    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greeting_count +=1

    def add_friend(self, new_friend):
        self.friend.append(new_friend)

    def num_friend(self):
        (print(len(self.friend))

# Sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# Jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")





# Sonny.greet(Jordan)
# Jordan.greet(Sonny)
