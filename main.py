import schedule
import time


#Inspired by: @tech_sis8 on TikTok

#Function that gets the weather data from the API
def get_weather_data(latitute, logitude):
        base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
        response = requests.get(base_url)
        data = response.json()
        return data

#Function that sends a text message with the body of the message
def send_text_message(message):
        account_sid = "AC00315666facb93cbe3a908b7c2e5f457"
        auth_token = "3d43b9dae077236607b0c97b7608d31f"
        from_phone_number = "+15613453459"
        to_phone_number = "+1561345345"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                body=message,
                from_= from_phone_number,
                to= to_phone_number
        )

        print("Message sent successfully")

#Function that sends the weather update
def send_weather_update():
        # Latitude and Longitude of West Palm Beach, FL
        latitute = 26.7153
        logitude = -80.0534


        weather_data = get_weather_data(latitute, logitude)
        temperature_celsius = weather_data["hourly"]["temperature_2m"]["0"]
        relativehumidty = weather_data["hourly"]["relativehumidity_2m"]["0"]
        wind_speed = weather_data["hourly"]["windspeed_10m"]["0"]
        weather_info = (
                f"Buen dia/n"
                f"La temperatura actual en West Palm Beach es de:"
                f"Temperatura: {temperature_celsius} grados Celsius\n"
                f"Relative Humidity: {relativehumidty}\n"
                f"Wind Speed: {wind_speed} m/s"
        )

        send_text_message(weather_info)

#Function that runs the program
def main():
        schedule.every().day.at("10:00").do(send_weather_update)
        while True:
                schedule.run_pending()
                time.sleep(1)

if __name__ == "__main__":
        main()