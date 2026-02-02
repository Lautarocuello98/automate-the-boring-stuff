import random

capitals = {
    'afganistán': 'kabul', 'albania': 'tirana', 'alemania': 'berlín',
    'andorra': 'andorra la vieja', 'angola': 'luanda', 'antigua y barbuda': 'saint john\'s',
    'arabia saudita': 'riad', 'argelia': 'argel', 'argentina': 'buenos aires',
    'armenia': 'ereván', 'australia': 'canberra', 'austria': 'viena',
    'azerbaiyán': 'bakú', 'bahamas': 'nasáu', 'barbados': 'bridgetown',
    'baréin': 'manama', 'bélgica': 'bruselas', 'belice': 'belmopán',
    'benín': 'porto novo', 'bielorrusia': 'minsk', 'botsuana': 'gaborone',
    'brasil': 'brasilia', 'brunéi': 'bandar seri begawan', 'bulgaria': 'sofía',
    'burkina faso': 'uagadugú', 'burundi': 'gitega', 'bután': 'timbu',
    'cabo verde': 'praia', 'camboya': 'nom pen', 'camerún': 'yaundé',
    'canadá': 'ottawa', 'catar': 'doha', 'chad': 'yamena',
    'chile': 'santiago', 'china': 'pekin', 'chipre': 'nicosia',
    'colombia': 'bogotá', 'comoras': 'moroni', 'república del congo': 'brazzaville',
    'república democrática del congo': 'kinsasa', 'corea del norte': 'pionyang',
    'corea del sur': 'seúl', 'costa de marfil': 'yamusukro', 'costa rica': 'san josé',
    'croacia': 'zagreb', 'cuba': 'la habana', 'dinamarca': 'copenhague',
    'djibouti': 'djibouti', 'dominica': 'roseau', 'república dominicana': 'santo domingo',
    'ecuador': 'quito', 'egipto': 'el cairo', 'el salvador': 'san salvador',
    'emiratos árabes unidos': 'abu dabi', 'eritrea': 'asmara', 'eslovaquia': 'bratislava',
    'eslovenia': 'liubliana', 'españa': 'madrid', 'estonia': 'tallin',
    'etiopía': 'adís abeba', 'filipinas': 'manila', 'finlandia': 'helsinki',
    'francia': 'parís', 'gabón': 'libreville', 'gambia': 'banjul',
    'georgia': 'tiflis', 'ghaná': 'acra', 'grecia': 'atenas',
    'granada': 'saint georges', 'guatemala': 'ciudad de guatemala', 'guinea': 'conakri',
    'guinea-bisáu': 'bisáu', 'guinea ecuatorial': 'malabo', 'haití': 'puerto príncipe',
    'honduras': 'tegucigalpa', 'hungría': 'budapest', 'india': 'nueva delhi',
    'indonesia': 'yakarta', 'irán': 'teherán', 'iraq': 'bagdad',
    'irlanda': 'dublín', 'israel': 'jerusalén', 'italia': 'roma',
    'jamaica': 'kingston', 'japón': 'tokio', 'jordania': 'amman',
    'kazajistán': 'nur-sultán', 'kenia': 'nairobi', 'kiribati': 'tarawa',
    'kosovo': 'pristina', 'kuwait': 'ciudad de kuwait', 'kirguistán': 'bishkek',
    'laos': 'vientiane', 'letonia': 'riga', 'líbano': 'beirut',
    'lesoto': 'maseru', 'liberia': 'monrovia', 'libia': 'trípoli',
    'liechtenstein': 'vaduz', 'lituania': 'vilna', 'luxemburgo': 'luxemburgo',
    'madagascar': 'antananarivo', 'malasia': 'kuala lumpur', 'malaui': 'lilongüe',
    'maldivas': 'male', 'mali': 'bamako', 'malta': 'valletta',
    'marruecos': 'rabat', 'mauricio': 'port louis', 'mauritania': 'nouakchott',
    'méxico': 'ciudad de méxico', 'micronesia': 'palikir', 'moldavia': 'chisináu',
    'mónaco': 'mónaco', 'mongolia': 'ulán bator', 'montenegro': 'podgorica',
    'mozambique': 'maputo', 'myanmar': 'naypyidaw', 'namibia': 'windhoek',
    'nauru': 'yaren', 'nepal': 'katmandú', 'nicaragua': 'managua',
    'níger': 'niamey', 'nigeria': 'abuya', 'noruega': 'oslo',
    'nueva zelanda': 'wellington', 'omán': 'mascate', 'países bajos': 'amsterdam',
    'pakistán': 'islamabad', 'palaos': 'melekeok', 'panamá': 'ciudad de panamá',
    'papúa nueva guinea': 'port moresby', 'paraguay': 'asunción', 'perú': 'lima',
    'polonia': 'varsovia', 'portugal': 'lisboa', 'qatar': 'doha',
    'rumanía': 'bucarest', 'rusia': 'moscú', 'ruanda': 'kigali',
    'samoa': 'apia', 'san marino': 'san marino', 'santo tomé y príncipe': 'santo tomé',
    'serbia': 'belgrado', 'seychelles': 'victoria', 'sierra leona': 'freetown',
    'singapur': 'singapur', 'siría': 'damasco', 'sudáfrica': 'pretoria',
    'sudán': 'jartum', 'sudán del sur': 'yuba', 'suecia': 'estocolmo',
    'suiza': 'berna', 'tailandia': 'bangkok', 'tanzania': 'dodoma',
    'togo': 'lomé', 'tonga': 'nukualofa', 'túnez': 'túnez',
    'turquía': 'ankara', 'turkmenistán': 'ashgabat', 'tuvalu': 'funafuti',
    'ucrania': 'kiyv', 'uganda': 'kampala', 'emiratos árabes unidos': 'abu dabi',
    'reino unido': 'londres', 'estados unidos': 'washington d. c.',
    'uruguay': 'montevideo', 'uzbekistán': 'taskent', 'vanuatu': 'port vila',
    'vaticano': 'ciudad del vaticano', 'venezuela': 'caracas',
    'viet nam': 'hanói', 'yemen': 'saná', 'zambia': 'lusaka', 'zimbabue': 'harare'
}

for quizNum in range(1):
    # Abrir archivos de quiz y respuestas
    quizFile = open(f'capitalworld{quizNum + 1}.txt', 'w', encoding='utf-8')
    answerKeyFile = open(f'capitalworld_answers{quizNum + 1}.txt', 'w', encoding='utf-8')

    # Encabezado
    quizFile.write('Nombre:\nFecha:\n\nPeriodo:\n\n')
    quizFile.write((' ' * 20) + f'Quiz de Capitales del Mundo (Formulario {quizNum + 1})\n\n')

    # Mezclar países
    countries = list(capitals.keys())
    random.shuffle(countries)

    # Generar preguntas
    for questionNum in range(len(countries)):
        correctAnswer = capitals[countries[questionNum]]
        wrongAnswers = list(capitals.values())
        wrongAnswers.remove(correctAnswer)
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Escribir pregunta
        quizFile.write(f'{questionNum + 1}. ¿Cuál es la capital de {countries[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}. {answerOptions[i]}\n")
        quizFile.write('\n')

        # Escribir clave de respuestas
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")

    quizFile.close()
    answerKeyFile.close()
