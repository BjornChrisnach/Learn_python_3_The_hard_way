## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## name, Dog has-a name
        self.name = name

## Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## name, cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## name, Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## name, Employee has-a name
        super(Employee, self).__init__(name)
        ## salary, Employee has a salary
        self.salary = Salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is_a Person
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank")

## frank has-a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse isa Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()