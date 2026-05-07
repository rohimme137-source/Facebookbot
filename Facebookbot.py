import os
import time
import requests
import mechanize
from bs4 import BeautifulSoup

def clear():
    os.system('clear')

def banner():
    print("=" * 45)
    print("   FACEBOOK AUTO MESSAGE BOT (FREE)")
    print("=" * 45)

def send_message(number, message):
    # এখানে ফেসবুকের মেসেজ পাঠানোর লজিক থাকবে
    # বর্তমানে এটি একটি ডামি প্রসেস হিসেবে কাজ করবে
    print(f"[*] Sending Message to: {number}")
    print(f"[+] Message: {message}")
    
    # লগইন এবং মেসেজ পাঠানোর রিকোয়েস্ট লজিক এখানে বসাতে হয়
    # নিরাপদ থাকতে প্রতি মেসেজের পর বিরতি দেওয়া জরুরি
    time.sleep(2) 
    print(f"[✔] Successfully Sent to {number}")

def main():
    clear()
    banner()
    
    filename = input("[+] নাম্বার ফাইলের নাম দিন: ")
    if not os.path.exists(filename):
        print("[-] ফাইল পাওয়া যায়নি!")
        return

    msg_text = input("[+] যে মেসেজটি পাঠাতে চান সেটি লিখুন: ")
    
    with open(filename, 'r') as f:
        numbers = [line.strip() for line in f.readlines() if line.strip()]

    print(f"\n[!] মোট {len(numbers)}টি নাম্বারে মেসেজ পাঠানো শুরু হচ্ছে...\n")

    for i, num in enumerate(numbers, 1):
        print(f"[{i}/{len(numbers)}]", end=" ")
        send_message(num, msg_text)
        print("-" * 30)
        time.sleep(3) # ফেসবুক স্প্যাম ফিল্টার এড়াতে বিরতি

    print("\n[+] সকল মেসেজ পাঠানো সম্পন্ন হয়েছে।")

if __name__ == "__main__":
    main()
