import sqlite3

conn = sqlite3.connect('quiz.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO categories (name) VALUES ('Опознавательные знаки')")
cursor.execute("INSERT INTO categories (name) VALUES ('Нормативные документы')")
cursor.execute("INSERT INTO categories (name) VALUES ('Сигналы')")



# После создания таблиц, но перед commit/close

# 1. Вопрос типа "Верно/Неверно"
#cursor.execute('''
#INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2)
#VALUES (1, 1, 'Ярослав Мудрый основал Москву', 'true_false', 'Неверно', 'Верно', 'Неверно')
#''')

# 2. Вопрос с 2 вариантами ответа
#cursor.execute('''
#INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2)
#VALUES (1, 2, 'Кто написал "Войну и мир"?', 'two_options', 'Лев Толстой', 'Лев Толстой', 'Федор Достоевский')
#''')

# 3. Вопрос с 4 вариантами ответа
#cursor.execute('''
#INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2, option3, option4)
#VALUES (1, 3, 'Сколько планет в Солнечной системе?', 'four_options', '8', '7', '8', '9', '10')
#''')

# 4. Вопрос с изображением
#cursor.execute('''
#INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2, option3, option4, image_path)
#VALUES (1, 1, 'Какой это дорожный знак?', 'four_options', 'Главная дорога', 'Стоп', 'Главная дорога', 'Уступи дорогу', 'Круговое движение', 'images/road_sign.jpg')
#''')

# 5. Вопрос с числовым ответом (нужно ввести число)
#cursor.execute('''
#INSERT INTO questions (test_id, category_id, question, question_type, correct_answer)
#VALUES (2, 2, 'Какая максимальная скорость разрешена в жилой зоне? (км/ч)', 'number_input', '20')
#''')

# 6. Вопрос с несколькими правильными ответами (2 из 4)
#cursor.execute('''
#INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2, option3, option4, multiple_correct)
#VALUES (2, 3, 'Какие из этих сигналов являются запрещающими?', 'multiple_choice', 'Красный,Желтый', 'Красный', 'Зеленый', 'Желтый', 'Синий', 'Красный,Желтый')
#''')

# 7. Вопрос с 3 правильными ответами из 4
#cursor.execute('''
#INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2, option3, option4, multiple_correct)
#VALUES (3, 1, 'Какие документы должен иметь при себе водитель?', 'multiple_choice', 'Права,СТС,Полис ОСАГО', 'Права', 'СТС', 'Полис ОСАГО', 'Медицинский полис', 'Права,СТС,Полис ОСАГО')
# ''')

# 8. Еще один вопрос с изображением (2 категория)
#cursor.execute('''
# INSERT INTO questions (test_id, category_id, question, question_type, correct_answer, option1, option2, option3, option4, image_path)
# VALUES (3, 2, 'Что означает этот дорожный знак?', 'four_options', 'Опасный поворот', 'Крутой подъем', 'Опасный поворот', 'Скользкая дорога', 'Неровная дорога', 'images/danger_turn.jpg')
# ''')

#conn.commit()
#conn.close()


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

#160
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5)
VALUES 
(2, 3, 'В качестве переносных светильников должны быть использованы светильники напряжением', 'five_options', 'не выше 12 вольт переменного тока',
'не выше 12 вольт переменного тока', 'не выше 24 вольт постоянного тока', 'не выше 220 вольт переменного тока', 
'не выше 110 вольт переменного тока', 'не выше 36 вольт постоянного тока')
''')

#161
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(2, 3, 'Работа двигателей внутреннего сгорания с перегрузкой не более 10 процентов номинальной мощности допускается в течение', 'four_options', 'не более одного часа',
'не более одного часа', 'не более двух часов', 'не более трех часов', 'не более тридцати минут')
''')

#162
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(2, 3, 'Использовать на судах переносные электрические отопительные приборы', 'four_options', 'запрещается',
'запрещается', 'разрешается, если их суммарная мощность не превышает 20% от общей мощности стационарного электрооборудования', 
'разрешается, после проведения необходимых замеров нагрузки на судовую электрическую сеть', 'разрешается только в жилых помещениях')
''')

#163
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(2, 1, 'При обнаружении пропусков воды в подводной части корпуса как временная мера могут быть допущены цементные заделки', 'four_options', 'не более 3 в одном отсеке',
'не более 3 в одном отсеке', 'не более 1 в одном отсеке', 'не более 2 в одном отсеке', 'не более 5 в одном отсеке')
''')

