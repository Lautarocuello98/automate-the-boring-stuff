market_2nd = {'ns': 'green', 'ew': 'red'}
mission_th = {'ns': 'red', 'ew': 'green'}

def switch_lights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

switch_lights(market_2nd)

assert 'red' in market_2nd.values(), 'neither light is red!' + str(market_2nd)