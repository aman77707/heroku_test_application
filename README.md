# OnlineKart E-commerce

## Motivation:
  Motivattion for the project came from the idea of creating a basic and sample proof of concept for the      
  online shopping platform. Though the project has missing front-end and is under the scope of enormous     
  improvement it has definitely achored me at a position from where I can take this project from a sample   
  POC to a completely built working website as an e-commerce platform.  

## Dependencies and hosting instructions:
### Carry out the following steps:
  * Once, the repository has been cloned in a local environment, navigate to the repository root which contains  
    requirements.txt file and execute:  
    ```
    pip install -r requirements.txt
    ```  
  * After installing the dependencies, set flask variable FLASK_APP. To do this execute the below command:  
    ```
    export FLASK_APP=app.py
    ```
  * Set the environment variables by running the command:  
    ```
    source setup.sh
    ```
  * To run the server, run:  
    ```
    flask run --reload
    ```

  Post starting the server, we are in position to start sending requests to the end points hosted on the URL.

## Types of users in the system:
  * Admin:  
    This user has all the necessary permissions for the database tables. It is allowed to carry out the following  
    operations:  
      * Get categories
      * Post categories
      * Delete categories
      * Patch categories
      * Get Products
      * Post Products
      * Patch Products
      * Delete Products
      * Get Customers
      * Post Customers
      * Delete Customers
      * Get Transactions

  * Customer:
    This user has permissions to get the products, categories and carry out transactions to purchase the products:  
      * Get categories
      * Get Products
      * Post Transactions

  * Guest:
    This user can just view the products and categories:  
      * Get categories
      * Get Products

## API Endpoints:  
  * GET: http://127.0.0.1:5000/categories  
    This endpoint is used to get a list of all the categories of products available in the store. An example of response looks like:  
    ```
    {  
          "categories": [  
          {  
            "id": 4,   
            "name": "electronic"  
          },   
          {  
            "id": 5,   
            "name": "groceries"  
          }  
        ],  
        "success" : True  
    }
    ```
  * POST: http://127.0.0.1:5000/categories  
    This input takes a json of the category to be created as input, an example of such a category looks like:  
    ```
    {
      "name" : "electronics"
    }
    ```
    The response from such POST request would look like:  
    ```
    {
      "category_name": "electronics", 
      "message": "Successfully Inserted in the database", 
      "success": true
    }
    ``` 
  * PATCH: http://127.0.0.1:5000/categories/<category_id>  
    This input takes a json of the category to be created as input, an example of such a category looks like:  
    ```
    {
      "name" : "electricals"
    }
    ```
    The response from such PATCH request would look like:  
    ```
    {
      "category_name": "electricals", 
      "message": "Successfully Updated in the database", 
      "success": true
    }
    ``` 
  * DELETE: http://127.0.0.1:5000/categories/<category_id>  
    This end point deletes the mentioned category ID from the system. An example of response looks like:  
    ```
    {
      "id": 9, 
      "message": "Deleted Successfully"
    }
    ```
  * GET: http://127.0.0.1:5000/products  
    This endpoint is used to get a list all the products of a specific category available in the store. An example of response looks like:  
    ```
    {  
      "products": [
        {
          "availability_status": true, 
          "category_id": 4, 
          "description": "Grooming appliance for men", 
          "id": 3, 
          "name": "Trimmer", 
          "price": 1120
        }
      ],  
      "success" : True  
    }
    ```
  * POST: http://127.0.0.1:5000/products  
    This endpoint is used to add a new product in the store database. This API takes an input as a JSON object for the product to be entered:  
    ```
    {
      "name" : "trimmer", 
      "category" : 1 , 
      "price" : 1120, 
      "description": "Grooming appliance" , 
      "availability_status" : true
    }
    ```
    Response for such request looks like:
    ```
    {
      "availability_status": true, 
      "category_id": 4, 
      "description": "Grooming appliance", 
      "name": "trimmer", 
      "price": 1120, 
      "success": true
    }
    ```
  * PATCH: http://127.0.0.1:5000/products/<product_id>  
    This endpoint is used to update the details of a product in the store database. This API takes an input as a JSON object for the product to be entered:   
    ```
    {
      "name" : "trimmer", 
      "category" : 1 , 
      "price" : 1120, 
      "description": "Grooming appliance" , 
      "availability_status" : false
    }
    ```
    Response for such request looks like:
    ```
    {
      "availability_status": false, 
      "category_id": 4, 
      "description": "Grooming appliance", 
      "name": "trimmer", 
      "price": 1120, 
      "success": true
    }
    ```
  * DELETE: http://127.0.0.1:5000/products/<product_id>  
    This end point is used to delete the mentioned product by the product_id in the databse. It does not take any http request body. A response for such a  
    request looks like:  
    ```
    {
      "id": 11, 
      "message": "Deleted Successfully"
    }
    ```
  * GET: http://127.0.0.1:5000/users  
    This api end point is used to get all the registered users to the platform. A response to a request made to the api looks like:  
    ```
    {
      "success": true, 
      "users": [
        {
          "id": 4, 
          "name": "Hermione Granger"
        }, 
        {
          "id": 5, 
          "name": "Ron Weasley"
        }, 
        {
          "id": 6, 
          "name": "Harry Potter"
        }
      ]
    }
    ```
  * POST: http://127.0.0.1:5000/users  
    This endpoint takes a JSON object of the new user about to get registered and adds the user to the database:  
    ```
    {
      "name" : "Aman Bhardwaj"
    }
    ```
    Response would look like after a successful registration:  
    ```
    {
      "message": "Successfully Inserted in the database", 
      "success": true, 
      "user_name": "Hermione Granger"
    }
    ```
  * DELETE: http://127.0.0.1:5000/users/<user_id>  
    This end point is used to remove a user from the database. A response from such a request looks like:  
    ```
    {
      "id": 5, 
      "message": "Deleted Successfully"
    }
    ```
  * POST: http://127.0.0.1:5000/purchase  
    This end point allows user to make a purchase of a product. Takes a JSON body which couples user_id and product_id:  
    ```
    {
      "user_id" : 4,
      "product_id" : 3
    }
    ```
    Successful response from such a request looks like:  
    ```
    {
      "message": "Thankyou for shopping with us!!", 
      "product_id": 6, 
      "success": true, 
      "user_id": 4
    }
    ```
  * GET: http://127.0.0.1:5000/transactions  
    This endpoint is used to get all the transactions happed against a user. A response when a request made to the api looks like:    
    ```
    {
      "success": true, 
      "userproducts": [
        {
          "product": 3, 
          "user": 6
        }, 
        {
          "product": 3, 
          "user": 4
        }, 
        {
          "product": 6, 
          "user": 6
        }
      ]
    }
    ```