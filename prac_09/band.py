"""
CP1404, Prac_09,
Band class.
"""


class Band:
    def __init__(self, name):
        """Initialize the Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of the band and its members."""
        members = "".join(str(musician) for musician in self.musicians)
        return f"Band: {self.name}Members:{members}"

    def play(self):
        """Simulate the band playing and list what instruments are being played."""
        if not self.musicians:
            return f"The band {self.name} has no musicians."
        return "".join(musician.play() for musician in self.musicians)
