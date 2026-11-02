import random

class RealityGlitchDetector:
    def __init__(self):
        # Kuch aise toxic/corrupted codes jo dimaag ko harm kar sakte hain
        self.malicious_patterns = ["9.99v", "ERROR_PULSE", "HACKED_DATA"]

    def verify_integrity(self, knowledge_pack):
        print("🔍 [SECURITY] Scanning Knowledge Pack Integrity...")
        
        # 1. Check if data is empty
        if not knowledge_pack or "Bio_Signals" not in knowledge_pack:
            print("🚨 [GLITCH DETECTED] Empty or Invalid Knowledge Pack Structure!")
            return False
            
        # 2. Scanning neural pulses for malicious or corrupted signals
        for pulse in knowledge_pack["Bio_Signals"]:
            if pulse in self.malicious_patterns:
                print(f"🚨 [SECURITY BREACH] Corrupted/Malicious Pulse Detected: '{pulse}'!")
                return False
                
        print("🛡️ [SECURITY] Integrity Check Passed. Data is 100% pure.")
        return True

    def inject_random_glitch(self, knowledge_pack):
        """Yeh function testing ke liye hai, jo jaan-bujhkar data ko corrupt karega"""
        print("⚠️ [SYSTEM TEST] Injecting a fake glitch into the stream for safety testing...")
        # Pack ke beech mein ek galat pulse daal dete hain
        random_index = random.randint(0, len(knowledge_pack["Bio_Signals"]) - 1)
        knowledge_pack["Bio_Signals"][random_index] = "9.99v" # High voltage corruption
        return knowledge_pack