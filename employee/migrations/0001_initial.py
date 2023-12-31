# Generated by Django 4.2.7 on 2023-11-04 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empResume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionAppliedFor', models.CharField(max_length=500, null=True, verbose_name='Position Applied For')),
                ('fullName', models.CharField(max_length=200, null=True, verbose_name='Full Name')),
                ('totalExp', models.CharField(max_length=200, null=True, verbose_name='Total Experience')),
                ('currentCTC', models.CharField(max_length=200, null=True, verbose_name='Current CTC')),
                ('noticePeriod', models.CharField(max_length=200, null=True, verbose_name='Notice Period')),
                ('relocation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True, verbose_name='Relocation')),
                ('mobile', models.CharField(max_length=20, null=True, verbose_name='Mobile')),
                ('whatsapp', models.CharField(max_length=20, null=True, verbose_name='Mobile')),
                ('email', models.CharField(max_length=500, null=True, verbose_name='Email')),
                ('currentRole', models.CharField(max_length=500, null=True, verbose_name='Current Role')),
                ('changeReason', models.CharField(max_length=500, null=True, verbose_name='Change Reason')),
                ('currentOrganisation', models.CharField(max_length=500, null=True, verbose_name='Current Organisation')),
                ('academicQualification', models.CharField(max_length=500, null=True, verbose_name='Academic Qualification')),
                ('technicalCertification', models.CharField(max_length=500, null=True, verbose_name='Technical Certification')),
                ('uploadCV', models.FileField(null=True, upload_to='cv/%Y/%m/%d', verbose_name='Upload CV')),
                ('status', models.CharField(choices=[('Submitted', 'Submitted'), ('Rejected', 'Rejected')], default='Submitted', max_length=10, null=True, verbose_name='Status')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('modifiedDate', models.DateTimeField(auto_now=True, verbose_name='Modified Date')),
            ],
            options={
                'verbose_name': 'Employee CV',
                'verbose_name_plural': 'Employee CV',
                'db_table': 'emp-cv-list',
            },
        ),
    ]
