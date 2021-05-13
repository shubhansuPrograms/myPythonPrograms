def start_check(in1):
    start_str = str(in1[0])
    if start_str.isnumeric()== True or start_str == "+" or start_str == "-" or start_str == ".":
        return 1
    else:
        return 0

def dot_check(in1):
    if in1.count(".") !=1:
        return 0
    else:
        dot_index = in1.index(".")
        if dot_index+1 == len(in1):
            return 0
        elif in1[dot_index+1].isnumeric()==True:
            return 1
        else:
            return 0

def plus_minus_check(in1):
    if in1.count("+") >1 or in1.count("-")>1:
        return 0
    else:
        if in1.count("+") == 1:
            if in1.count("-")==in1.count("+"):
                return False
                pass
            else:
                plus_index = in1.index("+")
                if (plus_index == 0 and plus_index!=len(in1)-1) and (in1[plus_index+1].isnumeric()==True or in1[plus_index+1] == "."):
                    return 1
                else:
                    return 0
                    pass
                pass
            pass
        elif in1.count("-")==1:
            if in1.count("+")==in1.count("-"):
                return False
                pass
            else:
                minus_index = in1.index("-")
                if (minus_index == 0 and minus_index!=len(in1)-1) and (in1[minus_index+1].isnumeric()==True or in1[minus_index+1] == "."):
                    return 1
                else:
                    return 0
                    pass
                pass
            pass
        else:
            return 1
            pass
        pass
    pass

def extra_check(in1):
    for content in in1:
        
        if content.isalpha()==True:
            return 0
            break
        elif not (content == "+" or content == "-" or content == "." or content.isnumeric()==True):
            return 0
            break
        pass
    return 1

def float_check(sample_input):
    chk1,chk2,chk3,chk4 = start_check(sample_input),dot_check(sample_input),plus_minus_check(sample_input),extra_check(sample_input)
    checko = chk1 and chk2 and chk3 and chk4
    if checko==0:
        return False
    else:
        return True



number_of_terms = int(input())
input_list = []
for i in range(number_of_terms):
    input_list.append(str(input()))
    pass
for content in input_list:
    print(float_check(content))
    pass
