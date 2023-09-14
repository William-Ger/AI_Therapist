import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import openai

# Load the dataset
data_path = 'LiveLongerData_Cleaned.csv'
data = pd.read_csv(data_path)

# Set OpenAI API key
openai.api_key = 'ENTER-KEY-HERE'

def generate_life_expectancy_report(user_input_text):
    # Semantic analysis and factor extraction
    factor_descriptions = data['factor'].values
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(list(factor_descriptions) + [user_input_text])
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
    top_5_similar_indices = cosine_similarities.argsort()[-5:][::-1]
    similar_factors = data.iloc[top_5_similar_indices]
    
    # Creating a detailed report using GPT-4
    report_sections = []
    for i, (factor, ygl) in enumerate(zip(similar_factors['factor'], similar_factors['years_gained_lost'])):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a therapist"},
                {"role": "user", "content": f"Provide suggestions to improve life expectancy based on the factor: {factor,data['note']}"}],
            temperature=0.4, 
            max_tokens=300
        )
        suggestions = response.choices[0].message.content
        
        section = f"## {i+1}. {factor} ({ygl:+.2f} years)\n\n{suggestions}\n\n"
        report_sections.append(section)
    
    return report_sections

# Get user input and generate a personalized report
user_input_text = input("Please provide a brief description of your lifestyle and areas you wish to improve upon: ")
report_sections = generate_life_expectancy_report(user_input_text)

# Create a markdown document to store the report
md_path = "Consultation_Report.md"

# Create a string to hold the markdown content
md_content = "# Personalized Life Expectancy Enhancement Report\n\nDear User,\n\nBased on the details you provided, here are some personalized suggestions to help improve your life expectancy:\n\n"

# Add each section to the markdown content
for section in report_sections:
    md_content += section

# Add conclusion to the markdown content
md_content += "\n## Conclusion\n\nEvery small positive change can significantly impact your life expectancy. We recommend gradually incorporating the above suggestions into your daily routine.\n"

# Save the markdown content to a file
with open(md_path, 'w') as f:
    f.write(md_content)

# Inform the user that the report has been saved as a markdown file
print(f"The report has been saved as a markdown file at the following location: {md_path}")
