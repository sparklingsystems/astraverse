import json
from datetime import datetime

def create_event(date, event_name, description, icon):
    return {
        "date": date,
        "events": [
            {
                "eventName": event_name,
                "description": description,
                "icon": icon
            }
        ]
    }

def add_event(events_data, event):
    for existing_event in events_data["events"]:
        if existing_event["date"] == event["date"]:
            existing_event["events"].append(event["events"][0])
            return
    events_data["events"].append(event)

def main():
    events_data = {"events": []}
    
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        event_name = input("Enter the event name: ")
        description = input("Enter the event description: ")
        icon = input("Enter the event icon: ")
        
        event = create_event(date, event_name, description, icon)
        add_event(events_data, event)
        
        more = input("Do you want to add another event? (yes/no): ").lower()
        if more != "yes":
            break
    
    json_data = json.dumps(events_data, indent=2)
    with open("events.json", "w") as json_file:
        json_file.write(json_data)
    
    print("JSON data has been written to events.json")
    print(json_data)

if __name__ == "__main__":
    main()
