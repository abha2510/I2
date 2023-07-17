def average_age_of_employees_with_s_job_title(company):
 total_age=0
 count=0

 for employees,details in company['employees'].items():
  if details['job_title'].startswith('S'):
     total_age+=details['age']
     count+=1

     if count>0:
       return total_age/count
     
     else:
       return 0.0




company = {
    'employees': {
        'John': {'age': 35, 'job_title': 'Manager'},
        'Emma': {'age': 28, 'job_title': 'Software Engineer'},
        'Kelly': {'age': 41, 'job_title': 'Senior Developer'},
        'Sam': {'age': 30, 'job_title': 'Software Engineer'},
        'Mark': {'age': 37, 'job_title': 'Senior Manager'},
        'Sara': {'age': 32, 'job_title': 'Software Engineer'},
    }
}
print(average_age_of_employees_with_s_job_title(company))  # 31.0
