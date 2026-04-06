from env import GasSafetyEnv

env = GasSafetyEnv()
state = env.reset()

for _ in range(20):
    gas = state["gas_level"]
    motion = state["motion"]

    if gas > 300 and motion == 0:
        action = 2
    elif gas > 200:
        action = 1
    else:
        action = 0

    state, reward, done = env.step(action)

    print("State:", state, "Reward:", reward)

    if done:
        break