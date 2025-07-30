# Script created in Co-Pilot on 10 July 2025 to extract all Sensors from *.yaml files
import os
import yaml

PACKAGES_DIR = "/config/packages"
OUTPUT_FILE = "/config/dashboard_fragments/sensor_cards.yaml"
sensor_cards = []

def extract_sensors(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = yaml.safe_load(f)
            if data and 'sensor' in data:
                for sensor in data['sensor']:
                    name = sensor.get('name', 'Unnamed')
                    entity_id = sensor.get('unique_id') or f"sensor.{name.lower().replace(' ', '_')}"
                    card = {
                        "type": "custom:button-card",
                        "entity": entity_id,
                        "name": name
                    }
                    sensor_cards.append(card)
        except yaml.YAMLError:
            pass

for root, _, files in os.walk(PACKAGES_DIR):
    for file in files:
        if file.endswith(".yaml") or file.endswith(".yml"):
            extract_sensors(os.path.join(root, file))

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    yaml.dump(sensor_cards, out, default_flow_style=False)
