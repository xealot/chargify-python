A [Chargify API](http://support.chargify.com/faqs/api/api-user-guide) client written in Python.

Basic Usage
-----------
See the test cases for a full list of examples for all supported API calls.

	chargify = Chargify('api_key','subdomain')

	# List products
    result = chargify.products()
    
	# List customers
	result = chargify.customers()

	# List a specific customer
	result = chargify.customers(customer_id=123)

	# Create a customer
	result = chargify.customers.create(data={
        'customer':{
            'first_name':'Joe',
            'last_name':'Blow',
            'email':'joe@example.com'
        }
    })
    
    # Update a customer
    result = chargify.customers.update(customer_id=123,data={
        'customer':{
            'email':'joe@example.com'
        }
    })
    
    # Create a subscription
    result = chargify.subscriptions.create(data={
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
    
    # Cancel a subscription
    result = chargify.subscriptions.delete(subscription_id=123,data={
        'subscription':{
            'cancellation_message':'Goodbye!'
        }
    })
    
    # Migrate a subscription
    result = chargify.subscriptions.migrations.create(subscription_id=123,data={
        'product_id':1234
    })
    
    # Add a one time charge to a subscription
    result = chargify.subscriptions.charges.create(subscription_id=123,data={
        'charge':{
            'amount':'1.00',
            'memo':'This is the description of the one time charge.'
        }
    })
    
    # List transactions for a subscription
    result = chargify.subscriptions.transactions(subscription_id=123)