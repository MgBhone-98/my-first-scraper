import requests
import datetime
import pytz


def get_currency():
    # Free API သုံးပြီး ငွေလဲနှုန်းယူမယ်
    url = "https://open.er-api.com/v6/latest/USD"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data['result'] == 'success':
            mmk_rate = data['rates']['MMK']

            #now = datetime.datetime.now()
            # မြန်မာစံတော်ချိန် သတ်မှတ်ခြင်း
            tz_MM = pytz.timezone('Asia/Yangon')
            now_MM = datetime.datetime.now(tz_MM)

            print(f"--- Exchange Rate Update ---")
            print(f"Date: {now_MM.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"1 USD = {mmk_rate} MMK")  # ဒီစာကြောင်း ပါမှ MMK ထွက်မှာပါ
            print(f"----------------------------")
        else:
            print("Error: Could not fetch data.")

    except Exception as e:
        print(f"An error occured : {e}")

if __name__ == "__main__":
    get_currency()