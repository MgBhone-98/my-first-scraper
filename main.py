import datetime
import os

def run_task():
    now = datetime.datetime.now()
    print(f"--- Task Started at {now} ---")
    
    # လက်ရှိ run နေတဲ့ OS က ဘာလဲဆိုတာ စစ်တာ
    operating_system = os.name
    print(f"Running on OS: {operating_system}")
    
    print("Hello Gemini, my Python app is working!")
    print("---------------------------------------")

if __name__ == "__main__":
    run_task()