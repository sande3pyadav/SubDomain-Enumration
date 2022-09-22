import requests
import sys 


def subdomain(domain,wordlist):
       
       file = open(wordlist,'r').read() 
       line = file.splitlines() # it is used to spilit line       
       for x in line:
         subdom = f"https://{x}.{domain}" #take subdomain grom function 
      
         try:
             re = requests.get(subdom)
             if re.text:
                 print(subdom)

         except:
             pass             
        
wordlist=sys.argv[2]
website_name = sys.argv[1]

subdomain(website_name,wordlist)
