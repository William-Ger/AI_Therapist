import pandas as pd
import openai
from txtai.embeddings import Embeddings

# Load the dataset
data_path = 'LiveLongerData_Cleaned.csv'
data = pd.read_csv(data_path)

# Set OpenAI API key
openai.api_key = 'Enter-Key'

def generate_therapy_report(user_input_text):
    # Create an instance of the Embeddings class and build an index with the factor descriptions
    embeddings = Embeddings({"method": "transformers", "path": "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"})
    factor_descriptions = data['factor'].values.tolist()
    embeddings.index([(i, text, None) for i, text in enumerate(factor_descriptions)])

    # Query the index with the user input to find the most similar factors
    results = embeddings.search(user_input_text, 5)
    similar_factors_indices = [x[0] for x in results]
    similar_factors = data.iloc[similar_factors_indices]

    # Creating a detailed report using GPT-4
    report_sections = []
    for i, (factor, ygl) in enumerate(zip(similar_factors['factor'], similar_factors['years_gained_lost'])):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a therapist"},
                {"role": "user", "content": f"Provide suggestions to improve life based on the factor: {factor,data['note']}"}],
            temperature=0.5, 
            max_tokens=300
        )
        suggestions = response.choices[0].message.content
        
        section = f"## {i+1}. {factor} ({ygl:+.2f} years)\n\n{suggestions}\n\n"
        report_sections.append(section)
    
    return report_sections

# Get user input and generate a personalized report
# user_input_text = input("Please provide a brief description of your lifestyle and areas you wish to improve upon: ")
# report_sections = generate_therapy_report(user_input_text)

# # Create a markdown document to store the report
# md_path = "Life_Consultation_Report.md"

# # Create a string to hold the markdown content
# md_content = "# Personalized Life Consulting Report\n\nDear User,\n\nBased on the details you provided, here are some personalized suggestions to help improve your life:\n\n"

# # Add each section to the markdown content
# for section in report_sections:
#     md_content += section

# # Add conclusion to the markdown content
# md_content += "\n## Conclusion\n\nEvery small positive change can significantly impact your life. We recommend gradually incorporating the above suggestions into your daily routine.\n"

# # Save the markdown content to a file
# with open(md_path, 'w') as f:
#     f.write(md_content)

# # Inform the user that the report has been saved as a markdown file
# print(f"The report has been saved as a markdown file at the following location: {md_path}")
