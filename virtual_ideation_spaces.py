# InnoCraft Labs - Virtual Ideation Spaces

class VirtualIdeationSpaces:
    def __init__(self):
        self.ideation_spaces = []

    def create_ideation_space(self, name):
        ideation_space = IdeationSpace(name)
        self.ideation_spaces.append(ideation_space)

    def get_ideation_spaces(self):
        return self.ideation_spaces

    def run(self):
        print("Virtual Ideation Spaces feature is running!")


class IdeationSpace:
    def __init__(self, name):
        self.name = name
        self.whiteboard = Whiteboard()
        self.mind_mapping_tool = MindMappingTool()

    def get_name(self):
        return self.name

    def get_whiteboard(self):
        return self.whiteboard

    def get_mind_mapping_tool(self):
        return self.mind_mapping_tool


class Whiteboard:
    def __init__(self):
        self.content = ""

    def write(self, text):
        self.content += text

    def erase(self):
        self.content = ""

    def get_content(self):
        return self.content


class MindMappingTool:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def remove_node(self, node):
        self.nodes.remove(node)

    def get_nodes(self):
        return self.nodes
