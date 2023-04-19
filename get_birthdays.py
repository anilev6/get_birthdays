from datetime import timedelta, date
import random

names=('Bill','Jill','Kim','Jen','Sophia', 'Jackson', 'Olivia', 'Liam', 'Emma')
#, 'Noah', 'Ava', 'Elijah', 'Isabella', 'Lucas', 'Mia', 'Mason', 'Charlotte', 'Ethan', 'Amelia', 'Oliver', 'Harper', 'Aiden', 'Evelyn', 'Ezra')

users=[{'name':i,
        'birthday':date(random.randint(1945,2005),
                            date.today().month,
                            random.randint(13,28))} for i in names]

#assuming noone was born 29/02
def get_birthdays_per_week(users,n=1): 
      l_names=('Monday','Tuesday','Wednesday','Thursday','Friday')
      l=[[] for i in range(5)] #a list of names per day [mon,tue,wed,thr,fri] 

      tody = date.today()
      interval=timedelta(weeks=n)

      boundary_first=tody
      boundary_last=tody+interval

      if boundary_last.weekday()==5:
            boundary_last-=timedelta(days=1)
      elif boundary_last.weekday()==6:
            boundary_last-=timedelta(days=2)
      elif boundary_first.weekday()==0:
            boundary_first-=timedelta(days=2)    
      elif boundary_first.weekday()==6:
            boundary_first-=timedelta(days=1)

      for d in users:
            datte=date(tody.year,d['birthday'].month,d['birthday'].day)
            
            #sorting into a list l=[mon,tue,wed,thr,fri] assuming max range is one week
            if boundary_first<=datte<=boundary_last:
                  if datte.weekday()==5 or datte.weekday()==6:
                        l[0].append(d['name'])
                  else:
                        l[datte.weekday()].append(d['name'])

      #names comma separated      
      for i in range(5):
            l[i]=','.join(l[i])  


      #output starts with the today day
      l=l[date.today().weekday():]+l[:date.today().weekday()]
      l_names=l_names[date.today().weekday():]+l_names[:date.today().weekday()]
      for i,j in zip(l_names,l):
            if j != '':
                  print(f'{i}:{j}')

# print(users)
get_birthdays_per_week(users)