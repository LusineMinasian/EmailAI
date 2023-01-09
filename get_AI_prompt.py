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

print(get_prompt('Привет как дела Маша', 'бизнес'))
