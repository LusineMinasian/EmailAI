# get prompt from AI

import openai

def get_prompt(email, style):
    openai.api_key = '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'
    model_engine = 'text-davinci-003'
    prompt = f'перепиши имейл в {style} стиле: {email}'
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=3000,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(completion.choices[0].text)
    return completion.choices[0].text

