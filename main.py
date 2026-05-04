import requests
import datetime

def get_currency():
    # Free API သုံးပြီး ငွေလဲနှုန်းယူမယ်
    url = "https://open.er-api.com/v6/latest/USD"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data['result'] == 'success':
            mmk_rate = data['rates']['MMK']
            now = datetime.datetime.now()

            print(f"--- Exchange Rate Update ---")
            print(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"----------------------------")
        else:
            print("Error: Could not fetch data.")

    except Exception as e:
        print(f"An error occured : {e}")

if __name__ == "__main__":
    get_currency()