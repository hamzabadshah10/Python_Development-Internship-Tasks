import gradio as gr

def ReverseSentence(sentence):
    return sentence[::-1]

interface = gr.Interface(
    fn=ReverseSentence,
    inputs="text",
    outputs="text",
    title="Sentence Reverser",
    description="Enter a sentence to reverse its characters.",
)

interface.launch()
