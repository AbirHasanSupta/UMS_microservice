import uuid

from django.db import models


class UserProfile(models.Model):
    user_id = models.UUIDField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField()
    photo = models.ImageField(
        upload_to="profile_photos/",
        null=True,
        blank=True
    )

    blood_group = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(
        max_length=20,
        choices=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
        null=True,
        blank=True,
    )
    phone = models.CharField(max_length=20)
    alternate_phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()

    present_address = models.TextField()
    permanent_address = models.TextField(null=True, blank=True)

    emergency_contact_name = models.CharField(max_length=100)
    secondary_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone  = models.CharField(max_length=20)
    secondary_contact_phone = models.CharField(max_length=20, blank=True, null=True)

    marital_status = models.CharField(
        max_length=20,
        choices=[
            ("single", "Single"),
            ("married", "Married"),
            ("other", "Other"),
        ],
        null=True,
        blank=True,
    )

    nationality = models.CharField(max_length=50, null=True, blank=True)
    passport_number = models.CharField(max_length=50, null=True, blank=True)
    religion = models.CharField(max_length=50,
                                choices=[
                                    ("islam", "Islam"),
                                    ("hindu", "Hindu"),
                                    ("buddha", "Buddha"),
                                    ("christian", "Christian"),
                                    ("other", "Other")
                                ],
                                null=True, blank=True)
    national_id = models.CharField(max_length=50, null=True, blank=True)
    joined_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def user_document_path(instance, filename):
    return f"user_{instance.user.id}/documents/{filename}"


class UserDocument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE, related_name="documents")
    document_type = models.CharField(max_length=100)
    file = models.FileField(upload_to=user_document_path, max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
