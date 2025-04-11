import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
import random
import time

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


# Клавиатура с тестами
def tests_keyboard():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM tests")
    tests = cursor.fetchall()
    conn.close()

    keyboard = InlineKeyboardMarkup()
    for test_id, name in tests:
        keyboard.add(InlineKeyboardButton(name, callback_data=f"test_{test_id}"))

    return keyboard


# Стартовая команда
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! Я бот-викторина по ПДД. Выбери тест:",
        reply_markup=tests_keyboard()
    )


# Обработка выбора теста
@bot.callback_query_handler(func=lambda call: call.data.startswith('test_'))
def test_selected(call):
    test_id = int(call.data.split('_')[1])

    bot.answer_callback_query(call.id)
    bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text=f"Вы выбрали тест. Начинаем викторину!"
    )

    # Сохраняем данные для пользователя
    user_data = {
        'test_id': test_id,
        'correct': 0,
        'total': 0,
        'start_time': time.time(),
        'current_question': None,
        'asked_questions': set()  # Для отслеживания уже заданных вопросов
    }

    # Сохраняем данные в памяти
    bot.current_user_data = user_data

    ask_question(call.message)


# Задать вопрос
def sanitize_callback_data(data):
    """Очищает данные для callback_data, оставляя только допустимые символы."""
    return ''.join(e for e in data if e.isalnum() or e == '_')

def ask_question(message):
    user_data = getattr(bot, 'current_user_data', None)
    if not user_data:
        bot.send_message(message.chat.id, "Ошибка. Начните заново /start")
        return

    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    try:
        # Получаем вопрос, который еще не задавался
        if user_data['asked_questions']:
            cursor.execute('''
            SELECT id, question, question_type, correct_answer, option1, option2, option3, option4, option5, option6, image_path, multiple_correct 
            FROM questions 
            WHERE test_id = ? AND id NOT IN ({})
            ORDER BY RANDOM() 
            LIMIT 1
            '''.format(','.join(['?'] * len(user_data['asked_questions']))),
                           [user_data['test_id']] + list(user_data['asked_questions']))
        else:
            cursor.execute('''
            SELECT id, question, question_type, correct_answer, option1, option2, option3, option4, option5, option6, image_path, multiple_correct 
            FROM questions 
            WHERE test_id = ?
            ORDER BY RANDOM() 
            LIMIT 1
            ''', [user_data['test_id']])

        question_data = cursor.fetchone()

        if not question_data:
            bot.send_message(message.chat.id, "Вопросы для этого теста закончились!")
            return

        # Распаковываем данные вопроса
        (question_id, question_text, q_type, correct_answer,
         option1, option2, option3, option4, option5, option6,
         image_path, multiple_correct) = question_data

        # Добавляем вопрос в список заданных
        user_data['asked_questions'].add(question_id)

        # Сохраняем текущий вопрос
        user_data['current_question'] = {
            'id': question_id,
            'correct': correct_answer,
            'multiple_correct': multiple_correct.split(',') if multiple_correct else None,
            'start_time': time.time(),
            'type': q_type
        }

        # Создаем клавиатуру в зависимости от типа вопроса
        keyboard = InlineKeyboardMarkup()
        options = [opt for opt in [option1, option2, option3, option4, option5, option6] if opt is not None]

        if q_type == 'number_input':
            bot.send_message(
                message.chat.id,
                f"Вопрос {user_data['total'] + 1}/50:\n{question_text}\n\nВведите число:"
            )
            user_data['total'] += 1
            return

        elif q_type == 'true_false':
            keyboard.add(
                InlineKeyboardButton("Верно", callback_data="answer_Верно"),
                InlineKeyboardButton("Неверно", callback_data="answer_Неверно")
            )

        elif q_type in ['two_options', 'four_options', 'five_options', 'six_options']:
            required_options = {
                'two_options': 2,
                'four_options': 4,
                'five_options': 5,
                'six_options': 6
            }[q_type]

            if len(options) >= required_options:
                shuffled = random.sample(options[:required_options], required_options)
                for option in shuffled:
                    keyboard.add(InlineKeyboardButton(option, callback_data=f"answer_{sanitize_callback_data(option)}"))
            else:
                for option in options:
                    keyboard.add(InlineKeyboardButton(option, callback_data=f"answer_{sanitize_callback_data(option)}"))

        elif q_type == 'multiple_choice':
            for option in options:
                keyboard.add(InlineKeyboardButton(option, callback_data=f"manswer_{sanitize_callback_data(option)}"))
            keyboard.add(InlineKeyboardButton("✅ Готово", callback_data="manswer_done"))

        # Отправляем вопрос с изображением (если есть) или без
        if image_path:
            try:
                with open(image_path, 'rb') as photo:
                    bot.send_photo(
                        message.chat.id,
                        photo,
                        caption=f"Вопрос {user_data['total'] + 1}/50:\n{question_text }",
                        reply_markup=keyboard
                    )
            except Exception as e:
                print(f"Ошибка загрузки изображения: {e}")
                bot.send_message(
                    message.chat.id,
                    f"Вопрос {user_data['total'] + 1}/50:\n{question_text}",
                    reply_markup=keyboard
                )
        else:
            bot.send_message(
                message.chat.id,
                f"Вопрос {user_data['total'] + 1}/50:\n{question_text}",
                reply_markup=keyboard
            )

        user_data['total'] += 1

    except Exception as e:
        print(f"Ошибка при задании вопроса: {e}")
        bot.send_message(message.chat.id, "Произошла ошибка при загрузке вопроса. Попробуйте еще раз.")
    finally:
        conn.close()

