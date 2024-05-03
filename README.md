# Anime Movies Website

![Website Screenshot](animi_site.png)

## Description
This is a Django-based website for streaming and viewing information about anime movies. It provides a platform for users to browse through a collection of anime movies, view details about each movie, and watch them online.

## Features
- Browse a collection of anime movies.
- View detailed information about each movie.
- Watch movies online.
- User authentication and registration system.
- Add, edit, and delete movies (admin functionality).

## Technologies Used
- Django
- HTML/CSS
- JavaScript
- SQLite (for development)
- Bootstrap (for styling)


## Setup
1. **Clone the repository:**
git clone https://github.com/CodeWithRanjHa/Animi-Website-With-Django.git



2. **Navigate to the project directory:**
cd anime-movies-website


3. **Install dependencies:**
pip install -r requirements.txt


4. **Run migrations:**

python manage.py migrate


5. **Create a superuser (admin user):**
python manage.py createsuperuse


6. **Start the development server:**
python manage.py runserver


7. **Open your web browser and navigate to [http://localhost:8000](http://localhost:8000)**

## Usage
- **User Authentication:** Users can sign up for an account and log in to access additional features such as adding movies to favorites.
- **Browsing Movies:** Browse through the collection of anime movies, view details, and watch online.
- **Admin Panel:** Access the admin panel at [http://localhost:8000/admin](http://localhost:8000/admin) to manage movies, users, etc.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Create a new Pull Request


