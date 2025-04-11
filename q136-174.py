import sqlite3

conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO categories (name) VALUES ('Опознавательные знаки')")
cursor.execute("INSERT INTO categories (name) VALUES ('Нормативные документы')")
cursor.execute("INSERT INTO categories (name) VALUES ('Сигналы')")
conn.commit()
conn.close()


# После создания таблиц, но перед commit/close

# 1. Вопрос типа "Верно/Неверно"
cursor.execute('''
INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2)
VALUES (1, 1, 'Ярослав Мудрый основал Москву', 'true_false', 'Неверно', 'Верно', 'Неверно')
''')

# 2. Вопрос с 2 вариантами ответа
cursor.execute('''
INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2)
VALUES (1, 2, 'Кто написал "Войну и мир"?', 'two_options', 'Лев Толстой', 'Лев Толстой', 'Федор Достоевский')
''')

# 3. Вопрос с 4 вариантами ответа
cursor.execute('''
INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2, option3, option4)
VALUES (1, 3, 'Сколько планет в Солнечной системе?', 'four_options', '8', '7', '8', '9', '10')
''')

# 4. Вопрос с изображением
cursor.execute('''
INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2, option3, option4, image_path)
VALUES (1, 1, 'Какой это дорожный знак?', 'four_options', 'Главная дорога', 'Стоп', 'Главная дорога', 'Уступи дорогу', 'Круговое движение', 'images/road_sign.jpg')
''')

# 5. Вопрос с числовым ответом (нужно ввести число)
cursor.execute('''
INSERT INTO questions (test_id, category_id, question, question_type, correct_answer)
VALUES (2, 2, 'Какая максимальная скорость разрешена в жилой зоне? (км/ч)', 'number_input', '20')
''')

# 6. Вопрос с несколькими правильными ответами (2 из 4)
cursor.execute('''
INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2, option3, option4, multiple_correct)
VALUES (2, 3, 'Какие из этих сигналов являются запрещающими?', 'multiple_choice', 'Красный,Желтый', 'Красный', 'Зеленый', 'Желтый', 'Синий', 'Красный,Желтый')
''')

# 7. Вопрос с 3 правильными ответами из 4
cursor.execute('''
INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2, option3, option4, multiple_correct)
VALUES (3, 1, 'Какие документы должен иметь при себе водитель?', 'multiple_choice', 'Права,СТС,Полис ОСАГО', 'Права', 'СТС', 'Полис ОСАГО', 'Медицинский полис', 'Права,СТС,Полис ОСАГО')
''')

# 8. Еще один вопрос с изображением (2 категория)
cursor.execute('''
INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2, option3, option4, image_path)
VALUES (3, 2, 'Что означает этот дорожный знак?', 'four_options', 'Опасный поворот', 'Крутой подъем', 'Опасный поворот', 'Скользкая дорога', 'Неровная дорога', 'images/danger_turn.jpg')
''')

conn.commit()
conn.close()


#136
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 3, 'Звуковой сигнал "Прошу уменьшить ход"', 'six_options', 'продолжительный и короткий звук'
'один продолжительный звук', 'один короткий звук', 'серия коротких звуков ', 
'четыре коротких звука ', 'два коротких звука', 'продолжительный и короткий звук')
''')


#137
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 3, 'Звуковой сигнал "Прошу выйти на связь"', 'six_options', 'продолжительный, короткий и продолжительный звук'
'один продолжительный звук', 'один короткий звук', 'серия коротких звуков ', 
'четыре коротких звука ', 'два продолжительных и два коротких звука', 'продолжительный, короткий и продолжительный звук')
''')

#138
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 3, 'ЗЗвуковой сигнал "Я Вас понял"', 'six_options', 'продолжительный, короткий, продолжительный и короткий звук'
'один продолжительный звук', 'один короткий звук', 'серия коротких звуков ', 
'четыре коротких звука ', 'продолжительный, короткий и продолжительный звук', 'продолжительный, короткий, продолжительный и короткий звук')
''')





