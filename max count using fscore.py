my_tuple=(1,2,3,2,4,2,5,2,6)
max_count=max(my_tuple.count(item) for item in my_tuple)
print(f"maximum count:{max_count}")