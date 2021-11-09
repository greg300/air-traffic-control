# coding=utf-8

from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.plane import Plane, PlaneSchema

# Create the Flask application.
app = Flask(__name__)

# Generate database schema.
Base.metadata.create_all(engine)

@app.route('/planes')
def get_planes():
    # Fetch from the database.
    session = Session()
    plane_objects = session.query(Plane).all()

    # Transform into JSON-serializable objects.
    schema = PlaneSchema(many=True)
    planes = schema.dump(plane_objects)

    # Serialize as JSON.
    session.close()
    return jsonify(planes)


@app.route('/planes', methods=['POST'])
def add_plane():
    # Mount plane object.
    posted_plane = PlaneSchema(only=('name', 'serial_no', 'make'))\
        .load(request.get_json())

    plane = Plane(**posted_plane, created_by="HTTP post request")

    # Persist plane.
    session = Session()
    session.add(plane)
    session.commit()

    # Return created plane.
    new_plane = PlaneSchema().dump(plane)
    session.close()
    return jsonify(new_plane), 201