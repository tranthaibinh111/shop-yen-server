# Generated by Django 2.1.7 on 2019-04-15 03:55

import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertise_type', models.CharField(blank=True, choices=[('E', 'Email'), ('F', 'Facebook')], max_length=2, null=True)),
                ('name', models.CharField(max_length=100)),
                ('start_at', models.DateField(auto_now_add=True)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('summary', models.CharField(blank=True, max_length=255, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_advertisement', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_advertisement', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CronAdvertisement',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('W', 'Đang chờ chạy quảng cáo'), ('S', 'Đang gửi quảng cáo'), ('D', 'Hoàn thành'), ('E', 'Gửi quảng cáo thất bại')], default='W', max_length=2)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('full_name', models.CharField(max_length=100)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=2, null=True)),
                ('contact_type', models.CharField(choices=[('M', 'Mobile'), ('P', 'Home phone'), ('E', 'Email')], max_length=2)),
                ('contact', models.CharField(max_length=100)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_customer', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('D', 'Đang chuyển hàng'), ('CL', 'Đơn hàng hoàn thành'), ('RF', 'Đơn hàng đổi trả'), ('CC', 'Đơn hàng bị hủy')], default='D', max_length=2)),
                ('from_place', models.CharField(max_length=255)),
                ('to_place', models.CharField(max_length=255)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_delivery', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_delivery', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Deliveries',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('R', 'Nhận đơn đặt hàng'), ('D', 'Đang chuyển hàng'), ('CL', 'Đơn hàng hoàn thành'), ('RF', 'Đơn hàng đổi trả'), ('CC', 'Đơn hàng bị hủy')], default='R', max_length=2)),
                ('amount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('money_of_sale', models.DecimalField(decimal_places=0, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('service', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('fee', models.DecimalField(decimal_places=0, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('income', models.DecimalField(decimal_places=0, default=0, max_digits=16, validators=[django.core.validators.MinValueValidator(0)])),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_order', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_yen.Customer')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('OS', 'Hết hàng'), ('R', 'Nhận đơn đặt hàng'), ('D', 'Đang chuyển hàng'), ('CL', 'Đã giao hàng'), ('RF', 'Đơn hàng đổi trả'), ('CC', 'Đơn hàng bị hủy')], default='R', max_length=2)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=9, validators=[django.core.validators.MinValueValidator(0)])),
                ('amount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('money_of_sale', models.DecimalField(decimal_places=0, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_order_detail', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_order_detail', to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_yen.Order')),
            ],
            options={
                'verbose_name_plural': 'Order Details',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateTimeField(auto_now_add=True, help_text='Thời gian bắt đầu áp dụng giá')),
                ('cost_of_good', models.DecimalField(decimal_places=0, default=0, help_text='Giá vốn', max_digits=9, validators=[django.core.validators.MinValueValidator(0)])),
                ('regular_price', models.DecimalField(decimal_places=0, default=0, help_text='Giá vốn', max_digits=9, validators=[django.core.validators.MinValueValidator(0)])),
                ('retail_price', models.DecimalField(decimal_places=0, default=0, help_text='Giá vốn', max_digits=9, validators=[django.core.validators.MinValueValidator(0)])),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_price', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_price', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to="media/products/<module 'uuid' from '/usr/local/lib/python3.7/uuid.py'>")),
                ('weight', models.DecimalField(decimal_places=1, default=0, max_digits=8)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_product', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_product', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('zalo', models.CharField(blank=True, max_length=20, null=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_provider', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_provider', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_refund', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_refund', to=settings.AUTH_USER_MODEL)),
                ('order_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_yen.OrderDetail')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_service_price', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_service_price', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Service Prices',
            },
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('full_name', models.CharField(max_length=100)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=2, null=True)),
                ('contact_type', models.CharField(choices=[('M', 'Mobile'), ('P', 'Home phone'), ('E', 'Email')], max_length=2)),
                ('contact', models.CharField(max_length=100)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_shipper', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_shipper', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0, help_text='Số lượng thực tế trong kho', validators=[django.core.validators.MinValueValidator(0)])),
                ('order', models.IntegerField(default=0, help_text='Số lượng mà khách hàng đang đặt', validators=[django.core.validators.MinValueValidator(0)])),
                ('refund', models.IntegerField(default=0, help_text='Số lượng mà khách hàng đang đổi trả', validators=[django.core.validators.MinValueValidator(0)])),
                ('balance', models.IntegerField(default=0, help_text='Số lượng dự tính còn lại', validators=[django.core.validators.MinValueValidator(0)])),
                ('fee', models.DecimalField(decimal_places=0, default=0, help_text='Tiền phí nhập hàng', max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('fund', models.DecimalField(decimal_places=0, default=0, help_text='Tổng tiền vốn', max_digits=25, validators=[django.core.validators.MinValueValidator(0)])),
                ('money_of_sale', models.DecimalField(decimal_places=0, default=0, help_text='Tổng tiền bán', max_digits=25, validators=[django.core.validators.MinValueValidator(0)])),
                ('refund_money', models.DecimalField(decimal_places=0, default=0, help_text='Tổng tiền do khách hàng trả hàng', max_digits=25, validators=[django.core.validators.MinValueValidator(0)])),
                ('income', models.DecimalField(decimal_places=0, default=0, help_text='Tiền lời', max_digits=30, validators=[django.core.validators.MinValueValidator(0)])),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('timestamp', models.IntegerField(default=1555300517, help_text='Thời gian cuối cùng kiểm kê kho')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_stock', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_stock', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_yen.Product')),
            ],
        ),
        migrations.CreateModel(
            name='StockIn',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=9, validators=[django.core.validators.MinValueValidator(0)])),
                ('amount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('cost_of_good', models.DecimalField(decimal_places=0, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('service', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('fee', models.DecimalField(decimal_places=0, default=0, max_digits=15, validators=[django.core.validators.MinValueValidator(0)])),
                ('fund', models.DecimalField(decimal_places=0, default=0, max_digits=16, validators=[django.core.validators.MinValueValidator(0)])),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_stock_in', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_stock_in', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_yen.Product')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_yen.Provider')),
            ],
            options={
                'verbose_name_plural': 'Stock Ins',
            },
        ),
        migrations.CreateModel(
            name='StockOut',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_stock_out', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_stock_out', to=settings.AUTH_USER_MODEL)),
                ('order_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop_yen.OrderDetail')),
            ],
            options={
                'verbose_name_plural': 'Stock Outs',
            },
        ),
        migrations.CreateModel(
            name='CronAdvertisementHistory',
            fields=[
                ('cronadvertisement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop_yen.CronAdvertisement')),
                ('done_at', models.DateTimeField(auto_now_add=True)),
            ],
            bases=('shop_yen.cronadvertisement',),
        ),
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_yen.Product'),
        ),
        migrations.AddField(
            model_name='price',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_yen.Provider'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_yen.Product'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='order_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_yen.OrderDetail'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='shipper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_yen.Shipper'),
        ),
        migrations.AddField(
            model_name='cronadvertisement',
            name='advertisement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_yen.Advertisement'),
        ),
        migrations.AddField(
            model_name='cronadvertisement',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_marketplace', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cronadvertisement',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_yen.Customer'),
        ),
        migrations.AddField(
            model_name='cronadvertisement',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_marketplace', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together={('product',)},
        ),
        migrations.AlterUniqueTogether(
            name='shipper',
            unique_together={('full_name', 'contact_type', 'contact')},
        ),
        migrations.AlterUniqueTogether(
            name='provider',
            unique_together={('name', 'facebook'), ('name', 'zalo'), ('name', 'email'), ('name', 'mobile'), ('name', 'phone')},
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name', 'weight')},
        ),
        migrations.AlterUniqueTogether(
            name='price',
            unique_together={('provider', 'product', 'apply_date')},
        ),
        migrations.AlterUniqueTogether(
            name='orderdetail',
            unique_together={('order', 'product')},
        ),
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together={('full_name', 'contact_type', 'contact')},
        ),
        migrations.AlterUniqueTogether(
            name='advertisement',
            unique_together={('advertise_type', 'name', 'start_at')},
        ),
    ]
