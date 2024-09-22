import gradio as gr

def create_interface(fn, inputs, outputs):
    return gr.Interface(fn=fn, inputs=inputs, outputs=outputs)
