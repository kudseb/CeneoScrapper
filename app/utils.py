#funkcja do usuwania znakow formatujacych
def remove_wspace(string):
    try:
        return features[string].replace('\n',', ').replace('\r',', ')
    except AttributeError:
        pass