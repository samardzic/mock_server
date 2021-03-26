### GET ALL USERS 
http://localhost:3000/users 

<br/>

### GET SINGLE USER
http://localhost:3000/users/1

<br/>

### GET ALL COMPANIES
http://localhost:3000/companies

<br/>

### GET SINGLE COMPANY
http://localhost:3000/companies/1

<br/>

### GET ALL USERS OF A COMPANY
http://localhost:3000/companies/1/users

<br/>

### FILTER COMPANIES BY NAME
http://localhost:3000/companies?name=Microsoft
http://localhost:3000/companies?name=Microsoft&name=Apple

<br/>

### PAGINATION & LIMIT
http://localhost:3000/companies?_page=1&_limit=2

<br/>

### SORTING
http://localhost:3000/companies?_sort=name&_order=asc

<br/>

### USERS AGE RANGE
http://localhost:3000/users?age_gte=30
http://localhost:3000/users?age_gte=30&age_lte=40

<br/>

### FULL TEXT SEARCH
http://localhost:3000/users?q=Paul