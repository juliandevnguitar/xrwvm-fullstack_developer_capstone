from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology",
         "year_foundation": 1975,
         "ceo": "Bob Smith"},
        {"name": "Mercedes",
         "description": "Great cars. German technology",
         "year_foundation": 1975,
         "ceo": "Bob Smith"},
        {"name": "Audi",
         "description": "Great cars. German technology",
         "year_foundation": 1975,
         "ceo": "Bob Smith"},
        {"name": "Kia",
         "description": "Great cars. Korean technology",
         "year_foundation": 1975,
         "ceo": "Bob Smith"},
        {"name": "Toyota",
         "description": "Great cars. Japanese technology",
         "year_foundation": 1975,
         "ceo": "Bob Smith"},]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description']))
# Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        {
            "name": "Pathfinder",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
            "color": "BLACK"},
        {
            "name": "Qashqai",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
            "color": "WHITE"},
        {
            "name": "XTRAIL",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances[0],
            "color": "RED"},
        {
          "name": "A-Class",
          "type": "SUV", "year": 2023,
          "car_make": car_make_instances[1],
          "color": "BLACK"},
        {
          "name": "C-Class",
          "type": "SUV",
          "year": 2023,
          "car_make": car_make_instances[1],
          "color": "WHITE"},
        {
          "name": "E-Class",
          "type": "SUV",
          "year": 2023,
          "car_make": car_make_instances[1],
          "color": "GREEN"},
        {
          "name": "A4",
          "type": "SUV",
          "year": 2023,
          "car_make": car_make_instances[2],
          "color": "BLACK"},
        {
          "name": "A5",
          "type": "SUV",
          "year": 2023,
          "car_make": car_make_instances[2],
          "color": "WHITE"},
        {
          "name": "A6",
          "type": "SUV",
          "year": 2023,
          "car_make": car_make_instances[2],
          "color": "BLACK"},
        {
          "name": "Sorrento",
          "type": "SUV",
          "year": 2023,
          "car_make": car_make_instances[3],
          "color": "BLACK"},
        {
          "name": "Carnival",
          "type": "SUV",
          "year": 2023,
          "car_make": car_make_instances[3],
          "color": "WHITE"},
        {
          "name": "Cerato",
          "type": "Sedan",
          "year": 2023,
          "car_make": car_make_instances[3],
          "color": "BLACK"},
        {
          "name": "Corolla",
          "type": "Sedan",
          "year": 2023,
          "car_make": car_make_instances[4],
          "color": "BLUE"},
        {
          "name": "Camry",
          "type": "Sedan",
          "year": 2023,
          "car_make": car_make_instances[4],
          "color": "BLACK"},
        {
          "name": "Kluger",
          "type": "SUV",
          "year": 2023,
          "car_make": car_make_instances[4],
          "color": "RED"
        },
    ]
    for data in car_model_data:
        CarModel.objects.create(name=data['name'],
                                car_make=data['car_make'],
                                type=data['type'],
                                year=data['year'])
