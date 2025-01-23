import requests
import pandas as pd
import json

# Get Url with desired information and store it in a variable to be called later
weather_url= "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"
#request the data from the URL
response = requests.get(weather_url)

#convert the data to json
hourly_data = response.json()

#Save the data from response in the json folder
file_path = "data/json/response.json"


with open(file_path, "w") as file:
    json.dump(hourly_data, file, indent=5)

hourly = hourly_data["hourly"]

#convert hourly data to Dataframe
df = pd.DataFrame(hourly)

print(df)

#create a csv file called weather.csv
df.to_csv('weather.csv', index=False) 




