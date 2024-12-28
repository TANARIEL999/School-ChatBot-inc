import openai
import gradio as gr

# Set your OpenAI API key
openai.api_key = ""  

# Define the chat function
def chat_with_gpt4(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Specify GPT-4 model
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,  # Adjust the token limit as needed
            temperature=0.7,  # Adjust the creativity level
        )
        # Return the AI's response
        return response.choices[0].message["content"].strip()
    except Exception as e:
        # Handle any errors that occur
        return f"Error: {str(e)}"

# Create the Gradio interface
iface = gr.Interface(
    fn=chat_with_gpt4,
    inputs="text",
    outputs="text",
    title="GPT-4 Chatbot",
    description="Chat with OpenAI's GPT-4",
    theme="compact dark",  # Optional: change the theme if desired
)

# Launch the interface
iface.launch(share=True)
