# CRM Project - Django + DRF

## 📌 Overview
A Customer Relationship Management (CRM) system built using **Django** and **Django REST Framework (DRF)**.  
It supports core CRM functionalities such as **Lead Management**, **Contact Management**, **Tickets**, **Campaigns**, **Notes**, and **Attachments**, along with **secure JWT-based authentication**.

This project includes advanced features like asynchronous task processing with **Celery + Redis**, caching with Redis for API optimization, real-time notifications via **Django Channels (WebSockets)**, API tracking/logging, and robust **Role-Based Access Control (RBAC)**.

---

## 🚀 Features

### 🔹 Core CRM Modules
- **Leads Management** – Create, read, update, and delete leads.
- **Contacts Management** – Manage customer contact details.
- **Tickets System** – Create support tickets with file attachments.
- **Campaigns** – Manage marketing campaigns.
- **Notes & Attachments** – Add notes and upload files to tickets.

### 🔹 User Management & Access Control
- **Custom User Model** – Authentication via email instead of username.
- **Role-Based Access Control (RBAC)** – Roles like `Admin`, `Manager`, `Agent` with specific permissions.
- **Teams Management** – Assign users to teams dynamically.
- **Authentication & Authorization** – Secure login, logout, and protected routes with JWT tokens.

### 🔹 API Endpoints & Optimizations
- **Django REST Framework APIs** for Leads, Tickets, Campaigns, Contacts, Teams, Notes, and Attachments.
- **Filtering, Searching, and Ordering** for data retrieval.
- **Caching with Redis** for leads and other heavy-read APIs with TTL and cache invalidation.
- **API Tracking & Logging** – Logs all API requests and background task executions.
- **Pagination** support for large datasets.
- **File Uploads** – Upload notes and attachments in tickets.

### 🔹 Async & Scheduled Tasks (Celery + Redis)
- Async email sending on new lead creation.
- Scheduled daily reminders for leads not contacted in last 3 days.
- Logs and monitoring of background task execution.

### 🔹 Real-Time Notifications (WebSockets)
- Real-time notifications via Django Channels and Redis.
- WebSocket endpoint `/ws/notifications/`.
- Notifications for new leads and task completions.
- Secure, token-authenticated WebSocket connections.

### 🔹 Security & Performance
- **JWT Authentication** with token blacklist on logout.
- **CORS** configured for frontend origins.
- **API Throttling / Rate Limiting** to protect from abuse.
- Role-based endpoint permissions.
- Secure WebSocket authentication.

---

## 🛠 Tech Stack
- **Backend Framework:** Django, Django REST Framework  
- **Async Task Queue:** Celery with Redis broker  
- **Caching:** Redis  
- **Real-Time:** Django Channels + Redis  
- **Database:** PostgreSQL / SQLite (configurable)  
- **Authentication:** JWT (`djangorestframework-simplejwt`)  
- **File Handling:** Django File Storage  
- **Permissions:** DRF Permissions + Django Groups  

---


## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/crm-project.git
cd crm-project
```

### 2️⃣ Create Virtual Environment & Install Dependencies
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
 
env\Scripts\activate# OR on Windows
pip install -r requirements.txt
```


### 3️⃣ Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Create Superuser
```bash
python manage.py createsuperuser
```

### 5️⃣ Run the Development Server
```bash
python manage.py runserver
```

### 🔑 API Authentication
All protected API endpoints require a valid JWT Access Token in the request header:
```bash
Authorization: Bearer <access_token>
```


## 📡 API Endpoints

### 🔹 Authentication
| Method | Endpoint                                      | Description                                  |
|--------|-----------------------------------------------|----------------------------------------------|
| POST   | `/api/token/`                                 | Obtain access and refresh JWT tokens.        |
| POST   | `/api/token/refresh/`                         | Refresh the access token using refresh token.|
| POST   | `/api/users/logout/`                          | Logout and blacklist the refresh token.      |
| POST   | `/api/users/register/`                        | Register a new user account.                   |
| POST   | `/api/users/forgot-password/`                 | Request password reset email.                  |
| POST   | `/api/users/reset-password/<uidb64>/<token>/` | Reset password using token link.               |
| GET    | `/api/users/profile/`                         | Retrieve authenticated user's profile.        |
| PUT    | `/api/users/profile/update/`                  | Update authenticated user's profile.          |

