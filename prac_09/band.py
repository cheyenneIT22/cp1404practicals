"""Band class"""






class Band:




def __init__(self, name, instrument):
    """Initialise a band instance, based on parent class musician."""
    self.name = name
    self.instrument = instrument
def __str__(self):
    """Return a string like instrument but with band instance and instrument."""
    return f"{self.name} ({self.guitar})"


def play(self):
    """Returns the musician and the instrument"""
    if not self.instruments:
        return f"{self.name} needs an instrument!"
    return f"{self.name} is playing: {self.instruments[0]}"
