# Generated by Django 3.1.7 on 2021-04-05 09:36

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=35)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('dob', models.DateField(null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('status', models.BooleanField(default=False)),
                ('masjid_name', models.CharField(max_length=255, null=True)),
                ('masjid_id', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('card_info', models.BooleanField(default=False)),
                ('cardName', models.CharField(max_length=55, null=True)),
                ('donation_reference', models.CharField(max_length=50, null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('stripe_customer_id', models.CharField(max_length=255, null=True)),
                ('card_token', models.CharField(max_length=100, null=True)),
                ('masjidCardName', models.CharField(max_length=100, null=True)),
                ('verify_user', models.BooleanField(default=False)),
                ('masjidCardNumber', models.CharField(max_length=100, null=True)),
                ('masjidAddress', models.CharField(max_length=500, null=True)),
                ('lat', models.CharField(max_length=100, null=True)),
                ('lng', models.CharField(max_length=100, null=True)),
                ('profile_pic', models.ImageField(null=True, upload_to='profile_pic')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(null=True)),
                ('object_id', models.CharField(max_length=255, null=True)),
                ('masjid_id', models.IntegerField(null=True)),
                ('amount', models.CharField(max_length=255, null=True)),
                ('donation_reference', models.CharField(max_length=50, null=True)),
                ('donation_for', models.CharField(max_length=50, null=True)),
                ('payment_type', models.CharField(max_length=50)),
                ('recurring_period', models.CharField(max_length=50, null=True)),
                ('detail', models.CharField(max_length=255, null=True)),
                ('starting_at', models.DateField(null=True)),
                ('next_at', models.DateField(null=True)),
                ('payment_status', models.BooleanField(default=True)),
                ('charge_id', models.CharField(max_length=255, null=True)),
                ('customer_id', models.CharField(max_length=255, null=True)),
                ('cardToken', models.CharField(max_length=500, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=250, null=True)),
                ('feedback', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
