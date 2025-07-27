import gradio as gr

def SquareNumber(Number):
    return Number ** 2

demo = gr.Interface(
    fn=SquareNumber,
    inputs=gr.Number(label="Enter a Number"),
    outputs=gr.Number(label="Square of the Number"),
    title="Square Calculator",
    description="Enter a number and get its square instantly."
)

demo.launch()
