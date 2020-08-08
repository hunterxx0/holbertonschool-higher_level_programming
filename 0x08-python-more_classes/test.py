a

    >>> class Test:
    ...     t = 'I am a class attribute!'
    >>> x = Test()
    >>> x.t = 'I am an instance attribute!'
    >>> x.t
    'I am a instance attribute!'
    >>> Test.t
    'I am a class attribute!'
    >>>













    >>> class Test:
    ...     t = 'I am a class attribute!'
    ...     def __init__(self, tes='I am an instance attribute!'):
    ...         self.tes = tes
    ...     @property
    ...     def tes(self):
    ...          return self.__tes
    ...     @tes.setter
    ...     def tes(self, tes='I am an instance attribute!'):
    ...         self.__tes = tes
    >>> x = Test()
    >>> y = Test()
    >>> x.tes
    'I am a instance attribute!'
    >>> y.tes
    'I am a class attribute!'
    >>> Test.t
    'I am a class attribute!'
    >>>
