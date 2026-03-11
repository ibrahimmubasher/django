from rest_framework import serializers
from datetime import date
from .models import Book, Author, Genre



class AuthorSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    
    class Meta:
        model = Author
        fields = "__all__"

    def get_age(self, obj):
        dob = obj.date_of_birth
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age
        
        
    


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    

    class Meta:
        model = Book
        fields = "__all__"
        
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must longwr than 3 characters.")
        return value
        
    def validate_published_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Published date cannot be in the future.")
        return value
