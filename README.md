This proof of concept project demonstrates how to upload files in Django using model forms and the Django template language. The project includes the following files:

    models.py: Defines the model for the uploaded file, including the name, file, and date uploaded.
    forms.py: Defines the form used to upload files, including the file field and any additional fields for the model.
    views.py: Defines the views used to handle the file upload process, including the form view for displaying the form and the success view for displaying the success message.
    upload.html: The HTML template used to display the file upload form.
    success.html: The HTML template used to display the success message after a file is uploaded.

Libraries used:

    Django: The web framework used to build the project.
    Django template language: The template language used to create the HTML templates.
    Bootstrap 5: The CSS framework used to style the HTML templates.

Requirements installation: To run the project, make sure you have the following libraries installed:

    Django (version 3.2.4)
    Bootstrap 5 (version 5.0.2)
To install these libraries using Conda, use the following command:
```
conda env create -f environment.yml
```
This will create a new Conda environment with the required libraries installed. To activate the environment, use the following 
```
conda activate poc-django-upload-files
```
To run the project, navigate to the project directory and run the following command:
```
python django_upload_files/manage.py runserver
```

Access the file upload form at the specified URL, upload a file using the form and view the success message. Note: It is recommended to review the Django documentation for a more detailed understanding of the project components and the Django framework in general. Targets:

- Demonstrate how to upload files in Django using model forms and the Django template language.
- Use Bootstrap 5 to style the HTML templates.
- Create a Conda environment with the required libraries installed.
- Provide instructions for activating and deactivating the environment.
- Provide instructions for running the project.
