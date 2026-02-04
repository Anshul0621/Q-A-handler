import json

DATA_FILE = "data.json"


def load_data():
    try:
        with open(DATA_FILE,'r') as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return []
def add_qa():
        while True:   
          question = input('Enter the Question here: ')
          answer = input('Enter the Answer here: ')
          category = input("Enter your Category: ")
          if question.strip() =='' or answer.strip() == '' or category.strip()=='':
              print("Add valid Inputs only.")
          else:
              break
        a = load_data()
        with open(DATA_FILE,'w') as f:
            newdict = {"question":question,"answer":answer,'category':category}
            a.append(newdict)
            json.dump(a,f,indent=2)
            print("Q&A added successfully")
def readall():
          data = load_data()
          for i in data:
               print(f'Q: {i["question"]}')
               print(f'A: {i["answer"]}')
               print('-------------------')
def view_by_category():
     cate = input("Enter the category here: ").lower()
     data = load_data()
     flag=False
     for i in data:
          if i.get('category','').lower() == cate:
               flag=True
               print(f'Q: {i["question"]}')
               print(f'A: {i["answer"]}')
               print('-------------------')
     if flag==False:
          print("Category not found.")
def update_qa():
     ques = input('Enter which question you want to update: ')
     newdata=[]
     data = load_data()
     flag = False
     for i in data:
          if i['question'].lower() == ques.lower():
               newans = input("Enter your answer here: ")
               i['answer'] = newans
               newdata.append(i)
               print("Answer updated successfully")
               flag = True
          else:
               newdata.append(i)
     if flag == False:
          print("Question not Found.")
     with open(DATA_FILE,'w') as f:
          json.dump(newdata,f,indent=2)
def delete_qa():
    ques = input("Enter question you want to delete: ")
    newdata = []
    data = load_data()
    quesflag= True
    for i in data:
     if i['question'].lower() == ques.lower():
          quesflag=False
          continue
     else:
          newdata.append(i)
    if quesflag==True:
          print("Question not found.")
    if quesflag == False:
         print("Question deleted successfully")  
    with open(DATA_FILE,'w') as f:
          json.dump(newdata,f,indent=2)  
def search_qa():
    searchques = input("Search ques here: ")
    data = load_data()
    flag = False
    for i in data:
        if  searchques.lower() in i['question'].lower() :
          print(f"Q. {i['question']}\nAns. {i['answer']}")
          flag = True
    if flag==False:
          print("Question not found.")
def menu():
     print("========================")
     print("Admin Q&A System")
     print("========================")
     print("1. Add Q&A")
     print("2. View All Q&A")
     print("3. View by Category")
     print("4. Update Q&A")
     print("5. Delete Q&A")
     print("6. Search Q&A")
     print("7. Exit")
     print("========================")
     while True:
          try:
               a = int(input('Enter your input: '))
               print('------------------------')
               if a == 1:
                    add_qa()
               elif a == 2:
                    readall()
               elif a == 3:
                    view_by_category()
               elif a == 4:
                    update_qa()
               elif a == 5:
                    delete_qa()
               elif a == 6:
                    search_qa()
               elif a == 7:
                    break
               else:
                    print("Not a valid input")
          except ValueError:
               print("Value should be number only")
menu()





