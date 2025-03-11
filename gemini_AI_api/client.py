from google import genai
from google.genai import types


def get_car_ai_bio(model, brand, year):

    gemini_api_key="SUA CHAVE DE API"
    
    prompt = '''
                Me mostre uma descrição de venda para o carro {} {} {} em 250 caracteres.
                Fale coisas específicas e técnicas deste modelo.
             '''
    prompt = prompt.format(brand, model, year)

    client = genai.Client(api_key=gemini_api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
                max_output_tokens=1000,
                temperature=0.1,
        )
    )
    
    return response.text
