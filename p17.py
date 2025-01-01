my_dict={'b':2,'a':1,'d':4,'c':3}
asc_dict=dict(sorted(my_dict.items()))
des_dict=dict(sorted(my_dict.items(),reverse=True))
print("orginal dictionar:",my_dict)
print("ascending order:",asc_dict)
print("decending order:",des_dict)
