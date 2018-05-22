def is_prime(number):
    # doctests
    """
        >>> [is_prime(n) for n in range(-10, 0)]
        [False, False, False, False, False, False, False, False, False, False]
        >>> is_prime(a)
        Traceback (most recent call last):
        ...
        NameError: name 'a' is not defined
        >>> is_prime(0)
        False
        >>> is_prime(3)
        True
        >>> is_prime(5)
        True
        >>> is_prime(7)
        True
        >>> is_prime(1)
        False
    """        
    try:
        if number > 1:
            for i in range(2, number):
                if(number % i) == 0:
                    return False
                    break
                else:
                    return True
        else:
            return False

    except TypeError:
        raise TypeError

if __name__ == "__main__":
    import doctest
    doctest.testmod()
