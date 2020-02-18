import schedule,time
import code
class ancosys:
    eventid =1 
    def print_name(self):
        print(self.eventid)
a = ancosys()

schedule.every(3).seconds.do(a.print_name)

while True:
    
    schedule.run_pending()
    time.sleep(1)
code.interact("host object is available as variable 'h'", local=locals())
