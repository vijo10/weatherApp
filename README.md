# Weather App using Django

This is a weather application built with Django that allows users to get current weather information for a given location.

## Features

- **Location Search**: Users can search for a specific location to get weather information.
- **City Weather**: The application retrieves the current weather data for the searched location, including temperature, and weather condition.

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- Django
- OpenWeatherMap API Key

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/vijo10/weatherApp.git
   
2. Navigate to the project directory:
   
   ```bash
   cd weather-app-django

3. Create a virtual environment (optional but recommended):

  ```bash
  python3 -m venv env
     
4. Activate the virtual environment:

  ```bash
  env\Scripts\activate

5. Install the required dependencies:
   
   ```bash
   pip install -r requirements.txt
   
6. Set up the API key:

- Sign up on **OpenWeatherMap** and obtain an API key.
- Open the **`settings.py`** file in the **`weatherApp`** directory.
- Replace **`'APID'`** with your actual API key in the **`OPENWEATHERMAP_API_KEY`** variable.

7. Start the development server:
   
   ```bash
   python manage.py runserver
  
8. Open your web browser and access the application at **`http://localhost:8000`.**  
     
## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit an issue or a pull request.

