import os
import time

def load_numbers():
    filename = input("\n[+] নাম্বার ফাইলের নাম দিন (যেমন: numbers.txt): ")
    
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                # প্রতি লাইন থেকে নাম্বারগুলো লিস্টে নিচ্ছে এবং স্পেস বাদ দিচ্ছে
                numbers = [line.strip() for line in file.readlines() if line.strip()]
            
            print(f"[+] মোট {len(numbers)}টি নাম্বার পাওয়া গেছে।")
            return numbers
        except Exception as e:
            print(f"[-] ফাইল পড়তে সমস্যা হয়েছে: {e}")
            return []
    else:
        print("[-] ফাইলটি খুঁজে পাওয়া যায়নি! নিশ্চিত করুন ফাইলটি এই ফোল্ডারে আছে।")
        return []

def start_automation(numbers):
    if not numbers:
        print("[-] কোনো নাম্বার নেই, কাজ শুরু করা সম্ভব নয়।")
        return

    print("\n[*] অটোমেশন শুরু হচ্ছে...")
    for index, num in enumerate(numbers, 1):
        print(f"[{index}] কাজ চলছে: {num}")
        # এখানে আপনার মূল কাজের লজিক বসাবেন (যেমন SMS পাঠানো বা ID চেক)
        time.sleep(1) # ১ সেকেন্ড বিরতি
    
    print("\n[+] সব নাম্বারের কাজ শেষ হয়েছে।")

# মেইন ফাংশন টেস্ট
if __name__ == "__main__":
    print("--- ফাইল ইনপুট সিস্টেম ---")
    nums = load_numbers()
    if nums:
        start_automation(nums)
