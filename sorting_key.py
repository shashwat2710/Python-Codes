"""In this we will sort list with priority with the help of closure function."""
def sort_priority(values,group):
    def helper(x):
        if x in group:
            return(0,x)
        return(1,x)
    values.sort(key=helper)
    