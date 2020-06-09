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
    export FLASK_APP=api.py
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
    This endpoint is used to get all the categories of products available in the store. An example of response looks like:  
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
    }