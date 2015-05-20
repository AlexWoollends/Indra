"""
auditorium_model.py
Modeling Schelling's auditorium puzzle.
"""
import indra.grid_agent as ga
import indra.grid_env as ge


class AuditoriumAgent(ga.GridAgent):
    """
    Agents that seat themselves in an auditorium.
    """
    def __init__(self, name, goal="Get a seat"):
        super().__init__(name, goal=goal)
        self.seated = False

    def act(self):
        """
        Find a seat.
        Once seated, these agents just stay put!
        """
        if not self.seated:
            self.env.move_to_empty(self)
            self.seated = True
            (x, y) = self.pos
            print("Agent %s has pos %i, %i" % (self.name, x, y))


class RearAgent(AuditoriumAgent):
    """
    Agents that want to sit at the back.
    """

    def act(self):
        """
        Find a seat.
        Once seated, these agents just stay put!
        """
        if not self.seated:
            for row in self.env.row_iter():
                cell = self.env.position_item(self,
                                              grid_view=row)
                if cell is not None:
                    self.seated = True
                    break


class Auditorium(ge.GridEnv):
    """
    The auditorium where agents will seat themselves.
    """

    class RowIter:
        """
        Iterate through auditorium's rows.
        Returns a GridView of just that row.
        """
        def __init__(self, aud):
            self.auditorium = aud
            self.row = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.row < self.auditorium.height:
                ret = self.auditorium.get_row_view(self.row)
                self.row += 1
                return ret
            else:
                raise StopIteration()

    def __init__(self, name, height=36, width=40, torus=False,
                 model_nm="Auditorium", num_agents=800):
        super().__init__(name, width, height, torus=torus,
                         model_nm=model_nm)
        self.total_agents = num_agents
        self.curr_agents = 0

    def step(self):
        """
        Add an agent each turn.
        """
        super().step()
        if self.curr_agents < self.total_agents:
            self.add_agent(RearAgent("Rear agent %i"
                                     % self.curr_agents),
                           position=False)
            self.curr_agents += 1

    def row_iter(self):
        return Auditorium.RowIter(self)
