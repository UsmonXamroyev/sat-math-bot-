import json
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "8235456732:AAFI_bcgvaFeESGFUoHM7EWokclLxcCXj2g"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton(
            text="🧮 SAT Math Test",
            web_app={"url": "https://USERNAME.github.io/sat-math-bot/web/"}
        )
    )
    await message.answer("Testni boshlash uchun tugmani bosing 👇", reply_markup=kb)


@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def get_data(message: types.Message):
    user_answers = json.loads(message.web_app_data.data)

    with open("answers.json") as f:
        correct = json.load(f)

    score = 0
    for q, ans in user_answers.items():
        if ans.strip() == str(correct.get(q)):
            score += 1

    await message.answer(f"✅ To‘g‘ri: {score}\n❌ Xato: {len(correct)-score}")


if __name__ == "__main__":
    executor.start_polling(dp)