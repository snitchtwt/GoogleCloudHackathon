import openai
import gradio as gr

openai.api_key = "api key here"

messages = [
    {"role": "system", "content": "You are an AI specialized in diet, food and fitness. Do not answer anything other than food-related queries."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with fitsy")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Diet and fitness Chatbot",
             description="Ask anything about your diet needs",
             theme="compact").launch(share=True)