from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

another = Student(name="mehdi", surname="bennix")
print(another)

# Derived fields are not constructor arguments, so this line raises TypeError:
# Student(name="Edward", surname="agle", id="toto")
