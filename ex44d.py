class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

# inheritence from the implicit function from Parent, so it gets 
# executed 2 times
dad.implicit()
son.implicit()

# Child overrides his own function
dad.override()
son.override()

# super with arguments overrides the altered function from the Child
dad.altered()
son.altered()