#164
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(2, 1, 'При обнаружении пропусков воды в подводной части корпуса как временная мера могут быть допущены цементные заделки', 'four_options', 'не более 6 по всему корпусу',
'не более 6 по всему корпусу', 'не более 10 по всему корпусу', 'не более 5 по всему корпусу', 'не более 8 по всему корпусу')
''')

#165
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(2, 3, 'Проверка работоспособности всех элементов дистанционного управления на командном посту управления судном должна выполняться', 'four_options', 'перед каждым выходом судна в рейс',
'не реже одного раза в неделю', 'не реже одного раза в месяц', 'не реже одного раза в две недели', 'перед каждым выходом судна в рейс')
''')

#166
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5)
VALUES 
(2, 3, 'Эксплуатация судна запрещается, если время перехода с основного управления рулем на запасное превышает', 'five_options', '10 секунд',
'5 секунд', '10 секунд', '15 секунд', '30 секунд', '3 секунды')
''')

#167
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5)
VALUES 
(3, 2, 'Перед вводом в эксплуатацию судна, подлежащего государственной регистрации, за исключением маломерных, прогулочных и спортивных парусных судов после зимнего или другого длительного отстоя комиссией судовладельца (эксплуатанта) производится проверка готовности судна к эксплуатации, после чего составляется', 'five_options', 'акт о готовности судна к эксплуатации',
'акт о готовности судна к эксплуатации', 'протокол готовности судна к эксплуатации', 'свидетельство о классификации судна', 'свидетельство о годности судна к плаванию', 'акт о годности судна к плаванию')
''')

#168
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer)
VALUES 
(3, 3, 'Эксплуатация судна запрещается, если погрешность показаний аксиометра превышает градус(ов) при положении руля в диаметральной плоскости', 'number_input', '1')
''')

#169
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Отсутствие на судне свидетельства о минимальном составе экипажа является основанием для временного задержания судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#170
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Отсутствие на судне свидетельства о предотвращении загрязнения окружающей среды с судна является основанием для временного задержания судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#171
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Отсутствие на судне судовой роли является основанием для временного задержания судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#172
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Отсутствие на судне судового журнала является основанием для временного задержания судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#173
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Отсутствие на судне разрешения на судовую радиостанцию (если наличие радиостанции предусмотрено классом судна) является основанием для временного задержания судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#174
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Отсутствие на судне судового санитарного свидетельства о праве плавания является основанием для временного задержания судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#175
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Отсутствие на судне свидетельства о классификации является основанием для временного задержания судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#176
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Отсутствие на судне судового свидетельства об управлении безопасностью является основанием для временного задержания судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#177
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Отсутствие на судне акта о готовности судна к эксплуатации является основанием для временного задержания судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#178
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Превышение габаритов судна над гарантированными габаритами судовых ходов в районе эксплуатации судна является основанием для временного задержания судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#179
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Неисправность авральной и пожарной сигнализации является основанием для временного задержания судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#180
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Система управления безопасностью, применяемая на судне, должна включать в себя способы связи между работниками судовладельца и экипажем судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#181
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Система управления безопасностью, применяемая на судне, должна включать в себя порядок действий членов экипажа судна и других работников судовладельца в случае возникновения аварийных ситуаций', 'true_false', 'верно',
'верно', 'неверно')
''')

#182
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Система управления безопасностью, применяемая на судне, должна включать в себя программы учений экипажа судна по действиям в условиях аварийной ситуации', 'true_false', 'верно',
'верно', 'неверно')
''')

#183
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Система управления безопасностью, применяемая на судне, должна включать в себя порядок ознакомления членов экипажа судна, принятых на работу или назначенных на судно, со своими обязанностями до выхода судна в рейс', 'true_false', 'верно',
'верно', 'неверно')
''')

#184
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Система управления безопасностью, применяемая на судне, должна включать в себя порядок планирования рейса судна и обеспечения безопасности его плавания', 'true_false', 'верно',
'верно', 'неверно')
''')

#185
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Система управления безопасностью, применяемая на судне, должна включать в себя меры по обеспечению надежности механизмов, устройств, оборудования судов, в том числе регулярные проверки механизмов, устройств, оборудования, которые не используются постоянно', 'true_false', 'верно',
'верно', 'неверно')
''')

#186
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Система управления безопасностью, применяемая на судне, должна включать в себя порядок проведения проверок эффективности системы управления безопасностью и при необходимости ее пересмотра', 'true_false', 'верно',
'верно', 'неверно')
''')

#187
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Система управления безопасностью, применяемая на судне, должна включать в себя расписание проведения судовых работ и распорядок дня на судне', 'true_false', 'верно',
'верно', 'неверно')
''')

