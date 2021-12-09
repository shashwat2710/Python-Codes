'''To Parse Url expression'''
from urllib.parse import parse_qs
myvalues = parse_qs("https://www.youtube.com/watch?v=ot0EDBn0eNA", keep_blank_values=True)
print(myvalues)
