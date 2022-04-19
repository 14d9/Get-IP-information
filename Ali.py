import requests, webbrowser, time

print("""
     _____    __    _______    _      ___                    __  _         
    / ___/__ / /_  /  _/ _ \  (_)__  / _/__  ______ _  ___ _/ /_(_)__  ___ 
   / (_ / -_) __/ _/ // ___/ / / _ \/ _/ _ \/ __/  ' \/ _ `/ __/ / _ \/ _ \ 
   \___/\__/\__/ /___/_/    /_/_//_/_/ \___/_/ /_/_/_/\_,_/\__/_/\___/_//_/
                                                                                                                                         
""")

ip = input( """[+] THE IP ADDRESS : """)

req = requests.get("http://ipwhois.app/json/"+ip)
instagram = 'https://www.instagram.com/q97l/'

print("")
print("")
print("")

latitude = req.json()["latitude"]
longitude = req.json()["longitude"]

print("----------------------------------------------")
print("IP : ",req.json()["ip"])
print("IP -> Success : ",req.json()["success"])
print("IP -> Type : ",req.json()["type"])
print("IP -> Country : ",req.json()["country"])
print("IP -> Country Code : ",req.json()["country_code"])
print("IP -> Country Capital : ",req.json()["country_capital"])
print("IP -> Country Phone : ",req.json()["country_phone"])
print("IP -> Region : ",req.json()["region"])
print("IP -> City : ",req.json()["city"])
print(f"IP ->  Google Maps : https://www.google.com/maps/search/{latitude},+{longitude}")
print("IP -> TimeZone : ",req.json()["timezone"])
print("IP -> TimeZone Name : ",req.json()["timezone_name"])
print("IP -> TimeZone dst Offset : ",req.json()["timezone_dstOffset"])
print("IP -> TimeZone gmt Offset : ",req.json()["timezone_gmtOffset"])
print("IP -> TimeZone gmt : ",req.json()["timezone_gmt"])
print("IP -> Currency : ",req.json()["currency"])
print("IP -> Currency Code : ",req.json()["currency_code"])
print("IP -> Currency Symbol : ",req.json()["currency_symbol"])
print("IP -> Currency Plural : ",req.json()["currency_plural"])
print("IP -> Continent : ",req.json()["continent"])
print("IP -> Continent Code : ",req.json()["continent_code"])
print("----------------------------------------------")

print("")
print("")
print("[+] Thank you for using my tool")
time.sleep(1)
webbrowser.open(instagram)
print("")
print("[!] After 5 seconds [Get IP information] will be closed automatically")
time.sleep(5)
