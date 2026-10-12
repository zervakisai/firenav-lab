"""FireNav Lab 2D interface: run with python app.py (standard library only)."""
import tkinter as tk
from tkinter import ttk
from firenav.model import Mission
from firenav.demo import scripted_demo_path
from firenav.scenarios import spread_fire_once
from firenav.mission import start_rescue_observation, request_return_to_base
from firenav.replanner import replan_when_needed

CELL = 31
COLORS = {"background":"#0d1726", "ground":"#16283d", "grid":"#284159",
          "fire":"#f45152", "obstacle":"#52677c", "route":"#42b6fa",
          "drone":"#f4da65", "base":"#4be0b1", "target":"#e4a8ff"}

class FireNavApp:
    def __init__(self, root):
        self.root = root
        root.title("FireNav Lab | 2D Wildfire Rescue Mission Planner")
        root.configure(bg=COLORS["background"])
        self.mission = Mission()
        self.demo_points = []
        self.demo_index = 0
        self.demo_running = False

        shell = ttk.Frame(root, padding=12)
        shell.grid(sticky="nsew")
        ttk.Label(shell, text="FIRENAV LAB  •  STUDENT STARTER", font=("Arial", 15, "bold")).grid(row=0,column=0,columnspan=2,sticky="w",pady=(0,8))
        self.canvas = tk.Canvas(shell,width=self.mission.width*CELL,height=self.mission.height*CELL,
                                bg=COLORS["ground"],highlightthickness=0)
        self.canvas.grid(row=1,column=0,sticky="nsew")
        panel = ttk.Frame(shell,padding=(14,0))
        panel.grid(row=1,column=1,sticky="n",padx=(6,0))
        ttk.Label(panel,text="MISSION CONTROL",font=("Arial",11,"bold")).pack(anchor="w",pady=(0,8))
        self.info = ttk.Label(panel,text="",justify="left")
        self.info.pack(anchor="w",pady=(0,14))
        for label, command in [
            ("▶ SCRIPTED DEMO",self.play_demo),
            ("START MISSION  [FIRE-002]",self.start),
            ("SPREAD FIRE  [FIRE-001]",self.change_fire),
            ("REPLAN  [FIRE-004]",self.replan),
            ("RETURN TO BASE",self.return_base),
            ("RESET",self.reset),
        ]:
            ttk.Button(panel,text=label,command=command,width=28).pack(pady=4)
        ttk.Label(panel,text="LEARNING MODE\nDemo is scripted, not autonomous.\nButtons with ticket labels are exercises.",
                  foreground="#52677c",justify="left").pack(anchor="w",pady=(18,5))
        ttk.Label(shell,text="Educational synthetic map • No real wildfire data • Not for operational drone control",
                  foreground="#52677c").grid(row=2,column=0,columnspan=2,sticky="w",pady=(9,0))
        self.draw()

    def point(self, p):
        return (p[0]*CELL+CELL//2,p[1]*CELL+CELL//2)

    def draw(self):
        m=self.mission
        self.canvas.delete("all")
        for x in range(m.width):
            for y in range(m.height):
                self.canvas.create_rectangle(x*CELL,y*CELL,(x+1)*CELL,(y+1)*CELL,
                    fill=COLORS["ground"],outline=COLORS["grid"])
        for cells,color in [(m.obstacles,COLORS["obstacle"]),(m.fire,COLORS["fire"])]:
            for x,y in cells:
                self.canvas.create_rectangle(x*CELL+3,y*CELL+3,(x+1)*CELL-3,(y+1)*CELL-3,
                                             fill=color,outline="")
        if len(m.route)>1:
            xy=[v for p in m.route for v in self.point(p)]
            self.canvas.create_line(*xy,fill=COLORS["route"],width=3)
        for p,text_,color in [(m.base,"B",COLORS["base"]),(m.target,"T",COLORS["target"]),(m.position,"●",COLORS["drone"])]:
            x,y=self.point(p)
            self.canvas.create_oval(x-11,y-11,x+11,y+11,fill=color,outline="")
            self.canvas.create_text(x,y,text=text_,fill=COLORS["background"],font=("Arial",10,"bold"))
        self.info.config(text=f"State: {m.state}\nPosition: {m.position}\nBattery (demo units): {m.battery}\nFire cells: {len(m.fire)}\nWaypoints: {len(m.route)}\n\nLatest event:\n"+(m.events[-1] if m.events else "Ready"))

    def reset(self):
        self.demo_running=False
        self.mission=Mission()
        self.draw()

    def play_demo(self):
        self.reset()
        self.demo_points=scripted_demo_path(self.mission)
        self.demo_index=0
        self.mission.route=self.demo_points[:]
        self.mission.state="SCRIPTED_DEMO"
        self.mission.events.append("Scripted playback only — student A* not implemented")
        self.demo_running=True
        self.tick_demo()

    def tick_demo(self):
        if not self.demo_running: return
        if self.demo_index>=len(self.demo_points):
            self.demo_running=False
            self.mission.state="DEMO_FINISHED"
            self.draw()
            return
        self.mission.position=self.demo_points[self.demo_index]
        self.demo_index+=1
        self.draw()
        self.root.after(150,self.tick_demo)

    def start(self):
        self.demo_running=False
        start_rescue_observation(self.mission)
        self.draw()

    def change_fire(self):
        self.demo_running=False
        spread_fire_once(self.mission)
        self.draw()

    def replan(self):
        self.demo_running=False
        replan_when_needed(self.mission)
        self.mission.events.append("Replanning check completed (student TODO)")
        self.draw()

    def return_base(self):
        self.demo_running=False
        request_return_to_base(self.mission)
        self.draw()

if __name__=="__main__":
    root=tk.Tk()
    FireNavApp(root)
    root.mainloop()
