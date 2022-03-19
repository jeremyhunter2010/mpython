'''
Change Return Program
'''
print("How much did you buy")
_cost = input()
print("How much are you giving")
_total = input()

_change = int(_total) - int(_cost)

if _change < 0 :
 print("You need to give us " + str(abs(_change)))
elif _change == 0:
 print("You do not have change")
else:
 _register = {
  "1000": 0,
  "500" : 2,
  "200" : 5,
  "100" : 0,
  "50"  : 8,
  "20"  : 10,
  "10"  : 2
 }
 
 for cash, amount in _register.items():
  if str(_change) == cash and amount > 0 :
    print("Your "+ str(cash) +" change is available")
    exit()
  else:
    _check = _change / int(cash)
    if amount >= _check:
      print("Your "+ str(_change) +" change is available")
      exit()
    continue

 print("We do not have change")