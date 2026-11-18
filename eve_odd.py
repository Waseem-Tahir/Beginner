# if else statement in list comprehension
eve_odd={ n:('even' if n%2==0   else 'odd') for n in range(1,10)}
print(eve_odd)