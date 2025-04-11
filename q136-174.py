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
(1, 3, 'Звуковой сигнал "Прошу уменьшить ход"', 'six_options', 'продолжительный и короткий звук',
'один продолжительный звук', 'один короткий звук', 'серия коротких звуков', 
'четыре коротких звука', 'два коротких звука', 'продолжительный и короткий звук')
''')

#137
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 3, 'Звуковой сигнал "Прошу выйти на связь"', 'six_options', 'продолжительный, короткий и продолжительный звук',
'один продолжительный звук', 'один короткий звук', 'серия коротких звуков', 
'четыре коротких звука', 'два продолжительных и два коротких звука', 'продолжительный, короткий и продолжительный звук')
''')

#138
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 3, 'Звуковой сигнал "Я Вас понял"', 'six_options', 'продолжительный, короткий, продолжительный и короткий звук',
'один продолжительный звук', 'один короткий звук', 'серия коротких звуков', 
'четыре коротких звука', 'продолжительный, короткий и продолжительный звук', 'продолжительный, короткий, продолжительный и короткий звук')
''')

#139
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 3, 'Звуковой сигнал "Запрос на обгон"', 'six_options', 'продолжительный, короткий, продолжительный и короткий звук',
'продолжительный, короткий, продолжительный и короткий звук', 'один короткий звук', 'серия коротких звуков', 
'четыре коротких звука', 'продолжительный, короткий и продолжительный звук', 'два продолжительных и два коротких звука')
''')

#140
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 3, 'Звуковой сигнал "Обгон разрешен"', 'six_options', 'два продолжительных звука',
'продолжительный, короткий, продолжительный и короткий звук', 'два продолжительных звука', 'серия коротких звуков', 
'четыре коротких звука', 'продолжительный, короткий и продолжительный звук', 'два продолжительных и два коротких звука')
''')

#141
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 1, 'Минимальный запас воды под днищем судна, при глубине судового хода 301 см и более, при песчаном и галечном грунте составляет', 'six_options', '20 см',
'20 см', '5 см', '10 см', '15 см', '25 см', '40 см')
''')

#142
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 1, 'Минимальный запас воды под днищем судна, при глубине судового хода 301 см и более, при каменистом грунте составляет', 'six_options', '25 см',
'20 см', '5 см', '10 см', '15 см', '25 см', '40 см')
''')

#143
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 1, 'Минимальный запас по высоте при прохождении судов под мостами, при высоте моста над рабочим (фактическим) уровнем воды от 13,1 м до 16,0 м, на свободных реках и водохранилищах составляет', 'six_options', '0,5 м',
'0,2 м', '0,3 м', '0,4 м', '0,5 м', '1 м', '0,1 м')
''')

#144
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 1, 'Минимальный запас по высоте при прохождении судов под мостами, при высоте моста над рабочим (фактическим) уровнем воды от 13,1 м до 16,0 м, на зарегулированных участках составляет', 'six_options', '0,5 м',
'0,2 м', '0,3 м', '0,4 м', '0,5 м', '1 м', '0,1 м')
''')

#145
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 1, 'Минимальный запас по высоте при прохождении судов под мостами, при высоте моста над рабочим (фактическим) уровнем воды 16,1 и более м, на свободных реках и водохранилищах составляет', 'six_options', '0,5 м',
'0,2 м', '0,3 м', '0,4 м', '0,5 м', '1 м', '0,1 м')
''')

#146
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 1, 'Минимальный запас по высоте при прохождении судов под мостами, при высоте моста над рабочим (фактическим) уровнем воды 16,1 и более м, на зарегулированных участках составляет', 'six_options', '0,5 м',
'0,2 м', '0,3 м', '0,4 м', '0,5 м', '1 м', '0,1 м')
''')


#147
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 2, 'Самоходное судно с механическим двигателем считается находящимся на ходу, если оно', 'six_options', 'находится в движении, используя для этого механический двигатель',
'не стоит на якоре', 'не ошвартовано к берегу', 'не стоит на мели', 
'находится в движении, используя для этого механический двигатель', 'имеет ход относительно воды', 'движется со скоростью более 5 км/ч')
''')

