from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from Secretkeys import openapi_key

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
