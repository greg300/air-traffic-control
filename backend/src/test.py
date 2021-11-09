# coding=utf-8

from .entities.entity import Session, engine, Base
from .entities.plane import Plane

# Generate database schema.
Base.metadata.create_all(engine)

# Start session.
session = Session()

# Check for existing data.
planes = session.query(Plane).all()

if len(planes) == 0:
    # Create and persist mock plane.
    python_plane = Plane("SQLAlchemy Plane", "123456", "Test", "Script")
    session.add(python_plane)
    session.commit()
    session.close()

    # Reload planes.
    exams = session.query(Plane).all()

# Show existing planes.
print('### Planes:')
for plane in planes:
    print(f'({plane.id}) {plane.name} - {plane.serial_no} – {plane.make}')