def _debugs(_a:vars):
    counter=0
    for _b in _a:
        if len(_b)>0:
        
        
            if _b[0:1]!="_":
                print(_b+"=",end="")
                print(_a[_b])
        counter=counter+1



_value={'hello':1,'a':"hello world....\n",'b':'####################'}


_v=vars()
_v.update(_value)

_a=dict(_v)
_debugs(_a)
