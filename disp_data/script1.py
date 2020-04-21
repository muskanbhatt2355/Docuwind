import json

f = open('data.json')
data = json.loads(f.read())

first_name =[]
start_time = []
phone_no = []
res_id = []

# Python program to convert time from 24 hour 
# to 12 hour format 
  
# Convert Function which takes in 
# 24hour time and convert it to 
# 12 hour format 
def convert12(string): 
  
    # Get Hours 
    h1 = ord(string[0]) - ord('0'); 
    h2 = ord(string[1]) - ord('0'); 
  
    hh = h1 * 10 + h2; 
  
    # Finding out the Meridien of time 
    # ie. AM or PM 
    Meridien=""; 
    if (hh < 12): 
        Meridien = "AM"; 
    else: 
        Meridien = "PM"; 
  
    hh %= 12; 
    my_str = '';
  
    # Handle 00 and 12 case separately 
    if (hh == 0): 
        my_str = my_str + '12';
        #print("12", end = ""); 
  
        # Printing minutes and seconds 
        for i in range(2, 8):
            my_str = my_str + string[i];
            #print(string[i], end = ""); 
  
    else:
        my_str = my_str + str(hh) ;
        #req_Time = hh
        #print(hh,end=""); 
          
        # Printing minutes and seconds 
        for i in range(2, 8): 
            my_str = my_str + string[i];
            #req_Time = req_Time + str[i];
            #print(string[i], end = ""); 
  
    # After time is printed 
    # cout Meridien 
    my_str = my_str + ' ' + Meridien;
    return(my_str);
    #print(" " + Meridien); 


if len(first_name)==0:
    for i in data['resource']:
        for j in i:
            if j=='FirstName':
                first_name.append(i[j])
            elif j == 'StartTime':
                datetime = i[j].split()
                date = datetime[0]
                time = datetime[1]
                req_time = convert12(time);
                req_datetime = date + ' ' + req_time
                start_time.append(req_datetime)

            elif j == 'Phoneno':
                phone_no.append(i[j])
            elif j == 'ReservationId':
                res_id.append(i[j])

        

