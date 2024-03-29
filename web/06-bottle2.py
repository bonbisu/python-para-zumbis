import bottle


@bottle.route('/')
def home_page():
    mythings = ['Python', 'Ruby', 'Pearl', 'C++']
    return bottle.template('hello_world2', {'username': 'Bonbisu', 'things': mythings})


@bottle.post('/favorita')
def favorita():
    lang = bottle.request.forms.get('lang')
    if lang == None or lang == '':
        lang = 'Nenhuma escolhida'
    return bottle.template('lang_selection', {'lang': lang})


bottle.debug(True)
bottle.run(host='localhost', port=8082)
