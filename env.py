import random

class GasSafetyEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.gas_level = random.randint(50, 150)
        self.motion = random.randint(0, 1)
        self.time = random.randint(0, 23)
        return self.get_state()

    def get_state(self):
        return {
            "gas_level": self.gas_level,
            "motion": self.motion,
            "time": self.time
        }

    def step(self, action):
        self.gas_level += random.randint(-10, 50)
        self.gas_level = max(0, min(self.gas_level, 1000))
        self.motion = random.randint(0, 1)

        reward = 0
        danger = self.gas_level > 300 and self.motion == 0

        if action == 1:
            reward = 1 if danger else -0.5
        elif action == 2:
            if danger:
                reward = 1
                self.gas_level = 0
            else:
                reward = -0.5
        else:
            reward = -1 if danger else 0.5

        done = self.gas_level > 800

        return self.get_state(), reward, done