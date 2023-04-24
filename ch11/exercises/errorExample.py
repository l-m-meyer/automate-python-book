def spam():
    bacon()


def bacon():
    raise Exception('This is the error message.')


spam()


# RETURNS TRACEBACK
'''
Traceback (most recent call last):
  File "C:\...\errorExample.py", line 9, in <module>
    spam()
  File "C:\...\errorExample.py", line 2, in spam
    bacon()
  File "C:\...\errorExample.py", line 6, in bacon
    raise Exception('This is the error message.')
Exception: This is the error message.
'''