from django.http import JsonResponse
import os
from supabase import create_client, Client



def signUp(request):
    if (request.method == "GET"):
        name = request.GET.get("name")
        email = request.GET.get("email")
        password = request.GET.get("password")
        
        record = {
            "Name" : name, 
            "Email": email, 
            "Password":  password
            }
        
        supaUrl:str = "https://ejloapznmadflishlawt.supabase.co"
        supaKey:str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVqbG9hcHpubWFkZmxpc2hsYXd0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg4NzA1MjAsImV4cCI6MjAwNDQ0NjUyMH0.HTyNjhcAyaDhnaC9OODZ_SlpZZ-XXeM7C3Fa5oGNwNU"
        supabase: Client = create_client(supaUrl, supaKey)

        data = supabase.table("UserRecords").select('').eq('Email', email).execute().data

        if(len(data)>0):
            return JsonResponse({'response' : 'USER ALREADY EXISTS'})
        
        else:
            supabase.table("UserRecords").insert(record).execute()
            return JsonResponse({'response' : 'Data Entered Successfully'})

      
    else:
        return JsonResponse({'response': 'Invalid Method'})


def signIn(request):
    if (request.method == "GET"):
        email = request.GET.get("email")
        password = request.GET.get("password")
        
        record = { 
            "Email": email, 
            "Password":  password
            }
        
        supaUrl:str = "https://ejloapznmadflishlawt.supabase.co"
        supaKey:str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVqbG9hcHpubWFkZmxpc2hsYXd0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg4NzA1MjAsImV4cCI6MjAwNDQ0NjUyMH0.HTyNjhcAyaDhnaC9OODZ_SlpZZ-XXeM7C3Fa5oGNwNU"
        supabase: Client = create_client(supaUrl, supaKey)

        data = supabase.table("UserRecords").select('Password').eq('Email', email).execute().data

        if(len(data)==0):
            return JsonResponse({'response' : 'USER NOT FOUND'})
        
        else:
            if password == data[0]['Password']:
                return JsonResponse({'response' : 'SIGN IN SUCCESSFULL'})
            else:
                return JsonResponse({'response' : 'INCORRECT PASSWORD'})
      
    else:
        return JsonResponse({'response': 'Invalid Method'})
