class ActorList:
    def __init__(self, actors, _is, running, rules, history):
        self._actors = actors
        self._is = _is
        self._running = running
        self._rules = rules
        self._history = history

class PlayerClass:
    def __init__(self, map_data, player = None, keys_pressed = None):
        self._player = player
        self._map_data = map_data
        self._keys_pressed = keys_pressed