#188
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Система управления безопасностью, применяемая на судне, должна включать в себя порядок приема и передачи сообщений по УКВ радиосвязи', 'true_false', 'верно',
'верно', 'неверно')
''')

#189
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'При подходе судна к регулируемому участку, а также к пункту местонахождения диспетчерской (контрольного пункта), капитан (вахтенный начальник) судна передает по запросу диспетчера информацию о дате и времени выхода судна в рейс из пункта отправления', 'true_false', 'верно',
'верно', 'неверно')
''')

#190
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'При подходе судна к регулируемому участку, а также к пункту местонахождения диспетчерской (контрольного пункта), капитан (вахтенный начальник) судна передает по запросу диспетчера информацию о полагаемом времени прибытия судна в пункт назначения', 'true_false', 'верно',
'верно', 'неверно')
''')

#191
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'При подходе судна к регулируемому участку, а также к пункту местонахождения диспетчерской (контрольного пункта), капитан (вахтенный начальник) судна передает по запросу диспетчера информацию о роде и количестве груза, количестве пассажиров', 'true_false', 'верно',
'верно', 'неверно')
''')

#192
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'При подходе судна к регулируемому участку, а также к пункту местонахождения диспетчерской (контрольного пункта), капитан (вахтенный начальник) судна передает по запросу диспетчера информацию о вынужденной или намеренной остановке судна в пути и ее окончании', 'true_false', 'верно',
'верно', 'неверно')
''')

#193
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'При подходе судна к регулируемому участку, а также к пункту местонахождения диспетчерской (контрольного пункта), капитан (вахтенный начальник) судна передает по запросу диспетчера информацию о повреждении, неисправности или отсутствии знаков навигационного ограждения', 'true_false', 'верно',
'верно', 'неверно')
''')

#194
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'При подходе судна к регулируемому участку, а также к пункту местонахождения диспетчерской (контрольного пункта), капитан (вахтенный начальник) судна передает по запросу диспетчера информацию о неблагоприятной санитарно-эпидемиологической обстановке на судне', 'true_false', 'верно',
'верно', 'неверно')
''')

#195
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 1, 'Внешней границей головного шлюза шлюзованного участка бассейна ВВП является граница отдельного шлюза, проходящая с внешней стороны по отношению к шлюзованному участку', 'true_false', 'верно',
'верно', 'неверно')
''')

#196
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 1, 'Пассажирские и иные суда, работающие по расписанию, должны пропускаться через шлюз в соответствии с расписанием их движения', 'true_false', 'верно',
'верно', 'неверно')
''')

#197
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer)
VALUES 
(3, 1, 'Пропуск через шлюзы и шлюзованные участки ВВП судов осуществляется по заявке, подаваемой судоводителем диспетчеру шлюза не менее чем за часов до предполагаемого подхода судна к границе шлюза или шлюзованного участка ВВП', 'number_input', '1.5')
''')

#198
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5)
VALUES 
(3, 1, 'Суда, следующие на шлюзование, должны иметь', 'five_options', 'исправное рулевое устройство',
'исправное рулевое устройство', 'исправную УКВ радиостанцию', 'исправное устройство для подачи звуковых сигналов', 'утечек нефти и/или нефтепродуктов', 'выступающих за габаритную ширину')
''')

#199
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5)
VALUES 
(3, 1, 'Суда, следующие на шлюзование, не должны иметь', 'five_options', 'поврежденных элементов корпуса, надстройки, а также частей груза или иных предметов',
'поврежденных элементов корпуса, надстройки, а также частей груза или иных предметов', 'разложенных на палубе швартовных канатов', 'поднятых мачт и антенн', 'утечек нефти и/или нефтепродуктов', 'выступающих за габаритную ширину')
''')

#200
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 1, 'Допускается совместное шлюзование нефтеналивных судов и составов с нефтью и/или нефтепродуктами, а также их остатками, независимо от температуры вспышки паров', 'true_false', 'неверно',
'верно', 'неверно')
''')

#201
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 1, 'Допускается совместное шлюзование сухогрузных судов и составов, судов технического флота с нефтеналивными самоходными судами и составами с нефтью и/или нефтепродуктами, а также их остатками, с температурой вспышки паров 60 °C и выше', 'true_false', 'верно',
'верно', 'неверно')
''')

