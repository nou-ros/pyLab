
from .test_setup import TestSetUp

from authentication.models import User

class TestViews(TestSetUp):

    def test_user_cannot_register_without_data(self):
        # self.client is a APIClient attribute
        res = self.client.post(self.register_url)

        # pdb is a python debugger, pause the execution of program to see the inner variables
        # import pdb
        # pdb.set_trace() # to check use -> res  in shell for more user -> res.data

        self.assertEqual(res.status_code, 400) # we can use 200 code to check pdb trace

    def test_user_can_signup_correctly(self):
        res = self.client.post(self.register_url, self.user_data, format="json")
        
        # import pdb
        # pdb.set_trace()

        self.assertEqual(res.data['email'], self.user_data['email'])
        self.assertEqual(res.status_code, 201)
    
    def test_user_cannot_login_with_unverified_email(self):
        self.client.post(self.register_url, self.user_data, format="json")

        res = self.client.post(self.login_url, self.user_data, format="json")

        # import pdb
        # pdb.set_trace()

        self.assertEqual(res.status_code, 401)
    
    def test_user_can_login_after_verification(self):
        resp = self.client.post(self.register_url, self.user_data, format="json")

        email = resp.data['email']

        # verifying manually
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()

        res = self.client.post(self.login_url, self.user_data, format="json")

        # import pdb
        # pdb.set_trace()

        # self.assertEqual(res.status_code, 401)
        # after manual verification
        self.assertEqual(res.status_code, 200)