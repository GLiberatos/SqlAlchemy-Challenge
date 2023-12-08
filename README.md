# SqlAlchemy-Challenge
Module 10 Challenge

# Flask Weather API

This is a simple Flask API that provides weather data from a SQLite database. It offers endpoints to retrieve precipitation data, station information, temperature observations, and temperature statistics based on user-defined date ranges.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Examples](#examples)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- Required Python packages installed. You can install them using pip:

  ```bash
  pip install flask sqlalchemy
  
## Installation
Clone the repository:
git clone https://github.com/yourusername/your-repo.git

Navigate to the project directory:
cd your-repo

Run the API:
python app.py

The API should now be running locally on http://127.0.0.1:5000/.

## Usage
You can access the API endpoints to retrieve weather data. Here are the available endpoints:

## Endpoints
/api/v1.0/precipitation: Get precipitation data.<br>
/api/v1.0/stations: Get station information.<br>
/api/v1.0/tobs: Get temperature observations.<br>
/api/v1.0/<start>: Get temperature statistics from a start date.<br>
/api/v1.0/<start>/<end>: Get temperature statistics between a start and end date.

## Examples:
Here are some example requests to the API:

Get precipitation data:
`/api/v1.0/precipitation`

Get station information:
`/api/v1.0/stations`

Get temperature observations:
`/api/v1.0/tobs`

Get temperature statistics from a start date:
`/api/v1.0/start_date`

Get temperature statistics between a start and end date:
`/api/v1.0/start_date/end_date`
