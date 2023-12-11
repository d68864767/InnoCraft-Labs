# InnoCraft Labs - Main Script

from virtual_ideation_spaces import VirtualIdeationSpaces
from prototyping_playground import PrototypingPlayground
from team_collaboration_hub import TeamCollaborationHub
from innovation_challenges import InnovationChallenges
from version_control_and_history import VersionControlAndHistory
from ai_powered_insights import AIPoweredInsights

def main():
    # Create instances of each feature
    virtual_ideation_spaces = VirtualIdeationSpaces()
    prototyping_playground = PrototypingPlayground()
    team_collaboration_hub = TeamCollaborationHub()
    innovation_challenges = InnovationChallenges()
    version_control_and_history = VersionControlAndHistory()
    ai_powered_insights = AIPoweredInsights()

    # Run the main functionality of each feature
    virtual_ideation_spaces.run()
    prototyping_playground.run()
    team_collaboration_hub.run()
    innovation_challenges.run()
    version_control_and_history.run()
    ai_powered_insights.run()

if __name__ == "__main__":
    main()