---

### 🔹 Users
| Method | Endpoint                      | Description                          |
|--------|-------------------------------|------------------------------------|
| GET    | `/api/users/list/`            | List all users.                     |
| GET    | `/api/users/<int:pk>/`        | Retrieve, update, or delete a user.|
| GET    | `/api/users/count/`           | Get total number of users.          |
| GET    | `/api/users/extended/`        | Get extended user details.          |
| GET    | `/api/users/users-with-leads/` | List users with their assigned leads.|

---

### 🔹 Leads
| Method       | Endpoint                               | Description                         |
|--------------|--------------------------------------|-----------------------------------|
| GET / POST   | `/api/leads/`                        | List or create leads.              |
| GET / PUT / DELETE | `/api/leads/<int:pk>/`         | Retrieve, update, or delete a lead.|
| GET          | `/api/leads/count/`                  | Get total number of leads.         |
| GET          | `/api/leads/dropdown/`               | Get leads for dropdown selection.  |
| GET          | `/api/leads/extended/`               | Get extended lead details.         |
| GET          | `/api/contacts/leads-with-contacts/`| List leads with associated contacts.|

---

### 🔹 Contacts
| Method | Endpoint               | Description            |
|--------|------------------------|------------------------|
| POST   | `/api/contacts/`       | Create a new contact.   |
| GET    | `/api/contacts/<int:pk>/` | Retrieve a specific contact.|

---

### 🔹 Tickets
| Method       | Endpoint                         | Description                         |
|--------------|----------------------------------|-----------------------------------|
| GET / POST   | `/api/leads/tickets/`            | List or create tickets.            |
| GET / PUT / DELETE | `/api/leads/tickets/<int:pk>/` | Retrieve, update, or delete a ticket.|

---

### 🔹 Notes
| Method       | Endpoint                         | Description                         |
|--------------|----------------------------------|-----------------------------------|
| GET / POST   | `/api/leads/notes/`              | List or create notes for tickets.  |
| GET / PUT / DELETE | `/api/leads/notes/<int:pk>/`  | Retrieve, update, or delete a note.|

---

### 🔹 Attachments
| Method       | Endpoint                             | Description                         |
|--------------|------------------------------------|-----------------------------------|
| GET / POST   | `/api/leads/attachment/`            | List or upload attachments for tickets.|
| GET / PUT / DELETE | `/api/leads/attachment/<int:pk>/` | Retrieve, update, or delete an attachment.|

---

### 🔹 Campaigns
| Method       | Endpoint                             | Description                         |
|--------------|------------------------------------|-----------------------------------|
| GET / POST   | `/api/leads/campaigns/`            | List or create campaigns.           |
| GET / PUT / DELETE | `/api/leads/campaigns/<int:pk>/` | Retrieve, update, or delete a campaign.|

---

### 🔹 Teams
| Method       | Endpoint                             | Description                         |
|--------------|------------------------------------|-----------------------------------|
| GET / POST   | `/api/teams/`                      | List or create teams.              |
| GET / PUT / DELETE | `/api/teams/<int:pk>/`           | Retrieve, update, or delete a team.|
| POST         | `/api/teams/<int:team_id>/assign-users/` | Assign users to a team.       |
| POST         | `/api/teams/<int:team_id>/remove-users/` | Remove users from a team.     |
| GET          | `/api/teams/count/`                 | Get total number of teams.         |
| GET          | `/api/teams/with-users/`            | List teams with their users.       |

---

### 🔹 Miscellaneous
| Method | Endpoint                        | Description           |
|--------|--------------------------------|-----------------------|
| GET    | `/api/users/send-test-email/`  | Send a test email.    |






