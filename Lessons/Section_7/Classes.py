"""
We have talked about classes a bit during the first week of classes (no pun intended)
but now we will go through this topic in detail and actually learn how to create our own data types

In Python there are already pre-made data type such as list, dictionary, int, float and string. When
we think of list we think of it like a container that can hold things right? So when programming if we
needed something to be able to hold things for us we can use a list which is an object.

Alright, what if we wanted to represent people in code? Can we use an int? Well no... a person has an age, height, name
and etc. So a simple int will not be enough to represent a person. What about a list? We could store the age, height
name and etc in the list. Well... that works but is not a very good way to represent people. The better solution
will be to create a new data type that represents a person. Below is how we do it.
"""


class Person:
    def __init__(self, age, name, height):
        self.age = age
        self.name = name
        self.height = height

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_height(self):
        return self.height

john = Person(10, "Jonny", 130)
print(john.get_age())


"""
Alright looks a bit confusing right? No worries we will go through each piece.
To tell Python that you want to define a new object you use the "class" keyword.
Directly after the class keyword you give the object a name in this case we
named it person (case-sensitive). After that defined all the components and contents
of the new object. The last three are easy to understand and you have seen stuff like this before.
The only difference now is that these belong to a class so they are no longer called functions
and instead they are called methods. In particular, they are methods for the class/object person.
The first method __init__ is a special kind on method. It is what we call a constructor. This special
method will exist for a lot of classes you write, but is not required. Think of this special method as a blueprint for Python to
know how to build and initialize a person when you tell Python to make one. The last part you should
be confused about is the keyword "self". There are many definitions online, but think of self as a 
placeholder for an actual object. When we defined the get_name method we had to do self.name and
not just print name. The reason is because there can be multiple people so how does Python know which
name to print? This is why we need to use self. self is a placeholder for the actual object that calls the method.
When we define the method we do it generally so it works for all person objects. So when we do john.get_age()
the person object stored inside the var john calls the get_age method which does return self.age, but the self
gets replaced with john so it really does return john.name which makes a lot more sense. Got it? 
Ok now lets do harder examples. One more thing course_code and student_names are what we call attributes.
"""


class Course:
    def __init__(self, code):
        self.course_code = code
        self.student_names = []

    def get_course_code(self):
        return self.course_code

    def print_course_code(self):
        print(self.course_code)

    def add_student(self, new_student):
        self.student_names.append(new_student)

    """
    Notice how this method takes in a order parameter, but it has =False. This means that parameter is optional
    and you do not need to pass it in when using the method since by default it will be False.
    """
    def print_student_names(self, order=False):
        if order:
            print(self.student_names.sort())
        else:
            print(self.student_names)


"""
Hopefully the code makes sense. Anyhow I want you to now add another method called remove_student_name
which takes in a name (str) as input. The method will remove that name from the list. If the student is
not in the list then print that the student does not exist. If the method removed a student then print
that the student was removed from that course (need to specify the course name). 
"""

"""
Lets use our class and see if everything works as expected
"""
a_course = Course("ICS4U")
a_course.add_student("Bob")
a_course.add_student("Lee")
a_course.add_student("Ding")
a_course.add_student("Dong")
a_course.print_student_names()
a_course.print_student_names(False)
# a_course.remove_student_name("Jing")
# a_course.remove_student_name("Lee")
a_course.print_student_names()


"""
Alright now it is your turn.
Write and design a class called AreaFinder. AreaFinder will have one method for each shape.
AreaFinder needs to be able to take care of circles, rectangles and triangles.
"""


"""
There are a lot more special methods. __init__ is one of them but __len__, __str__, __eq__ and __lt__ also
exist. There are actually a lot more than this but we will not have time to cover them 
Ok time to upgrade the Person class!!!
"""