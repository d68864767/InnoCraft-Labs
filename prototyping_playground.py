# InnoCraft Labs - Prototyping Playground

class PrototypingPlayground:
    def __init__(self):
        self.prototypes = []

    def create_prototype(self, name):
        prototype = Prototype(name)
        self.prototypes.append(prototype)

    def get_prototypes(self):
        return self.prototypes

    def run(self):
        print("Prototyping Playground feature is running!")


class Prototype:
    def __init__(self, name):
        self.name = name
        self.wireframes = []
        self.mockups = []
        self.interactive_prototypes = []

    def add_wireframe(self, wireframe):
        self.wireframes.append(wireframe)

    def remove_wireframe(self, wireframe):
        self.wireframes.remove(wireframe)

    def add_mockup(self, mockup):
        self.mockups.append(mockup)

    def remove_mockup(self, mockup):
        self.mockups.remove(mockup)

    def add_interactive_prototype(self, interactive_prototype):
        self.interactive_prototypes.append(interactive_prototype)

    def remove_interactive_prototype(self, interactive_prototype):
        self.interactive_prototypes.remove(interactive_prototype)

    def get_name(self):
        return self.name

    def get_wireframes(self):
        return self.wireframes

    def get_mockups(self):
        return self.mockups

    def get_interactive_prototypes(self):
        return self.interactive_prototypes
