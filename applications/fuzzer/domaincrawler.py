import requests

class Crawler:
    
    def __init__(self, ip):
        self.ip = ip
        self.methods = ['GET', 'POST']
        self.subdomains_list = []
        self.subdomains_success = []
    
    def build_subdomains(self):
        print("Reading subdomains")
        file = open("./wordlists/endpoints.txt", 'r')
        
        
        for _ in range(0,10): # Modify later, this is just for testing
            self.subdomains_list.append(file.readline()[:-1] + "." + self.ip)
            #Removes \n characters
        
        print(self.subdomains_list)
        file.close()
    
    def make_requests(self):
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
        
        
        
        if len(self.subdomains_success) > 0:
            with open('./subdomains.txt', 'w') as fp: 
                for item in self.subdomains_success:
                        # write each item on a new line
                    fp.write("%s\n" % item)
            
            print('Stored new domains')
        else:
            print("No domains found")
    
    def subdomains(self):
        self.build_subdomains()
        self.make_requests()
        
        