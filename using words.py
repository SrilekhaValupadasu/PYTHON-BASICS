def concatenate(**letters):
    result=""
    for arg in letters.values():
        result+=arg
    return result
print(concatenate(a="real",b="python",c="is",d="great",e="!"))


#words return space between each words