#202
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 1, 'Допускается совместное шлюзование пассажирских судов (в том числе скоростных) с сухогрузными судами и составами и судами технического флота', 'true_false', 'верно',
'верно', 'неверно')
''')

#203
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 1, 'Допускается совместное шлюзование пассажирских судов (в том числе скоростных) с нефтеналивными самоходными судами и составами с нефтью и/или нефтепродуктами, а также их остатками, с температурой вспышки паров 60 °C и выше', 'true_false', 'неверно',
'верно', 'неверно')
''')

#204
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 1, 'При движении в подходных каналах шлюзов и межшлюзовых бьефах обгон судов, за исключением случаев обгона водоизмещающих судов скоростными судами', 'three_options', 'не допускается',
'допускается только с разрешения диспетчера шлюза', 'не допускается', 'допускается после согласования с обгоняемым судном')
''')

#205
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 1, 'При прохождении судами причальных стенок на подходах к шлюзу обгон судов', 'three_options', 'запрещается',
'допускается только с разрешения диспетчера шлюза', 'запрещается', 'допускается после согласования с обгоняемым судном')
''')

#206
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 1, 'Выход судов из камеры шлюза при нахождении у причальной стенки или у причальных палов не ошвартованных судов, ожидающих шлюзования', 'three_options', 'допускается только с разрешения диспетчера шлюза',
'допускается только с разрешения диспетчера шлюза', 'запрещается', 'допускается после согласования с судном, ожидающим шлюзования')
''')

#207
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer)
VALUES 
(3, 1, 'Минимальный запас по глубине на порогах бетонного шлюза при глубине при глубине 250,1 см и более должен составлять ….. см', 'number_input', '40')
''')

#208
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'Всем радиостанциям на внутренних водных путях запрещается работать на неразрешенных частотах', 'true_false', 'верно',
'верно', 'неверно')
''')

#209
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'Всем радиостанциям на внутренних водных путях запрещается работать с нарушением действующих норм стабильности частоты, ширины полосы излучения и побочных излучений', 'true_false', 'верно',
'верно', 'неверно')
''')

#210
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'Всем радиостанциям на внутренних водных путях запрещается использовать неприсвоенные позывные сигналы', 'true_false', 'верно',
'верно', 'неверно')
''')

#211
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 3, 'Вызовы и сообщения о бедствии, срочности и безопасности передаются', 'three_options', 'только по приказу капитана судна',
'только по приказу капитана судна', 'только капитаном судна', 'вахтенным начальником')
''')

#212
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 3, 'Судовые радиостанции дециметровых волн должны обеспечивать постоянное наблюдение на канале вызова бедствия, срочности и безопасности', 'four_options', '16 канал',
'5 канал', '1 канал', '3 канал', '16 канал')
''')

#213
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'Ведение переговоров на частоте безопасности и бедствия, не связанных с вопросами обеспечения безопасности плавания, запрещается', 'true_false', 'верно',
'верно', 'неверно')
''')

#214
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'При эксплуатации радиостанций на ВВП запрещается использовать частоты, классы и мощности излучения, не указанные в разрешении на судовую радиостанцию', 'true_false', 'верно',
'верно', 'неверно')
''')

#215
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'Лоцман при осуществлении лоцманской проводки имеет право пользоваться судовой радиостанцией и другими средствами связи судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#216
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'Лоцман при осуществлении лоцманской проводки имеет право пользоваться судовыми средствами, позволяющими контролировать местоположение судна', 'true_false', 'верно',
'верно', 'неверно')
''')

#217
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'Лоцман при осуществлении лоцманской проводки имеет право сверять данные, записанные в лоцманской квитанции, с данными, указанными в судовых документах', 'true_false', 'верно',
'верно', 'неверно')
''')

#218
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'Перед началом лоцманской проводки лоцман обязан предъявить капитану судна лоцманское удостоверение', 'true_false', 'верно',
'верно', 'неверно')
''')

#219
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'Перед началом лоцманской проводки лоцман обязан получить у капитана судна информацию о неисправности судовых механизмов, навигационного оборудования (при наличии)', 'true_false', 'верно',
'верно', 'неверно')
''')

#220
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'В перечень участков внутренних водных путей Российской Федерации, типов и размеров судов, подлежащих обязательной лоцманской проводке входит река Нева от 1358 км до 1385 км - для судов, проходящих Санкт-Петербургские мосты', 'true_false', 'верно',
'верно', 'неверно')
''')

