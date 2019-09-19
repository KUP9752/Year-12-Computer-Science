def f():
    print(s)
#end procedure

def p():
    s = "I love London"
    print(s)
#end procedure

def q():
    global s
    s = "I love London"
    print(s)
#end procedure

#s is gloabal and no variable in the f() overrides it, so f() prints whatever s is at the moment
s = 'I love Paris in the summer!'

#By turnin q() or p() off we can see how global and local assignment works in python
p()
q()
f()
