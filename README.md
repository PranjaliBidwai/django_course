# Django Setting Environment

A Django project demonstrating database setup and progression from SQLite to MySQL, with dummy data management using Mockaroo.

## Project Overview

This is a Django web application that includes multiple apps for managing e-commerce operations:
- **Playground**: Demo and testing application
- **Store**: Product management and e-commerce functionality
- **Likes**: User preferences and favorite tracking
- **Tags**: Tagging system for content organization

## Database Architecture

### Phase 1: SQLite (Development)
- **Initial Setup**: Uses SQLite as the default database for rapid local development
- **File**: `db.sqlite3`
- **Use Case**: Development, testing, and prototyping

### Phase 2: MySQL (Production)
- **Target Database**: MySQL for scalable production deployment
- **Management Tool**: DataGrip IDE for database administration, queries, and optimization
- **Use Case**: Live environment with concurrent users and larger data volumes

## Dummy Data

### Data Source: Mockaroo
- **Platform**: [Mockaroo Free Database Generator](https://www.mockaroo.com/)
- **Purpose**: Generate realistic dummy data for testing and development
- **Process**: 
  1. Use Mockaroo to generate sample datasets in your preferred format
  2. Export data to CSV or JSON
  3. Use Django management commands or direct imports to populate the database

## Project Structure

```
django-setting-environment/
├── db.sqlite3              # SQLite database (development)
├── manage.py               # Django management script
├── likes/                  # User likes app
├── playground/             # Demo/test app
├── store/                  # E-commerce store app
├── tags/                   # Tagging system app
├── storefront/             # Main project settings
└── resources/              # Additional resources
```

## Getting Started

### Prerequisites
- Python 3.8+
- Django 3.2+
- MySQL Server (for Phase 2)
- DataGrip or MySQL client
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd django-setting-environment
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   # or on macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Database Migration Guide

### From SQLite to MySQL

1. **Prepare MySQL Database**
   - Create a new MySQL database for the project
   - Update `storefront/settings.py` with MySQL credentials:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'your_database_name',
             'USER': 'your_mysql_user',
             'PASSWORD': 'your_password',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

2. **Export Data from SQLite**
   ```bash
   python manage.py dumpdata > backup.json
   ```

3. **Load Data into MySQL**
   ```bash
   python manage.py migrate
   python manage.py loaddata backup.json
   ```

## Working with Dummy Data

### Using Mockaroo

1. Visit [Mockaroo.com](https://www.mockaroo.com/)
2. Define your data schema (column names, types, formats)
3. Generate sample data (CSV, JSON, or SQL format)
4. Import into your database using:
   - Django fixtures
   - Management commands
   - DataGrip import tools
   - Raw SQL inserts

### Example: Loading CSV Data
```bash
python manage.py shell
>>> import csv
>>> from store.models import Product
>>> with open('mockaroo_data.csv') as f:
...     reader = csv.DictReader(f)
...     for row in reader:
...         Product.objects.create(**row)
```

## Tools & Technologies

| Tool | Purpose | Version |
|------|---------|---------|
| Django | Web Framework | 3.2+ |
| SQLite | Development Database | Built-in |
| MySQL | Production Database | 5.7+ |
| DataGrip | Database IDE | Latest |
| Mockaroo | Test Data Generation | Free Plan |

## Admin Panel

Access the Django admin interface at: `http://localhost:8000/admin/`

## Running Tests

```bash
python manage.py test
```

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [DataGrip Documentation](https://www.jetbrains.com/help/datagrip/)
- [Mockaroo Documentation](https://www.mockaroo.com/help)

## Contributing

When making changes:
1. Create a new branch
2. Make your changes
3. Test locally with SQLite
4. Verify with MySQL if applicable
5. Commit with clear messages

## License

This project is open source and available under the MIT License.

## Notes

- Keep `db.sqlite3` in version control only for development reference
- Use `.gitignore` to exclude sensitive files (database credentials, `.env` files)
- Always backup data before database migrations
- Test migrations in development environment first

---

**Last Updated**: April 2026
