def cal_average(score_list):
    n=len(score_list)
    s=0
    for score in score_list:
        s=s+score
    av=s/n
    return av



def is_even(num):
    if num % 2==0:
       return True
    else:
        return False 

def get_high_scores(students_dict,threshold):
    new={}
    for key,value in students_dict.items():
        if value >=threshold:
            new[key]=value
    return new


print(cal_average([80,90,100]))

print(is_even(4))

my_dict={"Alice":85,"Bob":92,"Cindy":78}
result=get_high_scores(my_dict,80)
print(result)