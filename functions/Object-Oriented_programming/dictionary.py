def dictionary():
        """Return a functional implementation of a dictionary.
        >>> d = dictionary()
        >>> d('setitem', 'A', 1)
        >>> d('setitem', 'B', 2)
        >>> d('getitem', 'B')
        2
        >>> d('setitem', 'B', 3)
        >>> d('getitem', 'B')
        3
        """
        records = []
        def getitem(key):
            matches = [r for r in records if r[0] == key]
            if len(matches) == 1:
                key, value = matches[0]
                return value
        def setitem(key, value):
            nonlocal records
            non_matches = [r for r in records if r[0] != key]
            records = non_matches + [[key, value]]
        def dispatch(message, key=None, value=None):
            if message == 'getitem':
                return getitem(key)
            elif message == 'setitem':
                setitem(key, value)
        return dispatch
