import time
from threading import Thread, Event
import sys

class Timer:
    def __init__(self):
        self.duration = 0
        self.remaining = 0
        self.running = False
        self.thread = None
        self.stop_event = Event()

    def start(self, duration):
        self.duration = duration
        self.remaining = duration
        self.running = True
        self.stop_event.clear()
        self.thread = Thread(target=self._run)
        self.thread.start()

    def stop(self):
        self.running = False
        self.stop_event.set()
        if self.thread:
            self.thread.join()
        return self.remaining

    def _run(self):
        start_time = time.time()
        while self.running and self.remaining > 0:
            elapsed = time.time() - start_time
            self.remaining = max(0, self.duration - elapsed)
            self._update_display()
            if self.stop_event.wait(0.1):
                break

    def _update_display(self):
        sys.stdout.write(f"\rTime remaining: {self.remaining:.1f}s")
        sys.stdout.flush()

timer = Timer()