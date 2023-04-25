import sys, getopt
import parser, domaincrawler


def main():
    initiator = parser.Initiator()
    print(initiator.ip)
    crawler = domaincrawler.Crawler(initiator.ip)
    
if __name__ == "__main__":
    main()