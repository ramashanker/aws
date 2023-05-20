import csv
import json
import os

json_folder_path = "json_data/"
csv_file_path = "starfleet.csv"
batch_size = 25
count = 0
index = 1

# Create the JSON folder if it does not exist
if not os.path.exists(json_folder_path):
    os.makedirs(json_folder_path)

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
        if count < batch_size:
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
            count = count + 1

        else:
            dynamodb_data = {"Starships": json_list}
            file_path = os.path.join(json_folder_path, f"batch_{index}.json")
            with open(file_path, "w") as json_file:
                json.dump(dynamodb_data, json_file, indent=4)
            count = 0
            index = index + 1
            dynamodb_data = []
            json_list = []
