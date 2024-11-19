def params_(a = 1, b = " a ", c = True):
    print (a,b,c,)

print(params_(5))
print(params_(12,4))
print(params_('Привет',12.8, [2,5,8,]))
print(params_())

print(params_(b=25))
print(params_(c=[1,2,3,]))

values_list = [ 12, 'str', False]
values_dict = {'a':1.5, 'b':'Hi', 'c':True}
params_(*values_list)
params_(**values_dict)

values_list2 = [34.8, "Hi"]
params_(*values_list2,42)