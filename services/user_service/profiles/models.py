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


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="programs")

    def __str__(self):
        return f"{self.name} ({self.department.code})"


class Designation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Semester(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


import uuid
from django.db import models


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.OneToOneField("UserProfile", on_delete=models.CASCADE, related_name="student_profile")

    student_code = models.CharField(max_length=50, unique=True)  # flexible institutional ID
    enrollment_date = models.DateField()

    program = models.ForeignKey("Program", on_delete=models.CASCADE, related_name="students")
    current_semester = models.ForeignKey("Semester", on_delete=models.SET_NULL, null=True, blank=True)

    gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    graduation_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_code} - {self.profile.first_name}"


class Teacher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.OneToOneField("UserProfile", on_delete=models.CASCADE, related_name="teacher_profile")

    teacher_code = models.CharField(max_length=50, unique=True)  # institutional ID
    joining_date = models.DateField()

    designation = models.ForeignKey("Designation", on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name="teachers")

    specialization = models.CharField(max_length=255, null=True, blank=True)
    employment_type = models.CharField(
        max_length=50,
        choices=[
            ("full_time", "Full-time"),
            ("part_time", "Part-time"),
            ("contract", "Contract"),
        ],
        default="full_time",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.teacher_code} - {self.profile.first_name}"


class Admin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.OneToOneField("UserProfile", on_delete=models.CASCADE, related_name="admin_profile")

    admin_code = models.CharField(max_length=50, unique=True)
    hire_date = models.DateField()

    role = models.ForeignKey("AdminRole", on_delete=models.SET_NULL, null=True, blank=True)
    office = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.admin_code} - {self.profile.first_name}"


class AdminRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

