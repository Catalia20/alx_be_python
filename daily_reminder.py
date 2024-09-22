task = input("Enter your task: ")
priority = input("priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
   case "high":
         if time_bound == "yes":
              print(f"Reminder: '{task}' is a high priority task. this task requires immediate attention today!")
         else :
              print(f"Note: '{task}' is a high priority task. consider completing it when you have a free tine.")
   case "mediun":
         if time_bound=="yes":
              print(f"Reminder: '{task}' is a high priority task. This task requires immediate attention today!")
         else :
              print(f"Note: '{task}' is a high priority task. consider completing it when you haave free time.")
  case "low":
         if time_bound== "yes":
              print(f"Reminder: '{task}' is a high priority task. This task requires immediate attention today!")
         elsen:
              print(f"Note: '{task}' is high priority task. Consider completing it when you have free time.")
   case _:
        print(f"Remider:'{task}' priority is not recpgnized, but is still needs tobbe completed.")
