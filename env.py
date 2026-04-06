import random

class GasSafetyEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.gas_level = random.randint(50, 150)
        self.motion = random.randint(0, 1)
        self.time = random.randint(0, 23)
        return self.state()

    def state(self):
        return {
            "gas_level": self.gas_level,
            "motion": self.motion,
            "time": self.time
        }

    def step(self, action):
        # Simulate gas change
        self.gas_level += random.randint(-10, 50)
        self.gas_level = max(0, min(self.gas_level, 1000))

        # Simulate motion
        self.motion = random.randint(0, 1)

        # Define danger condition
        danger = self.gas_level > 300 and self.motion == 0

        # Reward logic
        if action == 0:  # Do nothing
            reward = -1 if danger else 0.5

        elif action == 1:  # Alert
            reward = 1 if danger else -0.5

        elif action == 2:  # Shut off
            if danger:
                reward = 1
                self.gas_level = 0
            else:
                reward = -0.5

        else:
            reward = -1  # invalid action

        # Episode ends if very high gas
        done = self.gas_level > 800

        return self.state(), reward, done