#221
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'В перечень участков внутренних водных путей Российской Федерации, типов и размеров судов, подлежащих обязательной лоцманской проводке входит Канал имени Москвы и Москворецкая система', 'true_false', 'верно',
'верно', 'неверно')
''')

#222
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'В перечень участков внутренних водных путей Российской Федерации, типов и размеров судов, подлежащих обязательной лоцманской проводке входит Волго-Балтийский водный путь от Санкт-Петербурга до Череповца', 'true_false', 'верно',
'верно', 'неверно')
''')

#223
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 3, 'Минимальные высотные габариты надводных переходов в путевой информации даются', 'three_options', 'в обязательном порядке',
'только при их несоответствии объявленным в карте', 'не даются', 'в обязательном порядке')
''')

#224
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 3, 'Информация о путевых условиях плавания может передаваться потребителям с использованием проводных линий и радиосвязи', 'four_options', 'по КВ и УКВ радиостанциям',
'по телефону', 'по телефаксу', 'по телеграфу', 'по КВ и УКВ радиостанциям')
''')

#225
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 3, 'Владельцы участков водных путей необщего пользования (акваторий причалов, рейдов, карьеров, затонов и т.п.) обязаны предоставлять судоводителям и районам водных путей (гидросооружений) информацию о порядке и условиях движения и стоянки судов на указанных акваториях и подходах к ним, а также о габаритах акваторий, ветроволновом режиме, опасностях, имеющемся навигационном оборудовании и его действии, дополнительных мерах безопасности и т.п.', 'true_false', 'верно',
'верно', 'неверно')
''')

#226
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Свидетельство о минимальном составе экипажа судна выдается судовладельцу органом, осуществляющим государственную регистрацию судов, по заявлению судовладельца в срок не более двух рабочих дней со дня поступления заявления', 'true_false', 'верно',
'верно', 'неверно')
''')

#227
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(3, 2, 'Свидетельство о минимальном составе экипажа судна должно содержать следующую информацию', 'six_options', 'район и условия плавания',
'режим использования судна по времени', 'режим работы экипажа по времени', 'район и условия плавания', 'степень автоматизации (несение машинной вахты)', 'год постройки судна', 'максимальные габариты судна')
''')

#228
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Положение о минимальном составе экипажей самоходных транспортных судов применяется в отношении судов, зарегистрированных в соответствии с Кодексом внутреннего водного транспорта Российской Федерации в одном из реестров судов Российской Федерации, осуществляющих плавание по внутренним водным путям Российской Федерации, в акваториях морских портов и на подходах к ним, а также прибрежное плавание без захода в иностранные порты, за исключением маломерных судов, используемых в некоммерческих целях, прогулочных и спортивных парусных судов', 'true_false', 'верно',
'верно', 'неверно')
''')

#229
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 2, 'Хранение легковоспламеняющихся материалов в машинном отделении', 'three_options', 'запрещается',
'запрещается', 'разрешается только в специально отведенных местах', 'разрешается только в металлической таре')
''')

#230
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Запрещается на судне ношение обуви без задников, в том числе в свободное от вахт время', 'true_false', 'верно',
'верно', 'неверно')
''')

#231
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'До проведения работ в замкнутых помещениях они должны быть провентилированы, а операции по перекачке или перемещению грузов должны быть приостановлены', 'true_false', 'верно',
'верно', 'неверно')
''')

#232
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Для доступа в замкнутое помещение должны быть открыты не менее двух горловин при их наличии (лазов, люков). Одна из горловин используется для вентиляционных шлангов, систем сжатого воздуха, переносного освещения. Другая горловина предназначена для входа (выхода) людей', 'true_false', 'верно',
'верно', 'неверно')
''')

#233
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 2, 'Работа членов экипажа судна в замкнутых помещениях', 'three_options', 'без наблюдающего запрещается',
'без наблюдающего запрещается', 'допускается только при наличии наблюдающего и ассистента', 'допускается только лицами, имеющими сертификат на выполнение данного вида работ')
''')

#234
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 2, 'В цистернах и танках из-под нефтепродуктов для освещения должны применяться', 'three_options', 'переносные аккумуляторные фонари взрывобезопасного исполнения с напряжением 12 В',
'переносные аккумуляторные фонари взрывобезопасного исполнения с напряжением 12 В', 'переносные светильники напряжением 12 В переменного либо 24 В постоянного тока', 'любые переносные светильники во взрывозащищенном исполнении')
''')

#235
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer)
VALUES 
(3, 2, 'Забортные трапы и сходни должны испытываться один раз в лет и также в случае их ремонта', 'number_input', '1')
''')

#236
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 2, 'В месте установки забортного трапа (сходни) должен находиться', 'four_options', 'спасательный круг с линем',
'спасательный круг с лампочкой автоматического включения и веревкой длиной не менее 30 м', 'спасательный круг', 'спасательный круг с линем', 'спасательный круг с лампочкой автоматического включения')
''')

