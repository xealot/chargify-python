import unittest
from chargify import Chargify, ChargifyError

class ChargifyTestCase(unittest.TestCase):
    
    def assertResult(self, result, expected_url, expected_method, expected_data):
        """
        A little helper method to help verify that the correct URL, HTTP method, and POST data are
        being constructed from the Chargify API.
        """
        url, method, data = result
        print url, method, data
        self.assertEqual(url,expected_url)
        self.assertEqual(method,expected_method)
        self.assertEqual(data,expected_data)
        
class TestCustomers(ChargifyTestCase):
    
    def test_construct_request(self):
        chargify = Chargify('api_key','subdomain')
        
        # List
        result = chargify.customers.construct_request()
        self.assertResult(result,'https://subdomain.chargify.com/customers.json','GET',None)

        # Read/show (via chargify id)
        result = chargify.customers.construct_request(customer_id=123)
        self.assertResult(result,'https://subdomain.chargify.com/customers/123.json','GET',None)
        
        # Read/show (via reference value)
        result = chargify.customers.lookup.construct_request(reference=123)
        self.assertResult(result,'https://subdomain.chargify.com/customers/lookup.json?reference=123','GET',None)
        
        # Create
        result = chargify.customers.create.construct_request(data={
            'customer':{
                'first_name':'Joe',
                'last_name':'Blow',
                'email':'joe@example.com'
            }
        })
        self.assertResult(result,'https://subdomain.chargify.com/customers.json','POST',
            '{"customer": {"first_name": "Joe", "last_name": "Blow", "email": "joe@example.com"}}')
            
        # Edit/update
        result = chargify.customers.update.construct_request(customer_id=123,data={
            'customer':{
                'email':'joe@example.com'
            }
        })
        self.assertResult(result,'https://subdomain.chargify.com/customers/123.json','PUT',
            '{"customer": {"email": "joe@example.com"}}')
        
        # Delete
        result = chargify.customers.delete.construct_request(customer_id=123)
        self.assertResult(result,'https://subdomain.chargify.com/customers/123.json','DELETE',None)

class TestProducts(ChargifyTestCase):
    
    def test_construct_request(self):
        chargify = Chargify('api_key','subdomain')
        
        # List
        result = chargify.products.construct_request()
        self.assertResult(result,'https://subdomain.chargify.com/products.json','GET',None)
        
        # Read/show (via chargify id)
        result = chargify.products.construct_request(product_id=123)
        self.assertResult(result,'https://subdomain.chargify.com/products/123.json','GET',None)
        
        # Read/show (via api handle)
        result = chargify.products.handle.construct_request(handle='myhandle')
        self.assertResult(result,'https://subdomain.chargify.com/products/handle/myhandle.json','GET',None)

class TestSubscriptions(ChargifyTestCase):
    
    def test_construct_request(self):
        chargify = Chargify('api_key','subdomain')
        
        # List
        result = chargify.customers.subscriptions.construct_request(customer_id=123)
        self.assertResult(result,'https://subdomain.chargify.com/customers/123/subscriptions.json','GET',None)
        
        # Read
        result = chargify.subscriptions.construct_request(subscription_id=123)
        self.assertResult(result,'https://subdomain.chargify.com/subscriptions/123.json','GET',None)
        
        # Create
        result = chargify.subscriptions.create.construct_request(data={
            'subscription':{
                'product_handle':'my_product',
                'customer_attributes':{
                    'first_name':'Joe',
                    'last_name':'Blow',
                    'email':'joe@example.com'
                },
                'credit_card_attributes':{
                    'full_number':'1',
                    'expiration_month':'10',
                    'expiration_year':'2020'
                }
            }
        })
        self.assertResult(result,'https://subdomain.chargify.com/subscriptions.json','POST',
            '{"subscription": {"product_handle": "my_product", "credit_card_attributes": {"expiration_month": "10", "full_number": "1", "expiration_year": "2020"}, "customer_attributes": {"first_name": "Joe", "last_name": "Blow", "email": "joe@example.com"}}}')
            
        # Update
        result = chargify.subscriptions.update.construct_request(data={
            'subscription':{
                'credit_card_attributes':{
                    'full_number':'2',
                    'expiration_month':'10',
                    'expiration_year':'2030'
                }
            }
        })
        self.assertResult(result,'https://subdomain.chargify.com/subscriptions.json','PUT',
            '{"subscription": {"credit_card_attributes": {"expiration_month": "10", "full_number": "2", "expiration_year": "2030"}}}')
        
        # Delete
        result = chargify.subscriptions.delete.construct_request(subscription_id=123,data={
            'subscription':{
                'cancellation_message':'Goodbye!'
            }
        })
        self.assertResult(result,'https://subdomain.chargify.com/subscriptions/123.json','DELETE',
            '{"subscription": {"cancellation_message": "Goodbye!"}}')

class TestCharges(ChargifyTestCase):
    
    def test_construct_request(self):
        chargify = Chargify('api_key','subdomain')
        
        # Create
        result = chargify.subscriptions.charges.create.construct_request(subscription_id=123,data={
            'charge':{
                'amount':'1.00',
                'memo':'This is the description of the one time charge.'
            }
        })
        self.assertResult(result,'https://subdomain.chargify.com/subscriptions/123/charges.json','POST',
            '{"charge": {"amount": "1.00", "memo": "This is the description of the one time charge."}}')

class TestComponents(ChargifyTestCase):
    
    def test_construct_request(self):
        chargify = Chargify('api_key','subdomain')
        
        # List
        result = chargify.subscriptions.components.usages.construct_request(subscription_id=123,component_id=456)
        self.assertResult(result,'https://subdomain.chargify.com/subscriptions/123/components/456/usages.json','GET',None)
   
        # Create
        result = chargify.subscriptions.components.usages.create.construct_request(subscription_id=123,component_id=456,data={
            'usage':{
                'quantity':5,
                'memo':'My memo'
            }
        })
        self.assertResult(result,'https://subdomain.chargify.com/subscriptions/123/components/456/usages.json','POST',
            '{"usage": {"memo": "My memo", "quantity": 5}}')
            
if __name__ == "__main__":
    unittest.main()