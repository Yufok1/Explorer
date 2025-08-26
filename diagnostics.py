import os
import json
import time
from datetime import datetime

class Diagnostics:
    def __init__(self, checkpoint_dir='data/checkpoints', interval_minutes=10):
        self.checkpoint_dir = checkpoint_dir
        self.interval = interval_minutes * 60
        self.last_time_checkpoint = time.time()
        os.makedirs(self.checkpoint_dir, exist_ok=True)

    def save_checkpoint(self, label, state):
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        fname = f'{label}_checkpoint_{ts}.json'
        path = os.path.join(self.checkpoint_dir, fname)
        with open(path, 'w') as f:
            json.dump(state, f, indent=2)
        print(f'[Diagnostics] Checkpoint saved: {path}')

    def maybe_time_checkpoint(self, label, state):
        now = time.time()
        if now - self.last_time_checkpoint >= self.interval:
            self.save_checkpoint(label, state)
            self.last_time_checkpoint = now

    def report(self, state):
        print('[Diagnostics] Comprehensive System Report:')
        print(json.dumps(state, indent=2))