# Обработка числового ответа
@bot.message_handler(func=lambda message: getattr(bot, 'current_user_data', None) and
                                          getattr(bot.current_user_data['current_question'], 'type',
                                                  None) == 'number_input')
def handle_number_answer(message):
    user_data = getattr(bot, 'current_user_data', None)
    if not user_data or not user_data.get('current_question'):
        return

    user_answer = message.text.strip()
    correct_answer = user_data['current_question']['correct']
    is_correct = user_answer == correct_answer

    # Обновляем статистику
    if is_correct:
        user_data['correct'] += 1
        feedback = "✅ Верно!"
    else:
        feedback = f"❌ Неверно! Правильный ответ: {correct_answer}"

    bot.send_message(message.chat.id, feedback)
    time.sleep(1)  # Пауза перед следующим вопросом

    # Проверяем, завершен ли тест
    if user_data['total'] >= 50:
        finish_quiz(message)
    else:
        ask_question(message)


# Обработка обычных ответов
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

    bot.answer_callback_query(call.id, feedback)
    time.sleep(1)  # Пауза перед следующим вопросом

    # Проверяем, завершен ли тест
    if user_data['total'] >= 50:
        finish_quiz(call.message)
    else:
        ask_question(call.message)


# Обработка ответов с множественным выбором
@bot.callback_query_handler(func=lambda call: call.data.startswith('manswer_'))
def handle_multiple_answer(call):
    user_data = getattr(bot, 'current_user_data', None)
    if not user_data or not user_data.get('current_question'):
        bot.answer_callback_query(call.id, "Ошибка. Начните заново /start")
        return

    action = call.data.split('_')[1]

    if action == 'done':
        # Проверяем выбранные ответы
        selected_answers = getattr(user_data['current_question'], 'selected_answers', [])
        correct_answers = user_data['current_question']['multiple_correct']

        # Сортируем для сравнения
        selected_sorted = sorted(selected_answers)
        correct_sorted = sorted(correct_answers)

        is_correct = selected_sorted == correct_sorted

        # Обновляем статистику
        if is_correct:
            user_data['correct'] += 1
            feedback = "✅ Верно!"
        else:
            feedback = f"❌ Неверно! Правильные ответы: {', '.join(correct_answers)}"

        bot.answer_callback_query(call.id, feedback)
        time.sleep(1)  # Пауза перед следующим вопросом

        # Проверяем, завершен ли тест
        if user_data['total'] >= 50:
            finish_quiz(call.message)
        else:
            ask_question(call.message)
    else:
        # Добавляем/удаляем выбранный ответ
        selected_answer = '_'.join(call.data.split('_')[1:])
        if not hasattr(user_data['current_question'], 'selected_answers'):
            user_data['current_question']['selected_answers'] = []

        if selected_answer in user_data['current_question']['selected_answers']:
            user_data['current_question']['selected_answers'].remove(selected_answer)
            bot.answer_callback_query(call.id, f"Убрано: {selected_answer}")
        else:
            user_data['current_question']['selected_answers'].append(selected_answer)
            bot.answer_callback_query(call.id, f"Выбрано: {selected_answer}")


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

    # Получаем название теста
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM tests WHERE id = ?", (user_data['test_id'],))
    test_name = cursor.fetchone()[0]
    conn.close()

    # Сохраняем статистику
    save_user_stats(message.from_user.id, user_data)

    # Формируем сообщение с результатами
    result_text = (
        f"🏁 Тест завершен!\n\n"
        f"📚 Тест: {test_name}\n"
        f"⏱ Время прохождения: {minutes} мин {seconds} сек\n"
        f"✅ Правильных ответов: {correct} из {total}\n"
        f"📊 Процент правильных: {percentage:.1f}%\n"
        f"🏆 Ваш статус: {status}\n\n"
        f"Выберите новый тест:"
    )

    bot.send_message(
        message.chat.id,
        result_text,
        reply_markup=tests_keyboard()
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
    WHERE user_id = ? AND test_id = ?
    ''', (user_id, user_data['test_id']))

    existing = cursor.fetchone()

    if existing:
        # Обновляем существующую запись
        new_correct = existing[0] + user_data['correct']
        new_total = existing[1] + user_data['total']
        best_time = min(existing[2] or float('inf'), time.time() - user_data['start_time'])

        cursor.execute('''
        UPDATE user_stats 
        SET correct_answers = ?, total_questions = ?, best_time = ?
        WHERE user_id = ? AND test_id = ?
        ''', (new_correct, new_total, best_time, user_id, user_data['test_id']))
    else:
        # Создаем новую запись
        total_time = time.time() - user_data['start_time']
        cursor.execute('''
        INSERT INTO user_stats (user_id, test_id, correct_answers, total_questions, best_time)
        VALUES (?, ?, ?, ?, ?)
        ''', (user_id, user_data['test_id'], user_data['correct'], user_data['total'], total_time))

    conn.commit()
    conn.close()


# Команда для добавления вопросов
@bot.message_handler(commands=['addq'])
def add_question(message):
    # Проверяем, является ли пользователь администратором
    # if message.from_user.id != ADMIN_ID:  # ADMIN_ID нужно задать
    #     bot.send_message(message.chat.id, "У вас нет прав для добавления вопросов.")
    #     return

    # Запрашиваем данные для нового вопроса
    msg = bot.send_message(message.chat.id, "Введите данные вопроса в следующем формате:\n\n"
                                            "test_id|category_id|question_type|question|correct_answer|option1|option2|option3|option4|image_path(опционально)|multiple_correct(опционально)\n\n"
                                            "Типы вопросов: true_false, two_options, four_options, number_input, multiple_choice")

    bot.register_next_step_handler(msg, process_question_data)


def process_question_data(message):
    try:
        data = message.text.split('|')
        test_id = int(data[0])
        category_id = int(data[1])
        question_type = data[2]
        question = data[3]
        correct_answer = data[4]

        # Обрабатываем опциональные поля
        option1 = data[5] if len(data) > 5 else None
        option2 = data[6] if len(data) > 6 else None
        option3 = data[7] if len(data) > 7 else None
        option4 = data[8] if len(data) > 8 else None
        image_path = data[9] if len(data) > 9 else None
        multiple_correct = data[10] if len(data) > 10 else None

        # Добавляем вопрос в базу данных
        conn = sqlite3.connect('quiz.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO questions 
        (test_id, category_id, question, question_type, correct_answer, option1, option2, option3, option4, image_path, multiple_correct)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
        test_id, category_id, question, question_type, correct_answer, option1, option2, option3, option4, image_path,
        multiple_correct))

        conn.commit()
        conn.close()

        bot.send_message(message.chat.id, "Вопрос успешно добавлен!")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка при добавлении вопроса: {str(e)}")


# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.remove_webhook()  # Delete any existing webhook first
    time.sleep(1)  # Small delay
    bot.infinity_polling()