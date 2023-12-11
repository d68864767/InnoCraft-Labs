# InnoCraft Labs - Innovation Challenges

class InnovationChallenges:
    def __init__(self):
        self.challenges = []

    def launch_challenge(self, name, description):
        challenge = Challenge(name, description)
        self.challenges.append(challenge)

    def get_challenges(self):
        return self.challenges

    def run(self):
        print("Innovation Challenges feature is running!")


class Challenge:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def remove_participant(self, participant):
        self.participants.remove(participant)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_participants(self):
        return self.participants
