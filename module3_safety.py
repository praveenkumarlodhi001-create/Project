import random

class EmergencySafetyInterrupter:
    def __init__(self):
        self.max_safe_heart_rate = 140  # 140 BPM se upar dimaag ke liye khatra hai
        self.current_heart_rate = 75    # Normal starting heart rate (BPM)

    def monitor_vital_signs(self):
        # Data transfer ke stress se heart rate thoda upar-neeche hota hai
        heart_rate_fluctuation = random.randint(-5, 12)
        self.current_heart_rate += heart_rate_fluctuation
        
        print(f"🫀 [VITAL CHECK] User Heart Rate: {self.current_heart_rate} BPM")
        
        # Safety Check Logic
        if self.current_heart_rate > self.max_safe_heart_rate:
            print(f"\n🚨🚨 [CRITICAL ALERT] Heart Rate Exceeded Safe Limit ({self.current_heart_rate} BPM)!")
            return False  # Danger! System ko band karne ka signal
            
        return True  # Safe to continue