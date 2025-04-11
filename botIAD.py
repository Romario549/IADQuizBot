import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
import random
import time



# conn = sqlite3.connect('quiz.db')
# cursor = conn.cursor()
# cursor.execute("INSERT INTO categories (name) VALUES ('История')")
# cursor.execute("INSERT INTO categories (name) VALUES ('Наука')")
# conn.commit()
# conn.close()


# # Вопрос типа "Верно/Неверно"
# cursor.execute('''
# INSERT INTO questions (category_id, question, question_type, correct_answer, option1, option2)
# VALUES (1, 'Ярослав Мудрый основал Москву', 'true_false', 'Неверно', 'Верно', 'Неверно')
# ''')
#
# # Вопрос с 2 вариантами
# cursor.execute('''
# INSERT INTO questions (category_id, question, question_type, correct_answer, option1, option2)
# VALUES (1, 'Кто написал "Войну и мир"?', 'two_options', 'Лев Толстой', 'Лев Толстой', 'Федор Достоевский')
# ''')
#
# # Вопрос с 4 вариантами
# cursor.execute('''
# INSERT INTO questions (category_id, question, question_type, correct_answer, option1, option2, option3, option4)
# VALUES (2, 'Сколько планет в Солнечной системе?', 'four_options', '8', '7', '8', '9', '10')
# ''')
# Добавление вопроса с изображением
# cursor.execute('''
# INSERT INTO questions (category_id, question, question_type, correct_answer, option1, option2, option3, option4, image_path)
# VALUES (1, 'Какой это архитектурный стиль?', 'four_options', 'Барокко', 'Готика', 'Барокко', 'Ренессанс', 'Классицизм', 'images/baroque.jpg')
# ''')

TOKEN = '8087253865:AAERJhIB87wN2fi1yyl-0Zv3ovSQ3PUgIMw'
bot = telebot.TeleBot(TOKEN)

# Статусы для результатов
STATUSES = {
    1: "Новичок 🟢 (0-30%)",
    2: "Ученик 🔵 (30-50%)",
    3: "Знаток 🟣 (50-70%)",
    4: "Эксперт 🟠 (70-90%)",
    5: "Мастер 🔴 (90-100%)"
}


# Инициализация базы данных
def init_db():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        category_id INTEGER,
        question TEXT NOT NULL,
        question_type TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        image_path TEXT,  
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_stats (
        user_id INTEGER,
        category_id INTEGER,
        correct_answers INTEGER DEFAULT 0,
        total_questions INTEGER DEFAULT 0,
        best_time INTEGER,
        PRIMARY KEY (user_id, category_id)
    )''')

    conn.commit()
    conn.close()


init_db()


# Клавиатура с категориями
def categories_keyboard():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM categories")
    categories = cursor.fetchall()
    conn.close()

    keyboard = InlineKeyboardMarkup()
    for category_id, name in categories:
        keyboard.add(InlineKeyboardButton(name, callback_data=f"category_{category_id}"))

    return keyboard


# Стартовая команда
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! Я бот-викторина. Выбери категорию:",
        reply_markup=categories_keyboard()
    )


# Обработка выбора категории
@bot.callback_query_handler(func=lambda call: call.data.startswith('category_'))
def category_selected(call):
    category_id = int(call.data.split('_')[1])

    bot.answer_callback_query(call.id)
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f"Вы выбрали категорию. Начинаем викторину!"
    )

    # Сохраняем данные для пользователя
    user_data = {
        'category_id': category_id,
        'correct': 0,
        'total': 0,
        'start_time': time.time(),
        'current_question': None
    }

    # Сохраняем данные в памяти (в реальном проекте лучше использовать базу данных)
    bot.current_user_data = user_data

    ask_question(call.message)


# Задать вопрос
def ask_question(message):
    user_data = getattr(bot, 'current_user_data', None)
    if not user_data:
        bot.send_message(message.chat.id, "Ошибка. Начните заново /start")
        return

    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT id, question, question_type, correct_answer, option1, option2, option3, option4, image_path 
    FROM questions 
    WHERE category_id = ? 
    ORDER BY RANDOM() 
    LIMIT 1
    ''', (user_data['category_id'],))

    question_data = cursor.fetchone()
    conn.close()

    if not question_data:
        bot.send_message(message.chat.id, "В этой категории пока нет вопросов.")
        return

    question_id, question_text, q_type, correct, *options, image_path = question_data

    # Обновляем данные вопроса
    user_data['current_question'] = {
        'id': question_id,
        'correct': correct,
        'start_time': time.time()
    }

    # Создаем клавиатуру
    keyboard = InlineKeyboardMarkup()

    if q_type == 'true_false':
        keyboard.add(
            InlineKeyboardButton("Верно", callback_data="answer_Верно"),
            InlineKeyboardButton("Неверно", callback_data="answer_Неверно")
        )
    elif q_type == 'two_options':
        keyboard.add(
            InlineKeyboardButton(options[0], callback_data=f"answer_{options[0]}"),
            InlineKeyboardButton(options[1], callback_data=f"answer_{options[1]}")
        )
    elif q_type == 'four_options':
        shuffled = random.sample(options[:4], 4)  # Берем только первые 4 элемента
        for option in shuffled:
            keyboard.add(InlineKeyboardButton(option, callback_data=f"answer_{option}"))

    # Отправляем изображение (если есть) и вопрос
    if image_path:
        try:
            with open(image_path, 'rb') as photo:
                bot.send_photo(
                    message.chat.id,
                    photo,
                    caption=f"Вопрос {user_data['total'] + 1}/10:\n{question_text}",
                    reply_markup=keyboard
                )
        except FileNotFoundError:
            bot.send_message(
                message.chat.id,
                f"Вопрос {user_data['total'] + 1}/10:\n{question_text}",
                reply_markup=keyboard
            )
    else:
        bot.send_message(
            message.chat.id,
            f"Вопрос {user_data['total'] + 1}/10:\n{question_text}",
            reply_markup=keyboard
        )

    user_data['total'] += 1

