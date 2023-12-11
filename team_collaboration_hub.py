# InnoCraft Labs - Team Collaboration Hub

class TeamCollaborationHub:
    def __init__(self):
        self.team_members = []
        self.files = []

    def add_team_member(self, team_member):
        self.team_members.append(team_member)

    def remove_team_member(self, team_member):
        self.team_members.remove(team_member)

    def add_file(self, file):
        self.files.append(file)

    def remove_file(self, file):
        self.files.remove(file)

    def get_team_members(self):
        return self.team_members

    def get_files(self):
        return self.files

    def run(self):
        print("Team Collaboration Hub feature is running!")

class TeamMember:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

