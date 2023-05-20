import csv
import json

csv_file_path = "starfleet.csv"
json_file_path = "data.json"

# Open the CSV file and read its contents
with open(csv_file_path, newline='') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    # Skip the header row
    next(csv_reader)
    # Create an empty list to store the JSON objects
    json_list = []
    dynamodb_data = []
    # Loop through each row in the CSV file
    for row in csv_reader:
        # Create a dictionary to store the values from the CSV row
        data = {
            "PutRequest": {
                "Item": {
                    "Registry": {
                        "S": row[1],
                    },
                    "ShipClass": {
                        "S": row[2],
                    },
                    "Description": {
                        "S": row[3],
                    }
                }
            }
        }

        # Append the dictionary to the list
        json_list.append(data)

    dynamodb_data = {
        "StarShips": json_list
    }

# Write the list of JSON objects to a JSON file
with open(json_file_path, "w") as json_file:
    dynamodb_data
    json.dump(dynamodb_data, json_file, indent=4)
