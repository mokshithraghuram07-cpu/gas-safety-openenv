import gradio as gr
from env import GasSafetyEnv

env = GasSafetyEnv()

def simulate(gas_level, motion, action):
    env.gas_level = gas_level
    env.motion = motion

    next_state, reward, done = env.step(action)

    if next_state["gas_level"] > 300 and next_state["motion"] == 0:
        status = "⚠️ Danger!"
    elif next_state["gas_level"] > 200:
        status = "⚠️ Warning"
    else:
        status = "✅ Safe"

    return next_state["gas_level"], next_state["motion"], reward, status

with gr.Blocks() as demo:
    gr.Markdown("# 🔥 Smart Gas Safety AI")

    gas = gr.Slider(0, 1000, value=100, label="Gas Level")
    motion = gr.Radio([0, 1], label="Motion (0=No, 1=Yes)")
    action = gr.Radio([0, 1, 2], label="Action")

    btn = gr.Button("Run")

    out1 = gr.Number(label="Next Gas")
    out2 = gr.Number(label="Next Motion")
    out3 = gr.Number(label="Reward")
    out4 = gr.Textbox(label="Status")

    btn.click(simulate, [gas, motion, action], [out1, out2, out3, out4])

demo.launch()