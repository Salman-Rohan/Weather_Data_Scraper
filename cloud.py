import requests
import csv

def get_weather(city):
    url = f'https://wttr.in/{city}?format=j1'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        temp = data['current_condition'][0]['temp_C']
        desc = data['current_condition'][0]['weatherDesc'][0]['value']
        return {
            'City': city.title(),
            'Temperature (°C)': temp,
            'Condition': desc
        }
    else:
        return None

def save_to_csv(data, filename='weather_data.csv'):
    # ফাইল খুলবে অ্যাপেন্ড মোডতে, প্রথমবার নতুন ফাইল তৈরি হবে
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['City', 'Temperature (°C)', 'Condition'])
        # ফাইল খালি হলে হেডার লিখবে
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

if __name__ == "__main__":
    while True:
        city = input("Enter city name (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("Exiting program.")
            break
        weather = get_weather(city)
        if weather:
            print(f"Saving weather for {weather['City']}: {weather['Temperature (°C)']}°C, {weather['Condition']}")
            save_to_csv(weather)
        else:
            print("Could not fetch weather data for", city)

