import os
import json
from datetime import datetime

class MastishkStorageSystem:
    def __init__(self, custom_path=None):
        # Agar aap koi path nahi denge, toh yeh default path use karega
        if custom_path:
            self.db_folder = custom_path
        else:
            self.db_folder = r"D:\The_Mastishk_Initiative\Mastishk_Database"
        
        # Agar laptop mein yeh folder pehle se nahi bana hai, toh code khud bana dega
        if not os.path.exists(self.db_folder):
            os.makedirs(self.db_folder)
            print(f"📁 [STORAGE] New Database Folder Created at: {self.db_folder}")

    def save_session_log(self, subject_name, pack_id, subject_title, status, details):
        """Yeh function har ek run ka data file mein save karega"""
        
        # Current date and time nikalne ke liye
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        log_data = {
            "Timestamp": timestamp,
            "Subject_Name": subject_name,
            "Knowledge_Pack_ID": pack_id,
            "Subject_Title": subject_title,
            "Execution_Status": status,
            "System_Details": details
        }
        
        # File ka naam user ke hisab se unique rakhenge
        file_name = f"{subject_name}_{pack_id}_log.json"
        full_file_path = os.path.join(self.db_folder, file_name)
        
        # Data ko JSON file mein write (save) karna
        with open(full_file_path, 'w') as json_file:
            json.dump(log_data, json_file, indent=4)
            
        print(f"💾 [STORAGE] Session Log Permanently Saved To SSD: {full_file_path}")