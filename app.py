from flask import Flask,render_template,request
from dotenv import load_dotenv
import csv
import os

load_dotenv()

# MONGO_URI = os.getenv("MONGO_URI")
# app.config["MONGO_URI"] = "mongodb://localhost:27017/users"
# app.config["MONGO_URI"]=MONGO_URI
# client = pymongo.MongoClient(MONGO_URI)
# db = client.valo

'''
{
TeamName:{member1:}
}
TeamName, MemberName, Number, Email, Phone
TeamName, MemberName, Number, Email, Phone 
TeamName, MemberName, Number, Email, Phone 

TeamName, No of members, 1st Name, 1st number, 1st email, 2nd name, 2nd number, 2nd email, 3rd Name, 3rd Number, 3 email, 4th Name, 4th Number, 4th email.
'''

app = Flask(__name__)

def check_if_email_exists(email_id:str) -> bool:
    with open('registrations.csv','r') as csv_file_obj:
        csv_reader = csv.reader(csv_file_obj, delimiter=',')
        line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        else:
            if email_id == row[4] or email_id == row[7] or email_id == row[10] or email_id == row[13]:
                return False
    return True


def check_if_exists_in_directory(file_or_folder_name:str,directory:str='') -> bool:
    current_working_dir =  os.getcwd()
    try:
        if directory:
            os.chdir(directory)
        return file_or_folder_name in os.listdir()
    except FileNotFoundError:
        return False
    finally:
        os.chdir(current_working_dir)


def write_to_csv(data: dict):
    # TeamName, No of members, 1st Name, 1st number, 1st email, 2nd name, 2nd number, 2nd email, 3rd Name, 3rd Number, 3 email, 4th Name, 4th Number, 4th email.    
    header = ['TeamName', 'NoOfMembers', 'TeamLeadName', 'TeamLeadPhoneNumber', 'TeamLeadEmail', 'TransactionID1', '2ndMemberName', '2ndMemberPhone', '2ndMemberEmail', 'TransactionID2', '3rdMemberName', '3rdMemberNumber', '3rdMemberEmail', 'TransactionID3', '4thMemberName', '4thMemberNumber', '4thMemberEmail', 'TransactionID4']
    
    row = [data['TeamName'], data['NoOfMembers'], data['TeamLeadName'], data['TeamLeadPhoneNumber'], data['TeamLeadEmail'], data['TransactionID1'], data['2ndMemberName'], data['2ndMemberPhone'], data['2ndMemberEmail'], data['TransactionID2'], data['3rdMemberName'], data['3rdMemberNumber'], data['3rdMemberEmail'], data['TransactionID3'], data['4thMemberName'], data['4thMemberNumber'], data['4thMemberEmail'], data['TransactionID4']]
    with open('registrations.csv','a') as csv_file_obj:
        csv_write = csv.writer(csv_file_obj, delimiter=',',lineterminator='\n')
        if check_if_exists_in_directory('registrations.csv'):
            csv_write.writerow(row)
            print("came to if")
        else:
            print("came to else")
            with open('registrations.csv','x'):
                pass
            csv_write.writerow(header)
            write_to_csv(data)


@app.route("/", methods=["POST","GET"])
def data():
    message = ""
    phone_no = ""
    data = {}
    if request.method == "POST":
        data['TeamName'] = request.form['TeamName']
        data["NoOfMembers"] = request.form["NoOfMembers"]
        data['TeamLeadName'] = request.form['TeamLeadName']
        data["TeamLeadPhoneNumber"] = request.form["TeamLeadPhoneNumber"]
        data["TeamLeadEmail"] = request.form["TeamLeadEmail"]
        data["TranscationID1"] = request.form["TranscationID1"]

        data["2ndMemberName"] = request.form["2ndMemberName"]
        data["2ndMemberPhoneNumber"] = request.form["2ndMemberPhoneNumber"]
        data["2ndMemberEmail"] = request.form["2ndMemberEmail"]
        data["TransactionID2"] = request.form["TransactionID2"]

        data["3rdMemberName"] = request.form["3rdMemberName"]
        data["3rdMemberPhoneNumber"] = request.form["3rdMemberPhoneNumber"]
        data["3rdMemberEmail"] = request.form["3rdMemberEmail"]
        data["TransactionID3"] = request.form["TransactionID3"]

        data["4thMemberName"] = request.form["4thMemberName"]
        data["4thMemberPhoneNumber"] = request.form["4thMemberPhoneNumber"]
        data["4thMemberEmail"] = request.form["4thMemberEmail"]
        data["TransactionID4"] = request.form["TransactionID4"]
        
        emails = (data["TeamLeadEmail"], data["2ndMemberEmail"], data["3rdMemberEmail"], data["4thMemberEmail"])
        numbers = (data["TeamLeadPhoneNumber"], data["2ndMemberPhone"], data["3rdMemberPhoneNumber"], data["4thMemberPhoneNumber"])
        
        for email in emails:
            if email:
                if check_if_email_exists(email):
                    message = "One of your Email IDs is already registered for this event"
                    return render_template("index.html", message=message)
                    #  return jsonify({"error":"Email address already in use"}),400
        
        for number in numbers:
            if number:
                if len(number) != 10:
                    print(len(data["Contact_no_team_lead"]))
                    phone_no = "Please enter a valid Indian phone number (10 Digits)"
                    return render_template("index.html", phone_no=phone_no)
        
        # Pattern = re.compile("^.{3,32}#[0-9]{4}$")
        write_to_csv(data)
    
    return render_template("index.html")

@app.route("/data2",methods=["POST","GET"])
def data2():
    return render_template("data2.html")

if __name__ == "__main__":
    app.run()