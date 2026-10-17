from google import genai
from pydantic import BaseModel, Field
from typing import List
class Word(BaseModel):
    word: str = Field(description="Word form.")
    pinyin: str = Field(description="Pronunciation of the word.")
    pos: str = Field(description="Part of speech.")
    meaning: str = Field(description="English gloss definition.")
class Exam(BaseModel):
    lesson_name: str = Field(description="The name of the lesson.")
    lesson_text: str = Field(description="The text of the lesson.")
    words: List[Word]
client = genai.Client()
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Please generate a Chinese lesson in TBCL Level-4 with Pinyin after each sentence, quote each Level-4 word, followed by an exam of 10 words in TBCL Level-4 from the lesson text.",
    response_format={
        "type": "text",
        "mime_type": "application/json",
        "schema": Exam.model_json_schema()
    })
exam = Exam.model_validate_json(interaction.output_text)
print(exam.lesson_name)
print(exam.lesson_text)
for word in exam.words:
    print(word.word, word.pinyin, word.pos, word.meaning)
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, "exam.htm",{"exam": exam})
def result(request):
    return HttpResponse('''<head><style>body{font-family:標楷體}</style></head>恭喜你通過了這一課，請點擊以下連結前往 <a href=4>TBCL第5級</a> 的課文！<br>或返回上頁另生成一課～''')#request.POST["word_1"])
