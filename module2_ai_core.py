import hashlib
import time
import random

# Saare modules ko import kar rahe hain (Ab Module 5 bhi shamil hai)
from module1_buffer import MastishkBufferSimulator
from module3_safety import EmergencySafetyInterrupter
from module4_glitch import RealityGlitchDetector
from module5_storage import MastishkStorageSystem

class AIKnowledgePackGenerator:
    def __init__(self):
        self.bio_mapping = {
            "a": "0.11v", "b": "0.12v", "c": "0.13v", "d": "0.14v", "e": "0.15v",
            "f": "0.21v", "g": "0.22v", "h": "0.23v", "i": "0.24v", "j": "0.25v",
            "k": "0.31v", "l": "0.32v", "m": "0.33v", "n": "0.34v", "o": "0.35v",
            "p": "0.41v", "q": "0.42v", "r": "0.43v", "s": "0.44v", "t": "0.45v",
            "u": "0.51v", "v": "0.52v", "w": "0.53v", "x": "0.54v", "y": "0.55v", "z": "0.56v",
            " ": "0.00v"
        }

    def generate_pack(self, subject_title, raw_text_knowledge):
        print(f"🤖 [AI CORE] Reading Textbook Material for: {subject_title}...")
        clean_text = raw_text_knowledge.lower().strip()
        
        synaptic_stream = []
        for char in clean_text:
            if char in self.bio_mapping:
                synaptic_stream.append(self.bio_mapping[char])
            else:
                synaptic_stream.append("0.01v")
        
        security_hash = hashlib.sha256(clean_text.encode()).hexdigest()[:8].upper()
        
        return {
            "Pack_ID": f"KP-{security_hash}",
            "Subject": subject_title,
            "Bio_Signals": synaptic_stream
        }

def run_mastishk_system(kp_file, subject_name, db_system):
    """Main execution engine supporting safety, glitch, and storage saves"""
    helmet_system = MastishkBufferSimulator(subject_name, kp_file["Subject"])
    safety_system = EmergencySafetyInterrupter()
    glitch_detector = RealityGlitchDetector()

    # --- STEP 1: GLITCH CHECK ---
    if not glitch_detector.verify_integrity(kp_file):
        print("🛑 [SYSTEM SHUTDOWN] Brain Injection Aborted due to Security Glitch!")
        # Storage mein save karo ki ek Hack Attempt hua tha!
        db_system.save_session_log(
            subject_name, kp_file["Pack_ID"], kp_file["Subject"], 
            "FAILED_SECURITY_BREACH", {"Reason": "Corrupted or malicious pulse detected"}
        )
        print("==================================================")
        return False

    # --- STEP 2: RUN INJECTION ---
    print("\n" + "="*50)
    print(f"🧠 PROJECT M.A.S.T.I.S.H.K. - RUNNING FOR {subject_name.upper()}")
    print("="*50)
    
    system_safe = True
    while helmet_system.download_progress < 100 and system_safe:
        system_safe = safety_system.monitor_vital_signs()
        
        if not system_safe:
            print("🛑 [EMERGENCY SHUTDOWN] Heart Rate Danger! Canceled.")
            db_system.save_session_log(
                subject_name, kp_file["Pack_ID"], kp_file["Subject"], 
                "FAILED_MEDICAL_EMERGENCY", {"Final_Heart_Rate": safety_system.current_heart_rate}
            )
            break
            
        helmet_system.download_progress += helmet_system.buffer_size
        if helmet_system.download_progress > 100: helmet_system.download_progress = 100
        
        helmet_system.brain_temperature += random.uniform(0.2, 0.5)
        print(f"📥 Injecting: {helmet_system.download_progress}% | Brain Temp: {helmet_system.brain_temperature:.2f}°C")
        
        if helmet_system.brain_temperature > 38.3:
            print("❄️ [ALERT] Neural Cooling System Triggered!")
            helmet_system.brain_temperature -= random.uniform(0.7, 1.1)
            
        print("-" * 30)
        time.sleep(0.1)

    if system_safe:
        print(f"\n✅ [PHASE 4] Synaptic Rewrite Complete. {subject_name} is an expert!\n")
        # Storage mein save karo ki run Successful raha!
        db_system.save_session_log(
            subject_name, kp_file["Pack_ID"], kp_file["Subject"], 
            "SUCCESS", {"Final_Brain_Temp": f"{helmet_system.brain_temperature:.2f} C"}
        )
        return True


# ==================================================
# 🚀 TESTING INTERACTION WITH STORAGE SYSTEM
# ==================================================
if __name__ == "__main__":
    ai_engine = AIKnowledgePackGenerator()
    glitch_detector = RealityGlitchDetector()
    
    # Storage system initialized at custom path
    # Aap is path ko badal bhi sakte hain agar D drive na ho toh
    my_database = MastishkStorageSystem(custom_path=r"D:\The_Mastishk_Initiative\Mastishk_Database")
    
    # 🧪 SIMULATION 1: SAFE DATA INJECTION
    print("\n--- 🟢 SIMULATION 1: SAFE DATA INJECTION ---")
    good_pack = ai_engine.generate_pack("Advanced_Rocket_Science_v1", "Propulsion thrust")
    run_mastishk_system(good_pack, "User_Alpha", my_database)
    
    time.sleep(1)

    # 🧪 SIMULATION 2: CORRUPTED DATA ATTACK TEST
    print("\n--- 🔴 SIMULATION 2: CORRUPTED DATA ATTACK TEST ---")
    bad_pack = ai_engine.generate_pack("Fighter_Jet_Pilot_v3", "Supersonic speed maneuvers")
    corrupted_pack = glitch_detector.inject_random_glitch(bad_pack)
    run_mastishk_system(corrupted_pack, "User_Beta", my_database)