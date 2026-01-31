import pyodbc
import time
import random
from datetime import datetime

# --- CONFIGURATION ---
server = 'YOUR_AZURE_SERVER.database.windows.net'
database = 'YOUR_AZURE_DB'
username = 'YOUR_AZURE_USERNAME'
password = 'YOUR_AZURE_PASSWORD'
driver = '{ODBC Driver 18 for SQL Server}'  # Standard for Azure

# --- ESTABLISH CONNECTION ---
try:
    conn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;')
    cursor = conn.cursor()
    print("Successfully connected to Azure!")
except Exception as e:
    print(f"Error connecting: {e}")
    exit()

# --- DATA GENERATOR LOOP ---


def send_traffic_data():
    print("Starting Live Stream... Press Ctrl+C to stop.")
    while True:
        try:
            # Generate fake traffic data
            sensor_id = 1
            car_count = random.randint(5, 50)
            avg_speed = round(random.uniform(30.0, 75.0), 2)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # SQL Insert Query
            query = """
            INSERT INTO traffic_table (sensor_id, timestamp, car_count, avg_speed) 
            VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (sensor_id, timestamp, car_count, avg_speed))
            conn.commit()

            print(
                f"[{timestamp}] Sent: {car_count} cars, Avg Speed: {avg_speed} km/h")

            time.sleep(5)  # Send data every 5 seconds
        except Exception as e:
            print(f"Stream error: {e}")
            break


if __name__ == "__main__":
    send_traffic_data()
