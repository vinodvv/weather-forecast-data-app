import requests

API_KEY = "053d57895e0747bda05ddc97b25bc958"


def get_data(place, forecast_days=None):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    num_values = 8 * forecast_days
    filtered_data = filtered_data[:num_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Bangalore", forecast_days=2))
