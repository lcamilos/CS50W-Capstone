from tabnanny import verbose
from django.db import models

# Create your models here.
class StudentClassInfo(models.Model):
    level_name = models.CharField(max_length=20)
    level_short_form = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Level List'

    def __str__(self):
        return self.level_name


class StudentSectionInfo(models.Model):
    group_name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Group List'

    def __str__(self):
        return self.group_name


class StudentShiftInfo(models.Model):
    shift_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Shift List'

    def __str__(self):
        return self.shift_name


class StudentInfo(models.Model):
    sporting_year = models.CharField(max_length=100)
    admission_date = models.DateField()
    admission_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    athlete_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    level_type = models.ForeignKey(StudentClassInfo, on_delete=models.CASCADE)
    group_type = models.ForeignKey(StudentSectionInfo, on_delete=models.CASCADE)
    shift_type = models.ForeignKey(StudentShiftInfo, on_delete=models.CASCADE)
    athlete_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    fathers_name = models.CharField(max_length=100)
    fathers_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    fathers_number = models.IntegerField(unique=True)
    mothers_name = models.CharField(max_length=100)
    mothers_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    mothers_number = models.IntegerField()

    class Meta:
        unique_together = ["admission_id", "level_type"]
        verbose_name_plural = 'Athlete List'

    def __str__(self):
        return self.name


class AttendanceManager(models.Manager):
    def create_attendance(self, student_level, student_id):
        student_obj = StudentInfo.objects.get(
            level_type__level_short_form=student_level,
            admission_id=student_id
        )
        attendance_obj = Attendance.objects.create(student=student_obj, status=1)
        return attendance_obj


class Attendance(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)

    objects = AttendanceManager()

    class Meta:
        unique_together = ['student', 'date']

    def __str__(self):
        return self.student.admission_id

        # # for integer field