#237
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5)
VALUES 
(3, 2, 'Перед отдачей якорей руководитель работ, кроме того, должен', 'five_options', 'проверить отсутствие людей в цепном ящике',
'проверить отсутствие людей в цепном ящике', 'проверить исправность якорного устройства', 'проверить крепление ленточного тормоза', 'проверить, нет ли под носовым подзором судна шлюпок, катеров, барж и других плавсредств', 'проверить отсутствие посторонних на палубе судна')
''')

#238
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer)
VALUES 
(3, 2, 'Во время отдачи и подъема якорей следует находиться на расстоянии не ближе м в стороне от линии движения якорь-цепи', 'number_input', '0.6')
''')

#239
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer)
VALUES 
(3, 2, 'При креплении канатов из синтетических материалов на кнехты следует накладывать не менее шлагов', 'number_input', '6')
''')

#240
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer)
VALUES 
(3, 2, 'Смена постельного белья на судах должна проводиться не реже 1 раза в календарных дней', 'number_input', '7')
''')

#241
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Используемые дезинфицирующие и моющие средства, предназначенные для уборки и дезинфекции транспортных средств и объектов транспортной инфраструктуры, и их запасы должны храниться в отдельных помещениях (шкафах), исключающих открытый доступ', 'true_false', 'верно',
'верно', 'неверно')
''')

#242
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Хранение дезинфицирующих средств в жилых и общественных помещениях, помещениях для хранения, приготовления и приема пищи не допускается', 'true_false', 'верно',
'верно', 'неверно')
''')

#243
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 2, 'Нарушение судоводителем или иным лицом, управляющим судном (за исключением маломерного) на внутреннем водном транспорте, правил плавания и стоянки судов, входа судов в порт и выхода их из порта буксировки составов и плотов, подачи звуковых и световых сигналов, несения судовых огней и знаков влечет за собой', 'three_options', 'административный штраф в размере от одной тысячи пятисот до трех тысяч рублей или лишение права управления судном на срок до трех лет',
'административный штраф в размере от пятисот до одной тысячи рублей или лишение права управления судном на срок до одного года', 'административный штраф в размере от одной тысячи пятисот до трех тысяч рублей или лишение права управления судном на срок до трех лет', 'административный штраф в размере от трех до пяти тысяч рублей или лишение права управления судном на срок до пяти лет')
''')

#244
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 2, 'Осуществление капитаном судна плавания без лоцмана в районах обязательной лоцманской проводки судов, за исключением случаев, если судно относится к категории судов, освобождаемых от обязательной лоцманской проводки, или капитану судна предоставлено право осуществлять плавание без лоцмана в установленном порядке влечет за собой', 'three_options', 'административный штраф в размере от одной тысячи пятисот до трех тысяч рублей или лишение права управления судном на срок до трех лет',
'административный штраф в размере от двух тысяч до двух тысяч пятисот рублей или лишение права управления судном на срок до трех месяцев', 'административный штраф в размере от одной тысячи пятисот до трех тысяч рублей или лишение права управления судном на срок до трех лет', 'административный штраф в размере от трех до пяти тысяч рублей или лишение права управления судном на срок до пяти лет')
''')

#245
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 2, 'Необъявление или неправильное объявление капитаном судна лоцману данных об осадке, о длине, ширине и вместимости судна иных данных о судне, которые необходимы лоцману для осуществления лоцманской проводки судна влечет за собой', 'three_options', 'административный штраф в размере от пятисот до одной тысячи рублей',
'административный штраф в размере от пятисот до одной тысячи рублей', 'административный штраф в размере от одной тысячи пятисот до трех тысяч рублей', 'административный штраф в размере от трех до пяти тысяч рублей')
''')

#246
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 2, 'Управление судном лицом, не имеющим права управления этим судном, или передача управления судном лицу, не имеющему права управления влечет за собой', 'three_options', 'административный штраф в размере от одной тысячи до одной тысячи пятисот рублей',
'административный штраф в размере от одной тысячи до одной тысячи пятисот рублей', 'административный штраф в размере от одной тысячи пятисот до трех тысяч рублей', 'административный штраф в размере от трех до пяти тысяч рублей')
''')