# Обработка ответа
@bot.callback_query_handler(func=lambda call: call.data.startswith('answer_'))
def handle_answer(call):
    user_data = getattr(bot, 'current_user_data', None)
    if not user_data or not user_data.get('current_question'):
        bot.answer_callback_query(call.id, "Ошибка. Начните заново /start")
        return

    user_answer = call.data.split('_')[1]
    correct_answer = user_data['current_question']['correct']
    is_correct = user_answer == correct_answer

    # Обновляем статистику
    if is_correct:
        user_data['correct'] += 1
        feedback = "✅ Верно!"
    else:
        feedback = f"❌ Неверно! Правильный ответ: {correct_answer}"

    # Время ответа на вопрос
    question_time = time.time() - user_data['current_question']['start_time']

    bot.answer_callback_query(call.id, feedback)
    time.sleep(1)  # Пауза перед следующим вопросом

    # Проверяем, завершен ли тест
    if user_data['total'] >= 10:
        finish_quiz(call.message)
    else:
        ask_question(call.message)


# Завершение викторины
def finish_quiz(message):
    user_data = getattr(bot, 'current_user_data', None)
    if not user_data:
        bot.send_message(message.chat.id, "Ошибка. Начните заново /start")
        return

    # Рассчитываем результаты
    total_time = time.time() - user_data['start_time']
    minutes = int(total_time // 60)
    seconds = int(total_time % 60)

    correct = user_data['correct']
    total = user_data['total']
    percentage = (correct / total) * 100

    # Определяем статус
    if percentage < 30:
        status = STATUSES[1]
    elif percentage < 50:
        status = STATUSES[2]
    elif percentage < 70:
        status = STATUSES[3]
    elif percentage < 90:
        status = STATUSES[4]
    else:
        status = STATUSES[5]

    # Получаем название категории
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM categories WHERE id = ?", (user_data['category_id'],))
    category_name = cursor.fetchone()[0]
    conn.close()

    # Сохраняем статистику
    save_user_stats(message.from_user.id, user_data)

    # Формируем сообщение с результатами
    result_text = (
        f"🏁 Викторина завершена!\n\n"
        f"📚 Категория: {category_name}\n"
        f"⏱ Время прохождения: {minutes} мин {seconds} сек\n"
        f"✅ Правильных ответов: {correct} из {total}\n"
        f"📊 Процент правильных: {percentage:.1f}%\n"
        f"🏆 Ваш статус: {status}\n\n"
        f"Выберите новую категорию:"
    )

    bot.send_message(
        message.chat.id,
        result_text,
        reply_markup=categories_keyboard()
    )

    # Очищаем данные пользователя
    delattr(bot, 'current_user_data')


# Сохранение статистики пользователя
def save_user_stats(user_id, user_data):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Проверяем существующую запись
    cursor.execute('''
    SELECT correct_answers, total_questions, best_time 
    FROM user_stats 
    WHERE user_id = ? AND category_id = ?
    ''', (user_id, user_data['category_id']))

    existing = cursor.fetchone()

    if existing:
        # Обновляем существующую запись
        new_correct = existing[0] + user_data['correct']
        new_total = existing[1] + user_data['total']
        best_time = min(existing[2] or float('inf'), time.time() - user_data['start_time'])

        cursor.execute('''
        UPDATE user_stats 
        SET correct_answers = ?, total_questions = ?, best_time = ?
        WHERE user_id = ? AND category_id = ?
        ''', (new_correct, new_total, best_time, user_id, user_data['category_id']))
    else:
        # Создаем новую запись
        total_time = time.time() - user_data['start_time']
        cursor.execute('''
        INSERT INTO user_stats (user_id, category_id, correct_answers, total_questions, best_time)
        VALUES (?, ?, ?, ?, ?)
        ''', (user_id, user_data['category_id'], user_data['correct'], user_data['total'], total_time))

    conn.commit()
    conn.close()


# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()