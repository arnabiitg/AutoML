const exampleWeatherData = [
    {
      dt: 1660708800, // Unix timestamp for 2022-08-17 00:00:00 UTC
      main: {
        temp: 25.5,
        humidity: 65,
      },
      wind: {
        speed: 4.5,
      },
    },
    {
      dt: 1660712400, // Unix timestamp for 2022-08-17 01:00:00 UTC
      main: {
        temp: 24.8,
        humidity: 68,
      },
      wind: {
        speed: 4.2,
      },
    },
    {
      dt: 1660716000, // Unix timestamp for 2022-08-17 02:00:00 UTC
      main: {
        temp: 24.3,
        humidity: 70,
      },
      wind: {
        speed: 3.8,
      },
    },
    {
      dt: 1660719600, // Unix timestamp for 2022-08-17 03:00:00 UTC
      main: {
        temp: 23.7,
        humidity: 72,
      },
      wind: {
        speed: 3.4,
      },
    },
    {
      dt: 1660723200, // Unix timestamp for 2022-08-17 04:00:00 UTC
      main: {
        temp: 23.2,
        humidity: 75,
      },
      wind: {
        speed: 3.0,
      },
    },
    {
      dt: 1660726800, // Unix timestamp for 2022-08-17 05:00:00 UTC
      main: {
        temp: 22.8,
        humidity: 78,
      },
      wind: {
        speed: 2.7,
      },
    },
    {
      dt: 1660730400, // Unix timestamp for 2022-08-17 06:00:00 UTC
      main: {
        temp: 22.5,
        humidity: 80,
      },
      wind: {
        speed: 2.4,
      },
    },
    {
      dt: 1660734000, // Unix timestamp for 2022-08-17 07:00:00 UTC
      main: {
        temp: 22.3,
        humidity: 82,
      },
      wind: {
        speed: 2.2,
      },
    },
    {
      dt: 1660737600, // Unix timestamp for 2022-08-17 08:00:00 UTC
      main: {
        temp: 22.0,
        humidity: 84,
      },
      wind: {
        speed: 2.0,
      },
    },
    {
      dt: 1660741200, // Unix timestamp for 2022-08-17 09:00:00 UTC
      main: {
        temp: 21.8,
        humidity: 85,
      },
      wind: {
        speed: 1.8,
      },
    },
    // Add more example data for additional hours here...
  ];
  
  // You can create a function to display the example weather data on the UI
  function displayExampleWeather() {
    const forecastContainer = document.querySelector('.forecast');
  
    exampleWeatherData.forEach((forecast) => {
      const timestamp = forecast.dt * 1000;
      const date = new Date(timestamp);
      const temperature = forecast.main.temp;
      const humidity = forecast.main.humidity;
      const windSpeed = forecast.wind.speed;
  
      const forecastItem = document.createElement('div');
      forecastItem.classList.add('forecast-item');
      forecastItem.innerHTML = `
        <h3>${date.getHours()}:00</h3>
        <p>Temperature: ${temperature}°C</p>
        <p>Humidity: ${humidity}%</p>
        <p>Wind Speed: ${windSpeed} m/s</p>
      `;
      forecastContainer.appendChild(forecastItem);
    });
  }
  
  // Call the function to display the example weather data
  displayExampleWeather();
  