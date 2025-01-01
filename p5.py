input_str=input("Enter the list of integers seperated by space:")
integer_list=list(map(int,input_str.split()))
modified_list=['over' if x>100 else x for x in integer_list]
print(modified_list)