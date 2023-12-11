# InnoCraft Labs - Version Control and History

class VersionControlAndHistory:
    def __init__(self):
        self.versions = []

    def create_version(self, prototype, author, changes):
        version = Version(prototype, author, changes)
        self.versions.append(version)

    def get_versions(self):
        return self.versions

    def run(self):
        print("Version Control and History feature is running!")


class Version:
    def __init__(self, prototype, author, changes):
        self.prototype = prototype
        self.author = author
        self.changes = changes

    def get_prototype(self):
        return self.prototype

    def get_author(self):
        return self.author

    def get_changes(self):
        return self.changes
