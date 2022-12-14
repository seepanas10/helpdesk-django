# Generated by Django 4.0.6 on 2022-07-15 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(choices=[('ACC', 'Accounts'), ('MAINT', 'Maintennance'), ('INFRA', 'Infrastructure')], max_length=5)),
                ('priority', models.CharField(choices=[('HIGH', 'High'), ('MED', 'Medium'), ('LOW', 'Low')], max_length=5)),
                ('due_Date', models.DateField()),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('fileupload', models.FileField(blank=True, help_text='Not Mandatory', upload_to='uploads/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('WORKING', 'Working'), ('REOPENED', 'Reopened'), ('CLOSED', 'Closed')], default='OPEN', max_length=10)),
                ('ticknum', models.IntegerField()),
            ],
        ),
    ]