#148
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 2, 'При плавании судов по ВВП, на которых установлена система разделения движения, судно с механическим двигателем длиной более 20 метров может использовать зону прибрежного плавания, в случаях:', 'six_options', 'для избежания непосредственной опасности',
'если оно следует к какому-либо месту, которое находится в пределах зоны прибрежного плавания', 'если оно следует к месту или от места посадки/высадки лоцмана', 
'для избежания непосредственной опасности', 'если габариты судового хода в зоне прибрежного плавания позволяют безопасно следовать там', 'только в светлое время суток', 'только при движении со скоростью не более 10 км/ч')
''')

#149
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 2, 'В условиях ограниченной видимости на каналах независимо от ширины судового хода разрешается двухстороннее движение одиночных самоходных судов с механическим двигателем и толкаемых составов, при условиях:', 'six_options', 'при визуальной видимости не менее двух длин судна (состава) по курсу',
'при визуальной видимости берегов по траверзу', 'при визуальной видимости не менее двух длин судна (состава) по курсу', 
'при визуальной видимости не менее трех длин судна (состава) по курсу', 'при визуальной видимости не менее 500 метров', 'на судне имеется радиолокационная станция', 'на ходовом мостике присутствуют не менее двух судоводителей, один из которых - капитан')
''')

#150
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 2, 'Транспортные происшествия классифицируются на', 'six_options', 'аварии',
'аварии', 'инциденты', 'столкновения судов', 'посадки судов на мель', 'затопление судов', 'повреждение гидротехнических сооружений')
''')

#151
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 2, 'К аварии следует относить', 'six_options', 'транспортные происшествия, в результате которых погибли или получили тяжкие телесные повреждения люди',
'транспортные происшествия, в результате которых погибли или получили тяжкие телесные повреждения люди', 'разрушение судна, которое невозможно и нецелесообразно устранять путем замены или ремонта', 
'посадки судов на мель с простоем свыше 24 часов', 'посадку на мель или повреждение судном гидротехнического сооружения, затопление судна или груза, повлекшее за собой прекращение движения на данном участке пути или шлюзе на 36 часов и более', 'затопление самоходных судов мощностью более 225 киловатт и несамоходных судов порожним водоизмещением более 300 тонн', 'разлив нефти, нефтепродуктов в количестве более 10 тонн')
''')

#152
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(1, 2, 'К аварии следует относить', 'six_options', 'затопление самоходных судов мощностью более 225 киловатт и несамоходных судов порожним водоизмещением более 300 тонн',
'затопление самоходных судов мощностью более 225 киловатт и несамоходных судов порожним водоизмещением более 300 тонн', 'разлив нефти, нефтепродуктов в количестве более 10 тонн', 
'посадки судов на мель с простоем свыше 24 часов', 'посадку на мель или повреждение судном гидротехнического сооружения, затопление судна или груза, повлекшее за собой прекращение движения на данном участке пути или шлюзе на 72 часа и более', 'разрушение судна, которое невозможно и нецелесообразно устранять путем замены или ремонта', 'транспортные происшествия, в результате которых погибли или получили тяжкие телесные повреждения люди')
''')

#153
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(1, 2, 'Затопление самоходного судна мощностью 330 киловатт относится к авариям', 'true_false', 'верно',
'верно', 'неверно')
''')

#154
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(1, 2, 'Затопление самоходного судна мощностью 250 киловатт относится к авариям', 'true_false', 'верно',
'верно', 'неверно')
''')

#155
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(1, 2, 'Повреждение судном гидротехнического сооружения, повлекшее за собой прекращение движения на данном участке пути или шлюзе на 24 часа относится к инцидентам', 'true_false', 'верно',
'верно', 'неверно')
''')

#156
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(1, 2, 'Посадка судна на мель, повлекшее за собой прекращение движения на данном участке пути на 75 часов относится к авариям', 'true_false', 'верно',
'верно', 'неверно')
''')

#157
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(1, 2, 'Разлив нефтепродуктов в количестве 800 килограмм относится к авариям', 'true_false', 'неверно',
'верно', 'неверно')
''')

#158
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(1, 2, 'Посадка судна на мель за пределами судового хода с простоем 12 часов относится к инцидентам', 'true_false', 'верно',
'верно', 'неверно')
''')

#159
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(1, 2, 'Разлив нефтепродуктов в количестве 12 тонн относится к авариям', 'true_false', 'верно',
'верно', 'неверно')
''')





