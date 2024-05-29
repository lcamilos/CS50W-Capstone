# CS50W Final Project: Tennis Center Registration System

### Overview
The Tennis Center Registration System is a web-based application developed using Python and the Django Framework. Its primary aim is to provide a tennis center with an online platform for managing, storing, and retrieving the list of registered athletes. This application allows center management to register and manage athlete data efficiently. It features a simple and user-friendly interface built with the Bootstrap Framework and CoreUI Admin Template. The system includes various features and functionalities that enhance the end-user experience. Additionally, the application is responsive, adapting seamlessly to different screen sizes, including mobile phones and computers. It enables the storage and management of class lists, sections, shifts, registered athletes, departments, subjects, and coaches. Each component supports CRUD (Create, Read, Update, Delete) operations, with some features accessible on the website and others available only through the Django Admin Panel.

### Distinctiveness and Complexity
The Tennis Center Registration System satisfies the distinctiveness and complexity requirements by implementing a comprehensive solution tailored to the needs of tennis center management. It stands out through its robust feature set, user-friendly interface, and efficient data management capabilities.

- **Distinctiveness**: The project distinguishes itself by offering a specialized solution for tennis centers, catering to the unique requirements of athlete registration and management. While there are generic registration systems available, this project provides specific functionalities tailored to tennis centers, such as athlete class, section, and shift management, alongside coach department and subject management.

- **Complexity**: The complexity of the project lies in its multifaceted approach to managing various aspects of a tennis center. It involves the creation of multiple models, views, and templates to handle athlete registration, coach management, and administrative tasks efficiently. The integration of frontend technologies like Bootstrap and CoreUI enhances the user experience and adds to the complexity of the system. Furthermore, the inclusion of authentication and authorization mechanisms ensures secure access to sensitive information.

### Files
- **views.py**: Handles backend information related to coaches, registered athletes, and center employees.
- **models.py**: Contains various models such as CoachInfo, CoachDepartmentInfo, RegisteredAthleteInfo, RegisteredAthleteClassInfo, RegisteredAthleteSectionInfo, and RegisteredAthleteShiftInfo.
- **JavaScript files**: For frontend functionality.
- **Templates**: The Templates folder contains several subfolders:
  - **Accounts**: Contains login.html.
  - **Base**: Includes base.html, footer.html, header.html, js.html, navbar.html, and sidebar.html.
  - **Pages**: Contains index.html.
  - **Partials**: Includes _alerts.html.
  - **Students**: Holds attendance_count.html, edit_student.html, registration.html, student_details.html, and student_list.html.
  - **Teachers**: Contains create_teacher.html, edit_teacher.html, single_teacher.html, and teacher_list.html.
  - **Home.html**: Represents the homepage of the application.
- **CSS file**: For styling the web application.
- **Other files**: URLs, admin configurations, settings, and static images.

### How To Run The Application
1. Install project dependencies by running `pip install -r requirements.txt`.
2. Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`.
3. Run the development server with `python manage.py runserver`.
4. Access the application in your web browser at `http://localhost:8000`.

### Features
- **Login**: Secure login functionality.
- **Dashboard**: Overview of key metrics and navigation.
- **Registered Athlete Class Management (Admin Panel)**: Register, list, edit, and delete classes.
- **Registered Athlete Section Management (Admin Panel)**: Register, list, edit, and delete sections.
- **Registered Athlete Shift Management (Admin Panel)**: Register, list, edit, and delete shifts.
- **Registered Athlete Management**: Register, list, view details, edit, and delete athletes.
- **Coach Department Management (Admin Panel)**: Register, list, edit, and delete departments.
- **Coach Subject Management (Admin Panel)**: Register, list, edit, and delete subjects.
- **Coach Management**: Register, list, view details, edit, and delete coaches.
- **Logout**: Securely log out of the system.

### Additional Information
The Tennis Center Registration System is designed to streamline athlete registration and management processes for tennis centers. It offers a comprehensive solution with a user-friendly interface and robust backend functionality. The project's documentation and codebase are well-organized, making it easy for developers to understand and extend its features. It adheres to best practices in web development and Django framework conventions.
