from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse


# Create your views here.

class About(View):
    def get(self,request):
        data = {
            "Portal_Name": "Career Connect",
            "Description": "An online job portal to connect job seekers with employers.",
            "Email": "careerconnect@gmail.com",
            "Contact": 9876543210,
            "Website": "https://www.careerconnect.com",
            "Location": "Kochi, Kerala"
        }

        return JsonResponse(data)


class JobView(View):
    def get(self,request):
        jobs = [
            {
                "id": 1,
                "job_title": "Python Developer",
                "company_name": "Tech Solutions Pvt Ltd",
                "location": "Kochi, Kerala",
                "job_category": "IT",
                "job_type": "Full-time",
                "salary": "25000-40000",
                "experience": "0-2 Years",
                "description": "Looking for a Python developer with basic knowledge of Django and MySQL.",
                "required_skills": ["Python", "Django", "MySQL"],
                "application_deadline": "2026-12-15",
                "is_active": True
            },
            {
                "id": 2,
                "job_title": "Frontend Developer",
                "company_name": "Digital Works",
                "location": "Bangalore, Karnataka",
                "job_category": "IT",
                "job_type": "Full-time",
                "salary": "20000-35000",
                "experience": "0-1 Years",
                "description": "Looking for a frontend developer to create responsive websites.",
                "required_skills": ["HTML", "CSS", "JavaScript", "Bootstrap"],
                "application_deadline": "2026-12-20",
                "is_active": True
            },
            {
                "id": 3,
                "job_title": "Data Entry Operator",
                "company_name": "Smart Office Solutions",
                "location": "Trivandrum, Kerala",
                "job_category": "Administration",
                "job_type": "Part-time",
                "salary": "12000-18000",
                "experience": "Fresher",
                "description": "Responsible for entering and maintaining company records.",
                "required_skills": ["MS Excel", "Typing", "Computer Knowledge"],
                "application_deadline": "2026-12-25",
                "is_active": True
            },
            {
                "id": 4,
                "job_title": "Digital Marketing Executive",
                "company_name": "Creative Media",
                "location": "Kozhikode, Kerala",
                "job_category": "Marketing",
                "job_type": "Full-time",
                "salary": "18000-30000",
                "experience": "1-2 Years",
                "description": "Responsible for managing social media accounts and digital marketing campaigns.",
                "required_skills": ["SEO", "Social Media", "Content Writing"],
                "application_deadline": "2026-12-30",
                "is_active": True
            }
        ]

        return JsonResponse(jobs,safe=False)


class CompanyView(View):
    def get(self,request):
        companies = [
            {
                "id": 1,
                "company_name": "Tech Solutions Pvt Ltd",
                "industry": "Information Technology",
                "location": "Kochi, Kerala",
                "website": "https://www.techsolutions.com",
                "email": "hr@techsolutions.com",
                "company_size": "100-200 Employees",
                "description": "A software development company providing technology solutions."
            },
            {
                "id": 2,
                "company_name": "Digital Works",
                "industry": "Web Development",
                "location": "Bangalore, Karnataka",
                "website": "https://www.digitalworks.com",
                "email": "hr@digitalworks.com",
                "company_size": "50-100 Employees",
                "description": "A company specializing in website and application development."
            },
            {
                "id": 3,
                "company_name": "Creative Media",
                "industry": "Digital Marketing",
                "location": "Kozhikode, Kerala",
                "website": "https://www.creativemedia.com",
                "email": "jobs@creativemedia.com",
                "company_size": "20-50 Employees",
                "description": "A digital marketing agency providing online marketing services."
            }
        ]

        return JsonResponse(companies,safe=False)


class CategoryView(View):
    def get(self,request):
        categories = [
            {
                "id": 1,
                "category_name": "Information Technology",
                "description": "Jobs related to software development, networking and IT support.",
                "total_jobs": 25
            },
            {
                "id": 2,
                "category_name": "Marketing",
                "description": "Jobs related to digital marketing, advertising and promotions.",
                "total_jobs": 15
            },
            {
                "id": 3,
                "category_name": "Finance",
                "description": "Jobs related to accounting, banking and financial management.",
                "total_jobs": 10
            },
            {
                "id": 4,
                "category_name": "Administration",
                "description": "Jobs related to office administration and data management.",
                "total_jobs": 12
            },
            {
                "id": 5,
                "category_name": "Customer Service",
                "description": "Jobs related to customer support and client communication.",
                "total_jobs": 18
            }
        ]

        return JsonResponse(categories,safe=False)


class JobTypeView(View):
    def get(self,request):
        job_types = [
            {
                "id": 1,
                "job_type": "Full-time",
                "description": "A regular full-time employment opportunity."
            },
            {
                "id": 2,
                "job_type": "Part-time",
                "description": "An employment opportunity with reduced working hours."
            },
            {
                "id": 3,
                "job_type": "Internship",
                "description": "A training opportunity for students and freshers."
            },
            {
                "id": 4,
                "job_type": "Remote",
                "description": "A job that can be performed from any location."
            },
            {
                "id": 5,
                "job_type": "Contract",
                "description": "An employment opportunity for a fixed period."
            }
        ]

        return JsonResponse(job_types,safe=False)


class ApplicationView(View):
    def get(self,request):
        applications = [
            {
                "id": 1,
                "applicant_name": "Arun Kumar",
                "email": "arun@gmail.com",
                "phone": 9876543211,
                "job_title": "Python Developer",
                "company_name": "Tech Solutions Pvt Ltd",
                "applied_date": "2026-11-01",
                "status": "Pending"
            },
            {
                "id": 2,
                "applicant_name": "Meera Thomas",
                "email": "meera@gmail.com",
                "phone": 9876543212,
                "job_title": "Frontend Developer",
                "company_name": "Digital Works",
                "applied_date": "2026-11-02",
                "status": "Shortlisted"
            },
            {
                "id": 3,
                "applicant_name": "Rahul Raj",
                "email": "rahul@gmail.com",
                "phone": 9876543213,
                "job_title": "Data Entry Operator",
                "company_name": "Smart Office Solutions",
                "applied_date": "2026-11-03",
                "status": "Rejected"
            }
        ]

        return JsonResponse(applications,safe=False)