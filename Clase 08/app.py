import gradio
demo = gradio.Blocks()
with demo:
    gradio.Markdown("registro")
    gradio.Textbox(label="Nombre")
    gradio.Button("Enviar")
demo.launch()

 

     