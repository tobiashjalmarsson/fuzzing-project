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
        
        parser.add_argument("-wldir", "--wldir"
                            , required=False,
                            help="Wordlist to use for directory fuzzing", 
                            type=str,
                            default="directories")
    
        parser.add_argument("-wldom", "--wldom"
                            , required=False,
                            help="Wordlist to use for subdomain fuzzing", 
                            type=str,
                            default="subdomains")
        
        
        
        arguments = parser.parse_args()
        self.ip = arguments.ip
        self.wldirectories = arguments.wldir + ".txt"
        self.wldomains = arguments.wldom + ".txt"

