def get_index_of_bracket(text):
    start = text.find("{")
    end = text.rfind("}")
    return start,end

def format_bib(path):
    """
    args:
        path:"txt file of bib"
    """
    with open(path,"a") as f:
        f.write("@")

        
    template = "- {0},**{1}**,{2}, [[Paper]]({3})"

    f = open(path,'r',encoding='UTF-8')
    
    text = f.readlines()

    bib_list = []
    for idx,item in enumerate(text):
        if "@" in item:
            temp = idx 
            bib_list.append(idx)
    bib_text_list = []
    

    for i in range(bib_list.__len__()-1):
        temp = []
        temp.append([item for item in text[bib_list[i]:bib_list[i+1]]])
        bib_text_list.append(temp)

    
    result = []
    for item in bib_text_list:
        url = ""

        for i in item[0]:
            if "title" in i[0:10] and "book" not in i[0:10] and "shorttitle" not in i[0:10]:
                start,end = get_index_of_bracket(i)
                title = i[start+1:end]
            elif "author" in i:
                start,end = get_index_of_bracket(i)
                author = i[start+1:end]
            elif "year" in i:
                start,end = get_index_of_bracket(i)
                year = i[start+1:end]
            
            elif "url" in i and "urldate" not in i:
                start,end = get_index_of_bracket(i)
                url = i[start+1:end]

        final_str =  template.format(author,title,year,url)   
        final_str = final_str.replace("{","")
        final_str = final_str.replace("}","")    
        result.append(final_str)
    return result


if __name__ == "__main__":
    for item in format_bib("bib.txt"):
        print(item)
        print(" ")