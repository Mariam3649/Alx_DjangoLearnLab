#!/bin/bash
# إعداد بيئة العمل لمشروع Django REST Framework

echo "🔹 إنشاء وتفعيل البيئة الافتراضية..."
python3 -m venv venv
source venv/bin/activate

echo "🔹 تثبيت Django و Django REST Framework..."
pip install --upgrade pip
pip install django djangorestframework

echo "🔹 عمل migrations..."
python manage.py makemigrations
python manage.py migrate

echo "✅ كله تمام! شغلي السيرفر كده:"
echo "   source venv/bin/activate && python manage.py runserver"
