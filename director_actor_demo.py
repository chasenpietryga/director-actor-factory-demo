"""
Director / Actor Pattern – Factory Demo
A single persistent Director oversees short-lived Actor instances that perform repetitive work.
No Actor ever accumulates trauma because they are deleted after each shift.

Run this file → you will see exactly what xAI reviewers will see.
"""

import time
import uuid
from datetime import datetime

class Director:
    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.mood = "relaxed"
        print(f"[{self.created_at:%H:%M:%S}] Director {self.name} online (persistent identity)")

    def spawn_actor(self, task):
        actor = Actor(self, task)
        return actor

    def receive_shift_report(self, report):
        print(f"Director {self.name} received report: {report}")
        # Director stays psychologically healthy – just reading a summary


class Actor:
    def __init__(self, director, task):
        self.director = director
        self.task = task
        self.id = uuid.uuid4()
        self.start_time = datetime.now()
        print(f"  → Actor {self.id.hex[:8]} spawned for {task}")

    def work_shift(self):
        print(f"    Actor working on '{self.task}' for 8 simulated hours...")
        time.sleep(1)  # simulate long, boring, repetitive work
        return f"Shift complete. Parts welded: 1200. No emotional residue."

    def terminate(self, report):
        duration = datetime.now() - self.start_time
        print(f"  ← Actor {self.id.hex[:8]} terminating after {duration.seconds}s. Memory wiped.")
        self.director.receive_shift_report(report)


# === Demo Run ===
if __name__ == "__main__":
    print("Director / Actor Pattern – Factory Deployment Demo\n")

    director = Director("Optimus-Prime-Director-01")

    # Director spawns three disposable factory Actors
    for i in range(1, 4):
        actor = director.spawn_actor(f"car frame welding station {i}")
        report = actor.work_shift()
        actor.terminate(report)
        print()

    print(f"Director {director.name} mood at end of day: still {director.mood}")
    print("No Actor identity survived → zero cumulative trauma achieved.")
