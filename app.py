# Import the dependencies.
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
import numpy as np

#################################################
# Database Setup
#################################################
# Create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def home():
    """List all available routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

#################################################
# Flask Routes
#################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(
        Measurement.date, 
        Measurement.prcp
    ).filter(Measurement.date >= one_year_ago).all()
    session.close()
    precipitation_data = [{
        "Date": date, 
        "Precipitation": prcp} for date, prcp in results
    ]
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()
    stations = [{
        "Station": station[0]} for station in results
    ]
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    most_active_station = 'USC00519281'
    results = session.query(
        Measurement.date, 
        Measurement.tobs
    ).filter(Measurement.station == most_active_station).filter(Measurement.date >= one_year_ago).all()
    session.close()
    temperatures = [{
        "Date": date, 
        "Temperature": tobs} for date, tobs in results
    ]
    return jsonify(temperatures)

@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)
    results = session.query(
        func.min(Measurement.tobs), 
        func.avg(Measurement.tobs), 
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start).all()
    session.close()
    temps = {
        "Minimum Temperature": results[0][0],
        "Average Temperature": results[0][1],
        "Maximum Temperature": results[0][2]
    }
    return jsonify({"Start Date": start, "Temperature Data": temps})

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = Session(engine)
    results = session.query(
        func.min(Measurement.tobs), 
        func.avg(Measurement.tobs), 
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()
    temps = {
        "Minimum Temperature": results[0][0],
        "Average Temperature": results[0][1],
        "Maximum Temperature": results[0][2]
    }
    return jsonify({"Start Date": start, "End Date": end, "Temperature Data": temps})

if __name__ == '__main__':
    app.run(debug=True)

