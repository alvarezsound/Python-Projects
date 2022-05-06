# Python Projects
This is the repository for all of my Python course projects! Click the links below to view the files.
## Projects:
- <a href="https://github.com/alvarezsound/Python-Projects/tree/main/Phonebook" target="_blank">Phonebook</a>
- <a href="https://github.com/alvarezsound/Python-Projects/tree/main/Check_Files_GUI" target="_blank">Check Files GUI</a>
- <a href="https://github.com/alvarezsound/Python-Projects/tree/main/Nice_or_mean_game" target="_blank">Nice or Mean Game</a>
- <a href="https://github.com/alvarezsound/Python-Projects/tree/main/Student_Tracker" target="_blank">Student Tracker</a>
- <a href="https://github.com/alvarezsound/Python-Projects/tree/main/Django_Checkbook" target="_blank">Checkbook (Django)</a>
- <a href="https://github.com/alvarezsound/Python-Projects/tree/main/Python_Assignments" target="_blank">Python Assignments</a>
- <a href="https://github.com/alvarezsound/Python-Projects/tree/main/Python_Challenges" target="_blank">Python Challenges</a>
## Phonebook
This project functions as a phone book for a user. It saves a contact's name, phone number, and email address in a database and allows the user to update and delete previously stored entries.
![Phonebook](/Images/Phonebook.png)
## Check Files GUI
This project allows the user to transfer all files from one chosen directory to another that have been modified within 24 hours. All files that are moved will be saved in a database.
![Check Files GUI](/Images/Check_Files_GUI.png)
## Nice or Mean Game
Simple game that utilizes python functions. Player enters their name and then is prompted with a scenario for which they need to choose to be nice or mean. Nice or mean choices are scored and player wins when reaching the score of 3 "Nice" and loses when reaching a score of 3 "Mean".
## Student Tracker
Student information tracker that utilizes python, sqlite3, and tkinter. Fully functioning GUI that allows you to insert a students information and submit into a database. You can also update and delete existing information.
![Student Tracker](/Images/Student_Tracker.png)
## Checkbook (Django)
Checkbook/banking website created using Django. Users can create an account(s) and view/add transactions. Finally, the transactions are stored in a database.

Code highlights:
views.py
```cs
def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account']
        return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)

def create_account(request):
    form = AccountForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    content = {'form': form}
    return render(request, 'checkbook/CreateNewAccount.html', content)

def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)
    transactions = Transaction.Transaction.filter(account = pk)
    current_total = account.initial_deposit
    table_contents = { }
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            pk = request.POST['account']
            form.save()
            return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
```
## Python Assignments
Various assignments and exercises used to build familiarity with python.
## Python Challenges
Various challenges where I was given a prompt of a small program to create, design, and code from scratch using knowledge gained in the course and further research.
