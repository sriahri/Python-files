query=input("query: ") 
print(query) 
data_list = ["ab","bc","cd"]
for i,quote in enumerate(data_list):
    found_at = quote.find(query) 
    if( found_at >= 0):
        print("Found at ", i, "..."+quote[found_at:found_at+50], "...")
    else:
        print("No results found")