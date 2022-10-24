days_of_week=['Sunday','Monday','Tuesday','Wednesday','Thursday', 'Friday','Saturday']

def add_time(start, duration, *args):
    
        [label, meridiam]=start.split(' ')
        [Starthours, Startminutes] =label.split(":")
        [DurationHour, Durationminutes]= duration.split(':')
        
        totalminutes= int(Startminutes) + int(Durationminutes)
        totalhours= int(Starthours) + int(DurationHour)
        
        future_days=0
        if totalminutes >= 60:
                totalminutes -= 60                
                totalhours += 1  
                
        if totalminutes < 10:
                        # .zfill here complete the spaces of the minutes of this way:
                        #pass this "2:2 PM" to this "2:02 PM" for example
                totalminutes=f'{totalminutes}'.zfill(2)
                                                              
        if totalhours >=12:
                #what means the variables: t, r?
                # well represent the number of times it divides in the remainder 
                t, r= divmod(totalhours, 12)
                
                totalhours=r if r else totalhours
                if totalhours > 12:
                        totalhours = totalhours - ((t-1) *12)
                        
                if t>0:        
                
                        if meridiam== 'PM':
                                future_days =((t-1) //2) +1
                        else:        
                                future_days= t//2
                #in the conditional below we check the hour and we switch 'AM' for 'PM'
                if t > 0 and t % 2 != 0:
                        meridiam='AM' if meridiam == 'PM' else 'PM'



                        
                # ReminingHours= totalhours % 12
                # TOO: divide by 12 to get number of days
                # DivisionTotalHours= totalhours // 12
                        
        new_time=str(totalhours)  + ":"
        new_time += str(totalminutes)  +  f" {meridiam}"
        
        if args:
                day=args[0].title()
                if future_days > 0:
                        index=days_of_week.index(day)
                        index+=future_days % 7
                        if index > 6:
                                index = index -7
                        day=days_of_week[index]        
                        
                new_time += f", {day}"
                
        if future_days == 1:
                new_time += " (next day)"
        elif future_days > 1:
                new_time +=f" ({future_days} days later)".rjust(11)                
                
                
    
        return new_time

        
    



print(add_time("2:59 AM", "24:00", "saturDay"))



    #return new_time
    
    
