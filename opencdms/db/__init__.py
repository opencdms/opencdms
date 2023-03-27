import os


class Connections:
    midas_open: str = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "data"
    )


connections = Connections()
