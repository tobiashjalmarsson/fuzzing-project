import argparse

class Initiator:
    """
    Class to parse arguments and store them in an
    easily accessible class.
    
    Add arguments here from what could be needed
    """
    
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Fuzz ip, -ip <IP>"
        )

        parser.add_argument("-ip", "--ip"
                            , required=True,
                            help="target ip for fuzzing", 
                            type=str,
                            default="127.0.0.1")
        arguments = parser.parse_args()
        self.ip = arguments.ip

