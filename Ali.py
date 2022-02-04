import requests
import time
import webbrowser
from discord_webhook import DiscordWebhook, DiscordEmbed

print("""
     _____    __    _______    _      ___                    __  _         
    / ___/__ / /_  /  _/ _ \  (_)__  / _/__  ______ _  ___ _/ /_(_)__  ___ 
   / (_ / -_) __/ _/ // ___/ / / _ \/ _/ _ \/ __/  ' \/ _ `/ __/ / _ \/ _ \ 
   \___/\__/\__/ /___/_/    /_/_//_/_/ \___/_/ /_/_/_/\_,_/\__/_/\___/_//_/
                                                                                                                                         
""")

ip = input( """
                              [+] THE IP ADDRESS : """)
if ip == '':
   print("[-] WRITE THE IP")
   time.sleep(1)
   print("[!] After 3 seconds [Get IP information] will be closed automatically")
   time.sleep(3)
webhook_url = input( """
                              [+] YOUR WEBHOOK : """)
if webhook_url == '':
   print("[-] WRITE THE WEBHOOK")
   time.sleep(1)
   print("[!] After 3 seconds [Get IP information] will be closed automatically")
   time.sleep(3)


req = requests.get("http://ipwhois.app/json/"+ip)
instagram = "https://www.instagram.com/14d9/"

print("")
print("")
print("")

latitude = req.json()["latitude"]
longitude = req.json()["longitude"]
fortheflag = str(req.json()["country_code"]).lower()

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

webhook = DiscordWebhook(url=f"{webhook_url}", username="Instagram : @14d9", avatar_url="https://cdn.discordapp.com/attachments/912363219383877672/939130050635243590/0.png")

embed = DiscordEmbed(title='Ali | Get IP information', description=f'**IP : {req.json()["ip"]}\nIP -> Success : {req.json()["success"]}\nIP -> Type : {req.json()["type"]}\nIP -> Country : {req.json()["country"]}\nIP -> Country Flag : **:flag_{fortheflag}:**\nIP -> Country Code : {req.json()["country_code"]}\nIP -> Country Capital : {req.json()["country_capital"]}\nIP -> Country Phone : {req.json()["country_phone"]}\nIP -> Region : {req.json()["region"]}\nIP -> City : {req.json()["city"]}\nIP ->  Google Maps : https://www.google.com/maps/search/{latitude},+{longitude}\nIP -> TimeZone : {req.json()["timezone"]}\nIP -> TimeZone Name : {req.json()["timezone_name"]}\nIP -> TimeZone dst Offset : {req.json()["timezone_dstOffset"]}\nIP -> TimeZone gmt Offset : {req.json()["timezone_gmtOffset"]}\nIP -> TimeZone gmt : {req.json()["timezone_gmt"]}\nIP -> Currency : {req.json()["currency"]}\nIP -> Currency Code : {req.json()["currency_code"]}\nIP -> Currency Symbol : {req.json()["currency_symbol"]}\nIP -> Currency Plural : {req.json()["currency_plural"]}\nIP -> Continent : {req.json()["continent"]}\nIP -> Continent Code : {req.json()["continent_code"]}**', color='000000')
embed.set_image(url='https://cdn.discordapp.com/attachments/912363219383877672/939120156414705675/600x200.png')

embed.set_footer(text='Created By Ali || Instagram @14d9')

webhook.add_embed(embed)
response = webhook.execute()

print("")
print("")
print("[+] Thank you for using my tool")
time.sleep(1)
webbrowser.open(instagram)
print("")
print("[!] After 5 seconds [Get IP information] will be closed automatically")
time.sleep(5)