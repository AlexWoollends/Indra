"""
fashion_model.py
A fashion model that includes followers and hipsters
changing fashions based on each other's choices.
"""
# import logging
import indra.display_methods as disp
import indra.menu as menu
import stance_model as sm


class Follower(sm.Follower):
    """
    A fashion follower: tries to switch to hipsters' fashions.
    """
    def __init__(self, name, goal, max_move):
        super().__init__(name, goal, max_move)
        self.other = Hipster


class Hipster(sm.Leader):
    """
    A fashion hipster: tries to not look like followers.
    """
    def __init__(self, name, goal, max_move):
        super().__init__(name, goal, max_move)
        self.other = Follower


class Society(sm.StanceEnv):
    """
    A society of hipsters and followers.
    """
    def __init__(self, name, length, height, model_nm=None, torus=False):
        super().__init__(name, length, height, model_nm=model_nm,
                         torus=False, postact=True)
        self.stances = ["blue", "red"]
        self.line_graph_title = \
            "A. Smith's fashion model: Populations in %s adopting fashion %s"
        self.agents.set_var_color('Hipster', disp.GREEN)
        self.agents.set_var_color('Follower', disp.MAGENTA)
        self.menu.view.add_menu_item("v",
                                     menu.MenuLeaf("(v)iew fashions",
                                                   self.view_pop))
