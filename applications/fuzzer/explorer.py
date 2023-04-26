import requests

class Crawler:
    
    def __init__(self, ip):
        self.ip = ip
        self.methods = ['GET', 'POST']
        self.subdomains_list = []
        self.subdomains_success = []
        self.directories_list = []
        self.directories_success = []
    
    def build_directories(self):
        print("Reading directories wordlist")
        file = open("./wordlists/directories.txt", 'r')
        
        
        for _ in range(0,10): # Modify later, this is just for testing
            self.directories_list.append(self.ip + "/" + file.readline()[:-1])
            #Removes \n characters
        
        print(self.directories_list)
        file.close()
    
    def build_subdomains(self):
        print("Reading subdomain wordlist")
        file = open("./wordlists/subdomains.txt", 'r')
        
        
        for _ in range(0,10): # Modify later, this is just for testing
            self.subdomains_list.append(file.readline()[:-1] + "." + self.ip)
            #Removes \n characters
        
        print(self.subdomains_list)
        file.close()
    
    def make_requests_subdomain(self):
        for subdom in self.subdomains_list:
            for method in self.methods:
                if method == 'GET':
                    res = requests.get(subdom)
                    if res.status_code != 404:
                        self.subdomains_success.append(subdom)
                
                if method == 'POST':
                    res = requests.post(subdom)
                    if res.status_code != 404:
                        self.subdomains_success.append(subdom)
        
    
    def make_requests_directories(self):
        for dir in self.directories_list:
            for method in self.methods:
                if method == 'GET':
                    res = requests.get(dir)
                    if res.status_code != 404:
                        self.directories_success.append(dir)
                
                if method == 'POST':
                    res = requests.post(dir)
                    if res.status_code != 404:
                        self.directories_success.append(dir)
        
        
        if len(self.directories_success) > 0:
            with open('./directories.txt', 'w') as fp: 
                for dir in self.subdomains_success:
                        # write each item on a new line
                    fp.write("%s\n" % dir)
            
            print('Stored new directories')
        else:
            print("No directories found")
    
    def subdomains(self):
        self.build_subdomains()
        self.make_requests_subdomain()
        
    def subdirectories(self):
        self.build_directories()
        self.make_requests_directories()    