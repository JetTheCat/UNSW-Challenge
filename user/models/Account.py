from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Models that is an extension of the UserAuth model to keep track of additional
# user information that is not stored in the django default User model.
class Account(models.Model):
    STUDENT = 'STUDENT'
    STAFF = 'STAFF'

    USER_ROLE_CHOICES = (
        (STAFF, 'Staff'),
        (STUDENT, 'Student'),
    )

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default=STUDENT, null=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    
    def __str__(self):
        return f'{self.user.username} Profile'


    # Custom save function to add additional function such as image resizing 
    # function to the base save function
    def save(self, *args, **kwargs):
        # Run parent class save
        super().save(*args, **kwargs)
        # Resize the given user image to 300px to 300px if the image dimension is > 300px by 300px
        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
