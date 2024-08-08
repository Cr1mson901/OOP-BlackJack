class deck:
    def __init__(self) -> None:
        pass

class hand:
    spacing = " " * 2
    def __init__(self) -> None:
        pass

    def print(self):
        for pieces in zip(*self):
            print(self.spacing.join(pieces))