#247
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 2, 'Управление судном (в том числе маломерным) судоводителем или иным лицом, находящимися в состоянии опьянения, а равно передача управления судном лицу, находящемуся в состоянии опьянения влечет за собой', 'three_options', 'административный штраф в размере от пятисот до одной тысячи рублей или лишение права управления судном на срок до одного года',
'административный штраф в размере от трех до пяти тысяч рублей', 'административный штраф в размере от одной тысячи пятисот до двух тысяч рублей или лишение права управления', 'административный штраф в размере от пятисот до одной тысячи рублей или лишение права управления судном на срок до одного года')
''')

#248
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 2, 'Свидетельство о праве плавания под Государственным флагом Российской Федерации выдается', 'four_options', 'Администрациями бассейнов внутренних водных путей',
'Администрациями бассейнов внутренних водных путей', 'ФАУ Российский речной регистр', 'территориальными подразделениями Ространснадзора', 'судовладельцем')
''')

#249
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 2, 'Свидетельство о праве собственности на судно выдается', 'four_options', 'Администрациями бассейнов внутренних водных путей',
'Администрациями бассейнов внутренних водных путей', 'ФАУ Российский речной регистр', 'территориальными подразделениями Ространснадзора', 'судовладельцем')
''')

#250
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5)
VALUES 
(3, 2, 'Администрациями бассейнов внутренних водных путей, согласно ст. 14 Кодекса внутреннего водного транспорта, выдаются следующие документы', 'five_options', 'Свидетельство о праве собственности на судно',
'Свидетельство о праве собственности на судно', 'Свидетельство о минимальном составе экипажа судна', 'Судовая роль', 'Разрешение на судовую радиостанцию', 'Мерительное свидетельство')
''')

#251
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Свидетельство о праве собственности на судно может находиться у собственника. На судне должна находиться его копия, заверенная у нотариуса', 'true_false', 'верно',
'верно', 'неверно')
''')

#252
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Свидетельство о праве собственности на судно может находиться у судовладельца. На судне должна находиться его копия, заверенная судовладельцем', 'true_false', 'неверно',
'верно', 'неверно')
''')

#253
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Свидетельство о праве собственности на судно может находиться у собственника. На судне должна находиться его копия, заверенная органом, выдавшим этот документ', 'true_false', 'верно',
'верно', 'неверно')
''')

#254
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 2, 'Пассажирское свидетельство выдается на пассажирское судно', 'four_options', 'ФАУ Российский речной регистр',
'Администрациями бассейнов внутренних водных путей', 'ФАУ Российский речной регистр', 'территориальными подразделениями Ространснадзора', 'судовладельцем')
''')

#255
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 2, 'Мерительное свидетельство выдается на судно', 'four_options', 'ФАУ Российский речной регистр',
'Администрациями бассейнов внутренних водных путей', 'ФАУ Российский речной регистр', 'территориальными подразделениями Ространснадзора', 'судовладельцем')
''')

#256
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(3, 2, 'ФАУ Российский речной регистр, согласно ст. 14 Кодекса внутреннего водного транспорта, выдаются следующие документы', 'six_options', 'свидетельство о классификации',
'пассажирское свидетельство (для пассажирского судна)', 'мерительное свидетельство', 'свидетельство о предотвращении загрязнения окружающей среды с судна', 'свидетельство о годности к плаванию', 'разрешение на судовую радиостанцию', 'свидетельство о классификации')
''')

#257
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 2, 'Свидетельство о минимальном составе экипажа судна выдается', 'four_options', 'Администрациями бассейнов внутренних водных путей',
'Администрациями бассейнов внутренних водных путей', 'ФАУ Российский речной регистр', 'территориальными подразделениями Ространснадзора', 'судовладельцем')
''')

#258
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 2, 'Свидетельство о предотвращении загрязнения окружающей среды с судна выдается', 'four_options', 'ФАУ Российский речной регистр',
'Администрациями бассейнов внутренних водных путей', 'ФАУ Российский речной регистр', 'территориальными подразделениями Ространснадзора', 'судовладельцем')
''')

#259
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 2, 'Судовой журнал, машинный журнал (для судна с механическим двигателем, эксплуатируемого членами экипажа судна без совмещения должностей) должны быть зарегистрированы в', 'four_options', 'Администрациями бассейнов внутренних водных путей',
'Администрациями бассейнов внутренних водных путей', 'ФАУ Российский речной регистр', 'территориальными подразделениями Ространснадзора', 'судовладельцем')
''')

#260
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 2, 'Разрешение на судовую радиостанцию выдается', 'four_options', 'территориальными подразделениями Роскомнадзора',
'Администрациями бассейнов внутренних водных путей', 'ФАУ Российский речной регистр', 'территориальными подразделениями Ространснадзора', 'территориальными подразделениями Роскомнадзора')
''')

