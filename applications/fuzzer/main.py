import sys, getopt
import parser, fuzzer.explorer as explorer


def main():
    initiator = parser.Initiator()
    print(initiator.ip)
    crawler = explorer.Crawler(initiator.ip)
    
if __name__ == "__main__":
    main()