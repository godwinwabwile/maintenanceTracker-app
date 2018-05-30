import unittest
import json
from app import app
from flask import Flask, request, jsonify

#start of tests
class UserTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app= app.test_client()
        self.case_user = {
            "name": "Godwin Wabwile",
            "email": "wegowabz1@gmail.com",
            "password": "password",
        }
    #correct credentials
    def test_signup(self):
        response = self.app.post('/signup/', data=json.dumps(self.case_user), content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["name"], "Godwin Wabwile")
        self.assertEqual(result["email"], "wegowabz1@gmail.com")
        self.assertEqual(result["password"], "password")
        #status code
        self.assertEqual(response.status_code, 201)

    #all fields should be filled
    def test_signup_fields(self):
        #name field
        self.case_user['name'] = ""
        self.case_user['email'] = "wegowabz1@gmail.com"
        self.case_user['password'] = "password"
        response = self.app.post('/signup/', data=json.dumps(self.case_user),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Please fill the name field then try again!")
        self.assertEqual(response.status_code, 400)  

        #email field
        self.case_user['name'] = "Godwin Wabwile"
        self.case_user['email'] = " "
        self.case_user['password'] = "password"
        response2 = self.app.post('/signup/', data=json.dumps(self.case_user),content_type="application/json")
        result2 = json.loads(response2.data)
        self.assertEqual(result2["message"], "Please fill the email field then try again!")
        self.assertEqual(response2.status_code, 400) 

        
        #password field
        self.case_user['name'] = "Godwin Wabwile"
        self.case_user['email'] = "wegowabz1@gmail.com"
        self.case_user['password'] = " "
        response3 = self.app.post('/signup/', data=json.dumps(self.case_user),content_type="application/json")
        result3 = json.loads(response3.data)
        self.assertEqual(result3["message"], "Please fill the password field then try again!")
        #status code
        self.assertEqual(response3.status_code, 400)  

          
    #email validation
    def test_valid_email(self):
        self.case_user['email'] = "godwin.wabz"
        response = self.app.post('/signup/', data=json.dumps(self.case_user),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "email must have thi @ sign")
        #status code
        self.assertEqual(response.status_code, 400)

        self.case_user['email'] = "1wegowabz@gmail.com"
        response = self.app.post('/signup/', data=json.dumps(self.case_user),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "cant start with a digit")
        #status code
        self.assertEqual(response.status_code, 400)  
      
    #test valid name
    def test_valid_name(self):
        self.case_user['name'] = "23Godwin $Wabwile"
        response = self.app.post('/signup/', data=json.dumps(self.case_user),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "names must start with alphabets")
        self.assertEqual(response.status_code, 400)  
    
    #password length
    def test_password_strength(self):    
        self.case_user['password'] = "wabz"
        response = self.app.post('/signup/', data=json.dumps(self.case_user),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "password must have atleast 8 characters")

        self.assertEqual(response.status_code, 400) 
    # end tests for api user signup
    
    #tests for user sign in
    ef test_signin_fields(self):
        #email field
        self.case_user['email'] = ""
        response = self.app.post('/signin', data=json.dumps(self.case_user),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "email field required")
        self.assertEqual(response.status_code, 400) 

        #password
        self.case_user['email'] = "wegowabz1@gmail.com"
        self.case_user['password'] = ""
        response1 = self.app.post('/signin', data=json.dumps(self.case_user),content_type="application/json")
        result1 = json.loads(response1.data)
        self.assertEqual(result1["message"], "enter password and try again buddy")
        self.assertEqual(response1.status_code, 400)        

    def test_signin_invalid_email(self):
        self.case_user['email'] = "godwin."
        response = self.app.post('/signin', data=json.dumps(self.case_user),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"], "Invalid email address!")
        self.assertEqual(response.status_code, 400)
if __name__ == "__main__":
    unittest.main()