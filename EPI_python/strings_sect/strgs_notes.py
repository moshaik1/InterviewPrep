
"""
----------------------------------------------------------------
string indexing

    string = "Hello world"

    string[4] => 'o'    


----------------------------------------------------------------
string slicing

    string = "Hello world"

    string[ 0 : 5 ] => "Hello"

    string[ : 5 ] => "Hello"

    string[ 6 : ] => "world"

    string[ 6 : -1 ] => "worl"

    string[ : -1 ] => "Hello worl"

    string[ : : -1 ] => "dlrow olleH"


----------------------------------------------------------------
string 'in' & 'not in' operator

    'Hello' in 'Hello world' => TRUE

    'Hello' in 'Hello' => TRUE

    'HELLO' in 'Hello world' => FALSE

    ' ' in 'span' => TRUE

    'cats' not in 'cats and dogs' => FALSE


----------------------------------------------------------------
upper( ) lower( ) title( )

    greet = 'Hello world"

    greet.upper( ) => HELLO WORLD

    greet.lower( ) => hello world

    greet.title( ) => Hello World

    
----------------------------------------------------------------
isupper( ) islower( )

    return TRUE if all letters are fully upper or fully lower

    -mix of upper and lower returns FALSE

    -numbers return FALSE unless string has lower characters or upper characters

    >>> spam = 'Hello world!' 

    >>> spam.islower() # False 

    >>> spam.isupper() # False 

    >>> 'HELLO'.isupper() # True 

    >>> 'abc12345'.islower() # True 

    >>> '12345'.islower() # False 

    >>> '12345'.isupper() # False



----------------------------------------------------------------
.startswith( ) .endswith( )

    whats does string start with or end with, returns BOOLEAN

----------------------------------------------------------------
.join( )

    takes all items in an iterable, like list, dictionary, tuple, or set and joins them into a string. separator can be specified

----------------------------------------------------------------
.split( )

    splits a string into a list, you can specify where to split. default is that it will use white space to split 

    >>> 'My name is Simon'.split() 

    # ['My', 'name', 'is', 'Simon'] 

    >>> 'MyABCnameABCisABCSimon'.split('ABC') 

    # ['My', 'name', 'is', 'Simon'] 

    >>> 'My name is Simon'.split('m') 

    # ['My na', 'e is Si', 'on']
    

----------------------------------------------------------------
Removing whitespace 

    .strip( ) 

    .rstrip( )

    .lstrip( )

"""