from env import GasSafetyEnv

env = GasSafetyEnv()

def reset():
    return env.reset()

def step(action):
    return env.step(action)