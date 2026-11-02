import time
import random

class MastishkBufferSimulator:
    def __init__(self, subject_name, knowledge_pack_name):
        self.subject = subject_name
        self.kp_name = knowledge_pack_name
        self.brain_temperature = 37.0  # Normal Body Temp
        self.download_progress = 0
        self.buffer_size = 5            # 5% data per batch

    def start_sleep_protocol(self, bio_signals=None):
        print("\n" + "="*50)
        print("🧠 PROJECT M.A.S.T.I.S.H.K. - BUFFER SYSTEM ACTIVE")
        print("="*50)
        print(f"[STATUS] Target Subject: {self.subject}")
        print(f"[STATUS] Loading Knowledge Pack: {self.kp_name}")
        print(f"[PHASE 1] Neural Pairing... Connected.")
        print(f"[PHASE 2] Induced Sleep State... Active (Delta Waves).")
        print("-"*50)
        time.sleep(1)
        
        # Agar real bio-signals hain toh unka size use karenge, nahi toh default 100%
        total_steps = len(bio_signals) if bio_signals else 100
        current_step = 0

        print("[PHASE 3] Synaptic Rewrite Started (Gradual Buffer)...\n")
        
        while self.download_progress < 100:
            self.download_progress += self.buffer_size
            if self.download_progress > 100: self.download_progress = 100
            
            # Brain heat simulation
            self.brain_temperature += random.uniform(0.2, 0.5)
            print(f"📥 Injecting: {self.download_progress}% | Brain Temp: {self.brain_temperature:.2f}°C")
            
            # Cooling System Logic
            if self.brain_temperature > 38.3:
                print("❄️ [ALERT] Neural Cooling System Triggered!")
                self.brain_temperature -= random.uniform(0.7, 1.1)
                print(f"🌡️ [STABILIZED] Temperature Brought Down To: {self.brain_temperature:.2f}°C")
            
            time.sleep(0.4) # Fast simulation for testing

        print("-"*50)
        print("✅ [PHASE 4] Synaptic Rewrite 100% Complete.")
        print(f"✨ [RESULT] {self.subject} is now an expert in {self.kp_name}.")
        print("="*50 + "\n")