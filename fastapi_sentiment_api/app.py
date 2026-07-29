from transformers import pipeline

# Load the pretrained sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

# Test the model with sample text
sample_text = "I love learning FastAPI."

# Generate prediction
result = classifier(sample_text)

# Display the result
print("Input Text:", sample_text)
print("Prediction:", result)