#261
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 2, 'Судовое санитарное свидетельство о праве плавания выдается', 'four_options', 'территориальными подразделениями Роспотребнадзора',
'Администрациями бассейнов внутренних водных путей', 'ФАУ Российский речной регистр', 'территориальными подразделениями Ространснадзора', 'территориальными подразделениями Роспотребнадзора')
''')

#262
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 2, 'Свидетельство о классификации судна выдается', 'four_options', 'ФАУ Российский речной регистр',
'Администрациями бассейнов внутренних водных путей', 'ФАУ Российский речной регистр', 'территориальными подразделениями Ространснадзора', 'территориальными подразделениями Роспотребнадзора')
''')

#263
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer)
VALUES 
(3, 2, 'Судовой журнал хранится на судне в течение лет со дня внесения в него последней записи', 'number_input', '2')
''')

#264
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5, option6)
VALUES 
(3, 2, 'На подлежащих государственной регистрации прогулочных судах и маломерных судах должны находиться следующие судовые документы:', 'six_options', 'судовой билет',
'судовой билет', 'судовая роль', 'свидетельство о предотвращении загрязнения окружающей среды с судна', 'свидетельство о годности к плаванию', 'разрешение на судовую радиостанцию', 'свидетельство о классификации')
''')

#265
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer)
VALUES 
(3, 2, 'Разрешение на судовую радиостанцию выдается на срок лет', 'number_input', '10')
''')

#266
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Мерительное свидетельство выдается на срок 5 лет', 'true_false', 'верно',
'верно', 'неверно')
''')

#267
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 2, 'Свидетельство о классификации судна выдается на срок 5 лет', 'true_false', 'верно',
'верно', 'неверно')
''')

#268
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4, option5)
VALUES 
(3, 2, 'Маломерное судно - это', 'five_options', 'судно, длина которого не должна превышать двадцать метров и общее количество людей на котором не должно превышать двенадцать',
'судно, длина которого не должна превышать двадцать метров и общее количество людей на котором не должно превышать двенадцать', 'судно, длина которого не должна превышать двенадцать метров и общее количество людей на котором не должно превышать двенадцать', 'судно, длина которого не должна превышать двадцать метров и общее количество людей на котором не должно превышать двадцать', 'судно, длина которого не должна превышать двенадцать метров и общее количество людей на котором не должно превышать двадцать', 'судно, использующее в качестве двигательной установки подвесной мотор, независимо от его размеров')
''')

#269
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3, option4)
VALUES 
(3, 2, 'Государственный надзор в области внутреннего водного транспорта, за исключением проверок судов и плавучих объектов, осуществляют', 'four_options', 'уполномоченные территориальные управления Ространснадзора',
'уполномоченные территориальные управления Ространснадзора', 'инспекторы государственного портового контроля', 'Администрации бассейнов внутренних водных путей', 'Государственные речные судоходные инспекции')
''')

#270
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2, option3)
VALUES 
(3, 2, 'Прогулочное судно - это', 'three_options', 'судно, которое используется в некоммерческих целях и предназначается для отдыха на водных объектах',
'судно, общее количество людей на котором не должно превышать восемнадцать, в том числе пассажиров не более чем двенадцать', 'судно, которое используется в некоммерческих целях и предназначается для отдыха на водных объектах', 'судно, общее количество людей на котором не должно превышать двадцать, в том числе пассажиров не более чем двенадцать')
''')

#271
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 1, 'Судовой ход - это часть внутреннего водного пути, предназначенная для движения судов и обозначенная навигационными знаками или иным способом', 'true_false', 'верно',
'верно', 'неверно')
''')

#272
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 1, 'Судно - это самоходное или несамоходное плавучее сооружение, предназначенное для использования в целях судоходства, в том числе судно смешанного (река - море) плавания, паром, дноуглубительный и дноочистительный снаряды, плавучий кран и другие технические сооружения подобного рода', 'true_false', 'верно',
'верно', 'неверно')
''')

#273
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 1, 'Плавучий объект - это несамоходное плавучее сооружение', 'true_false', 'верно',
'верно', 'неверно')
''')

#274
cursor.execute('''
INSERT INTO questions (
test_id, category_id, 
question, question_type, correct_answer, 
option1, option2)
VALUES 
(3, 1, 'Навигационно-гидрографическое обеспечение условий плавания судов по внутренним водным путям, за исключением участков пограничных зон Российской Федерации, осуществляется', 'true_false', 'верно',
'верно', 'неверно')
''')

conn.commit()
conn.close()