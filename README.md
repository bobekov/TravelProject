<h1>Django Travel Booking App</h1>

<h2>Overview</h2>

The Django Travel Booking Platform is a web application designed to facilitate seamless travel planning. It allows users to manage profiles, book flights and hotels, and share reviews about their experiences. The platform supports the following core models:

- Profile: Manage user-specific data, including contact information and preferences.
- Reservations: Track and manage bookings for flights, hotel rooms.
- Countries: Store information about various countries.
- Destinations: Define specific travel destinations within countries.
- Flights: Manage flight details, such as departure, arrival, and pricing.
- Hotels: List accommodations, including descriptions and amenities.
- Rooms: Detail the available rooms within hotels.
- Reviews: Allow users to share feedback about destinations.
---
<h2>Installation</h2>

**`Clone the repository`**

git clone <repository_url>  
cd <repository_directory>

**`Set up a virtual environment`**

python -m venv venv  
source venv/bin/activate   # For Linux/macOS  
venv\Scripts\activate      # For Windows  

**`Install dependencies`**
  
pip install -r requirements.txt  

**`Apply migrations`**
  
python manage.py migrate

**`Run the development server`**

python manage.py runserver

---
<h2>Public Section</h2>

The public section of the application is accessible to all users, including unauthenticated users. This part of the app includes general information and features that do not require the user to be logged in.
Key features of the public section include:
- **Registration:** Users can create an account using their email address.
- **Login/Logout:** After registration, users can log in to their profiles.  

<img src="https://github.com/user-attachments/assets/766fe629-f20c-43ae-a86d-15af3aaac36b" width="600" />

<h2>Private Section</h2>
The private section of the application is reserved for authenticated users only. Users must log in to access these areas. This section provides more personalized features and allows users to interact with their accounts and manage bookings and profile.Key features of the private section include:  

- **User Profile Management:** Users can view, edit, and delete their profiles, including personal information such as phone numbers, addresses, and profile pictures.  
- **Reservations:** Users can create and manage reservations for flights, hotel rooms.  
- **Logout:** Users can log out from the private section, which will end their session and redirect them to the home page.  
- **Models for:** Countries, Destinations, Flights, Hotels, Rooms, and Reviews  

<img src="https://github.com/user-attachments/assets/0f9ca3bc-b74e-4c41-92c8-d0d4d8d87b90" width="600" />

--
<h2>Usage</h2>
After setting up and running the project locally, you can navigate through the various sections of the application as follows:

1. **Countries and Destinations:** As an authenticated user, you can browse a list of countries and view related destinations.  
2. **Flight and Hotel Booking:** Check available flights and hotel rooms at your selected destination and proceed to make a reservation.  
3. **Reviews:** Share your experience by writing reviews for destinations.  

<h2>License</h2>  

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).




