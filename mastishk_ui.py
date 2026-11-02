import tkinter as tk
from tkinter import ttk
import random
import time
import threading

# Backend Modules Connection
from module1_buffer import MastishkBufferSimulator
from module3_safety import EmergencySafetyInterrupter
from module4_glitch import RealityGlitchDetector
from module5_storage import MastishkStorageSystem
from module2_ai_core import AIKnowledgePackGenerator

class MastishkCyberUI:
    def __init__(self, root):
        self.root = root
        self.root.title("⚡ PROJECT M.A.S.T.I.S.H.K. // NEURAL CORE v2.5 ⚡")
        self.root.geometry("850x700")
        self.root.configure(bg="#050508") # Deep Space Cyber Black

        # Core Engines
        self.ai_engine = AIKnowledgePackGenerator()
        self.glitch_detector = RealityGlitchDetector()
        self.database = MastishkStorageSystem(custom_path=r"D:\The_Mastishk_Initiative\Mastishk_Database")

        # Telemetry History
        self.is_running = False
        self.heart_history = [75] * 25
        self.temp_history = [37.0] * 25

        self.create_unique_widgets()

    def create_unique_widgets(self):
        # ─── TOP MAIN TERMINAL HEADER ───
        header_frame = tk.Frame(self.root, bg="#050508")
        header_frame.pack(pady=15, fill="x")
        
        tk.Label(header_frame, text="▲ CORE SYSTEM INTERFACE ▲", font=("Courier New", 10, "bold"), fg="#00FFCC", bg="#050508").pack()
        
        # FIXED LINE HERE: Removed letterspacing option
        tk.Label(header_frame, text="P R O J E C T   M.A.S.T.I.S.H.K.", font=("Impact", 24), fg="#00FFCC", bg="#050508").pack()
        
        # Cyber Separator Line
        canvas_line = tk.Canvas(self.root, height=2, bg="#00FFCC", highlightthickness=0)
        canvas_line.pack(fill="x", padx=40, pady=5)
        canvas_line.create_line(0, 0, 850, 0, fill="#00FFCC", width=2)

        self.status_label = tk.Label(self.root, text="» STATUS: SYSTEM IDLE // AWAITING PROTOCOL SELECTION", font=("Consolas", 10, "bold"), fg="#888888", bg="#050508")
        self.status_label.pack(pady=5)

        # ─── NEON COMMAND CONSOLE (INPUTS) ───
        input_frame = tk.Frame(self.root, bg="#0A0B10", bd=1, highlightbackground="#00FFCC", highlightcolor="#00FFCC", highlightthickness=1)
        input_frame.pack(pady=15, padx=40, fill="x")

        tk.Label(input_frame, text="[TARGET ID]:", fg="#00FFCC", bg="#0A0B10", font=("Consolas", 11, "bold")).grid(row=0, column=0, padx=15, pady=10, sticky="w")
        self.name_entry = tk.Entry(input_frame, font=("Consolas", 11), bg="#12131A", fg="#FFFFFF", insertbackground="#00FFCC", bd=0, width=18, highlightbackground="#222533", highlightthickness=1)
        self.name_entry.insert(0, "Praveen_Kumar")
        self.name_entry.grid(row=0, column=1, padx=5, pady=10)

        tk.Label(input_frame, text="[DATA MATRIX]:", fg="#00FFCC", bg="#0A0B10", font=("Consolas", 11, "bold")).grid(row=0, column=2, padx=25, pady=10, sticky="w")
        self.pack_choices = ["Advanced_Rocket_Science_v1", "Cardiology_Basics_v1", "Fighter_Jet_Pilot_v3", "Quantum_Physics_v2"]
        
        self.pack_dropdown = ttk.Combobox(input_frame, values=self.pack_choices, font=("Consolas", 10), state="readonly", width=28)
        self.pack_dropdown.current(0)
        self.pack_dropdown.grid(row=0, column=3, padx=5, pady=10)

        # ─── TWIN VITAL METRIC GRAPH PANELS ───
        graph_container = tk.Frame(self.root, bg="#050508")
        graph_container.pack(pady=10, padx=35, fill="both", expand=True)

        # Left Panel: Pulse Telemetry
        self.heart_box = tk.Frame(graph_container, bg="#0A0B10", bd=1, highlightbackground="#FF3366", highlightthickness=1)
        self.heart_box.pack(side="left", fill="both", expand=True, padx=8)
        self.heart_title = tk.Label(self.heart_box, text="'D BIOLOGICAL PULSE // -- BPM", fg="#FF3366", bg="#0A0B10", font=("Consolas", 11, "bold"))
        self.heart_title.pack(pady=5)
        self.heart_canvas = tk.Canvas(self.heart_box, bg="#0D0E15", highlightthickness=0)
        self.heart_canvas.pack(pady=5, padx=8, fill="both", expand=True)

        # Right Panel: Thermal Telemetry
        self.temp_box = tk.Frame(graph_container, bg="#0A0B10", bd=1, highlightbackground="#FFAA00", highlightthickness=1)
        self.temp_box.pack(side="right", fill="both", expand=True, padx=8)
        self.temp_title = tk.Label(self.temp_box, text="🌡️ SYNAPTIC HEAT // -- °C", fg="#FFAA00", bg="#0A0B10", font=("Consolas", 11, "bold"))
        self.temp_title.pack(pady=5)
        self.temp_canvas = tk.Canvas(self.temp_box, bg="#0D0E15", highlightthickness=0)
        self.temp_canvas.pack(pady=5, padx=8, fill="both", expand=True)

        # ─── BUFFER STATUS & GLOW PROGRESS ───
        bottom_frame = tk.Frame(self.root, bg="#050508")
        bottom_frame.pack(pady=15, fill="x", padx=40)

        self.progress_title = tk.Label(bottom_frame, text="» READY TO MOUNT TRACK STREAMS...", fg="#888888", bg="#050508", font=("Consolas", 9))
        self.progress_title.pack(anchor="w")

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Cyber.Horizontal.TProgressbar", thickness=12, troughcolor="#12131A", background="#00FFCC")
        self.p_bar = ttk.Progressbar(bottom_frame, style="Cyber.Horizontal.TProgressbar", orient="horizontal", mode="determinate")
        self.p_bar.pack(pady=5, fill="x")

        # ─── FUTURISTIC EMERGE TRIGGER BUTTON ───
        self.btn_start = tk.Button(
            self.root, 
            text="⚡ EXECUTE NEURAL CONVERGENCE ⚡", 
            font=("Consolas", 12, "bold"), 
            bg="#00FFCC", 
            fg="#050508", 
            activebackground="#00CC99", 
            activeforeground="#050508",
            bd=0, 
            padx=20, 
            pady=12, 
            cursor="hand2",
            command=self.start_system_thread
        )
        self.btn_start.pack(pady=15)

    def draw_unique_grid_graph(self, canvas, data_list, color, min_val, max_val, glow_color):
        canvas.delete("all")
        w, h = canvas.winfo_width(), canvas.winfo_height()
        if w < 10: w, h = 360, 200
        
        for i in range(1, 6):
            canvas.create_line(0, h * i / 6, w, h * i / 6, fill="#1B1C26", width=1)
            canvas.create_line(w * i / 6, 0, w * i / 6, h, fill="#1B1C26", width=1)

        points = []
        step_x = w / (len(data_list) - 1)
        val_range = (max_val - min_val) if (max_val - min_val) != 0 else 1
        
        for idx, val in enumerate(data_list):
            x = idx * step_x
            y = h - ((val - min_val) / val_range * (h - 30) + 15)
            points.append((x, y))

        glow_points = [(0, h)] + points + [(w, h)]
        canvas.create_polygon(glow_points, fill=glow_color, stipple="gray12")

        for i in range(len(points) - 1):
            canvas.create_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], fill=color, width=3)
            canvas.create_oval(points[i][0]-2, points[i][1]-2, points[i][0]+2, points[i][1]+2, fill="#FFFFFF", outline=color)

    def start_system_thread(self):
        if not self.is_running:
            self.target_name = self.name_entry.get().strip()
            self.selected_pack = self.pack_dropdown.get()

            if not self.target_name:
                self.status_label.config(text="» ERROR: ACCESS DENIED // TARGET ID UNKNOWN", fg="#FF3366")
                return

            self.is_running = True
            self.btn_start.config(state="disabled", bg="#222533", fg="#555A73", text="SYNAPSE TRANSFER ACTIVE")
            self.name_entry.config(state="disabled")
            
            self.heart_history = [75] * 25
            self.temp_history = [37.0] * 25

            threading.Thread(target=self.core_execution_flow, daemon=True).start()

    def core_execution_flow(self):
        self.root.after(0, lambda: self.status_label.config(text="» AI-MATRIX: Synthesizing Synaptic Bitstream Layers...", fg="#00FFCC"))
        time.sleep(1.0)
        kp_file = self.ai_engine.generate_pack(self.selected_pack, f"Payload stream array matrix {self.selected_pack}")

        self.root.after(0, lambda: self.status_label.config(text="» DEFENSE FIREWALL: Scanning Pulse Integrity Vectors...", fg="#FFAA00"))
        time.sleep(1.0)
        
        if random.random() < 0.15:
            kp_file = self.glitch_detector.inject_random_glitch(kp_file)

        if not self.glitch_detector.verify_integrity(kp_file):
            self.root.after(0, self.trigger_ui_shutdown, "CRITICAL DETONATION: CORRUPTED BIT VECTORS DETECTED")
            self.database.save_session_log(self.target_name, kp_file["Pack_ID"], kp_file["Subject"], "FAILED_GLITCH_BLOCKED", {"Alert": "Malicious vector caught"})
            return

        helmet_system = MastishkBufferSimulator(self.target_name, kp_file["Subject"])
        safety_system = EmergencySafetyInterrupter()
        self.root.after(0, lambda: self.status_label.config(text="» INJECTION LEVEL: ENGAGED // SYNC STATE LINKED", fg="#00FFCC"))

        system_safe = True
        while helmet_system.download_progress < 100 and system_safe:
            time.sleep(0.25)
            
            system_safe = safety_system.monitor_vital_signs()
            if not system_safe:
                self.root.after(0, self.trigger_ui_shutdown, "OVERFLOW FAULT: TARGET EXCEEDED MAXIMUM SAFE BPM")
                self.database.save_session_log(self.target_name, kp_file["Pack_ID"], kp_file["Subject"], "FAILED_VITAL_BPM_ALERT", {"BPM": safety_system.current_heart_rate})
                return

            helmet_system.download_progress += 5
            helmet_system.brain_temperature += random.uniform(0.15, 0.45)

            if helmet_system.brain_temperature > 38.3:
                self.root.after(0, lambda: self.status_label.config(text="» ALERT: CRYOGENIC NEURAL COOLING CYCLE ENGAGED", fg="#FFAA00"))
                time.sleep(0.2)
                helmet_system.brain_temperature -= random.uniform(0.7, 1.2)

            self.heart_history.pop(0)
            self.heart_history.append(safety_system.current_heart_rate)
            
            self.temp_history.pop(0)
            self.temp_history.append(helmet_system.brain_temperature)

            self.root.after(0, self.update_live_ui, helmet_system.download_progress, safety_system.current_heart_rate, helmet_system.brain_temperature)

        self.root.after(0, self.trigger_ui_success)
        self.database.save_session_log(self.target_name, kp_file["Pack_ID"], kp_file["Subject"], "SUCCESS", {"Log": "Process completed normally"})

    def update_live_ui(self, progress, heart, temp):
        self.p_bar['value'] = progress
        self.heart_title.config(text=f"🫀 BIOLOGICAL PULSE // {heart} BPM")
        self.temp_title.config(text=f"🌡️ SYNAPTIC HEAT // {temp:.2f} °C")
        self.progress_title.config(text=f"» Injecting '{self.selected_pack}' data cluster tracks into {self.target_name}:")
        if temp <= 38.3:
            self.status_label.config(text=f"» PROGRESS: Committing code lines to neuron pathways ({progress}%)", fg="#FFFFFF")
        
        self.draw_unique_grid_graph(self.heart_canvas, self.heart_history, "#FF3366", 50, 150, "#3a121c")
        self.draw_unique_grid_graph(self.temp_canvas, self.temp_history, "#FFAA00", 35.0, 40.0, "#3a2a0c")

    def trigger_ui_shutdown(self, reason):
        self.is_running = False
        self.status_label.config(text=f"▲ PROTOCOL ABORTED // {reason}", fg="#FF3366")
        self.btn_start.config(state="normal", bg="#00FFCC", text="⚡ RE-ENGAGE CORE PROTOCOL ⚡")
        self.name_entry.config(state="normal")

    def trigger_ui_success(self):
        self.is_running = False
        self.status_label.config(text="▲ CONVERGENCE INTEGRATION 100% SUCCESSFUL // EXPERT RATIO LOGGED ▲", fg="#00FFCC")
        self.btn_start.config(state="normal", bg="#00FFCC", text="⚡ RUN NEXT CORE SESSION ⚡")
        self.name_entry.config(state="normal")


if __name__ == "__main__":
    window = tk.Tk()
    app = MastishkCyberUI(window)
    window.mainloop()