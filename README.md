# Netflix Clone Using Django

This is a Netflix clone project built using Django for user authentication and other functionalities following the MVC (Model-View-Controller) architectural pattern. The project aims to replicate the aesthetics and functionality of the original Netflix platform while utilizing Tailwind CSS to achieve a visually authentic design. However, it is important to note that this clone is static and only contains movies and videos available in the database.

## Setting Up the Project From Scratch

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/your-username/netflix-clone.git
   
2. **Navigate to the Project Directory:**
    ```sh
    cd netflix-clone
  
3. **Install Dependencies:**
    ```sh
    pip install django
    pip install django-allauth

4. **Create and Apply Database Migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate

5. **Run the Development Server:**
    ```sh
    python manage.py runserver

6. **Access the Project:**
Open a web browser and navigate to http://127.0.0.1:8000/ to access the Netflix clone project.

Note:

- Ensure that you have Python and pip installed on your system.
- Customize the project settings in settings.py as per your requirements, such as database configuration and static files settings.
- In near future I plan to extend the functionality of the project by adding features like dynamic content generation, and integration with external APIs for fetching real-time movie data.

