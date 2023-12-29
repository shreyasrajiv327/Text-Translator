from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from Secretkeys import openapi_key
from difflib import SequenceMatcher
import csv
import os
os.environ['OPENAI_API_KEY']=openapi_key

llm=OpenAI(temperature=0.6)

def translate(language,text):
    prompt_temp=PromptTemplate(
        input_variables =['language','text'],
        template = "{text} the given sentance in the left to the language given in the right {language}"
    )
    #return llm.predict(p)
    response = LLMChain(llm=llm, prompt=prompt_temp, output_key="Translated_text")
    chain = SequentialChain(
        chains=[response],
        input_variables=['language','text'],
        output_variables=['Translated_text']
    )
    final = chain({'language':language,'text':text})
    return final
if __name__ == "__main__":
    print(translate("Italian","How are you?"))

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Skip the header
        next(reader, None)
        return [(row[0].lower().strip(), row[1].lower().strip()) for row in reader]

def find_similarity(original_text, translated_text):
    seq_matcher = SequenceMatcher(None, original_text, translated_text)
    return seq_matcher.ratio()



def similarity(final):
    csv_file_path = "/Users/shreyasr/Documents/Language-Intro/Langchain-Translator/spa-eng/spaeng.csv"
    # Read the contents of the CSV file
    translated_response = final
    dataset_lines = read_csv(csv_file_path)
    translated_response_cleaned = translated_response.lower().strip()
    # Compare the cleaned translated response with each Spanish row in the dataset
    similarities = [find_similarity(spanish_text, translated_response_cleaned) for _, spanish_text in dataset_lines]

    # Find the index of the most similar Spanish row in the dataset
    most_similar_index = similarities.index(max(similarities))

    # Print the most similar Spanish row
    #print(f"Translated Response: {translated_response_cleaned}")
    #print(f"Most Similar Spanish Row in the Dataset: {dataset_lines[most_similar_index][1]}")
    #print(f"Similarity Ratio: ")
    similarityratio={similarities[most_similar_index]}
    print(similarityratio)
    return similarityratio
# Specify the path of your CSV file

