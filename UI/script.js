const apiUrl = 'http://127.0.0.1:7000/api/endpoint';


async function fetchWeatherData() {
    const response = await fetch(apiUrl);
    const datas = await response.json();
    const data = JSON.parse(datas)
    // const abc = JSON.parse(data) 
    console.log('Fetched data:', data.time);

    return data;
}

async function displayWeather() {
    try {
        const weatherData = await fetchWeatherData();
        const forecastContainer = document.querySelector('.forecast');

        for (let i = 0; i < weatherData.time.length; i++) {
            const timestamp = new Date(weatherData.time[i]);
            const temperature = weatherData.temperature[i];
            const humidity = weatherData.humidity[i];
            const windSpeed = weatherData.windspeed[i];

            const forecastItem = document.createElement('div');
            forecastItem.classList.add('forecast-item');
            forecastItem.innerHTML = `
                <h3>${timestamp.getHours()}:00</h3>
                <p>Temperature: ${temperature}°C</p>
                <p>Humidity: ${humidity}%</p>
                <p>Wind Speed: ${windSpeed} m/s</p>
            `;
            forecastContainer.appendChild(forecastItem);
        }
    } catch (error) {
        console.error('Error fetching weather data:', error);
    }
}

// Call the function to display weather data
displayWeather();


displayWeather();
