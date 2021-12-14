from django.shortcuts import render
from .serializers import StatusListSerializer, RecordListSerializer
from rest_framework import generics, permissions
from .models import Status, Record

# Create your views here.

class o