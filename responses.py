# responses.py - Contains keyword mappings to responses for VITAP Chatbot

responses = {
    # General VITAP Info
    "vitap": "VITAP (VIT Amaravati) is a premier engineering institution located in Amaravati, Andhra Pradesh, India. It offers undergraduate and postgraduate programs in various engineering disciplines.",
    "about vitap": "VITAP is part of the VIT University group, known for its quality education, research, and innovation. It focuses on holistic development of students.",
    "location": "VITAP is located in Amaravati, the capital city of Andhra Pradesh, India.",
    "contact": "For contact information, visit the official VITAP website or reach out to the admissions office.",

    # Courses Available
    "courses": "VITAP offers B.Tech programs in Computer Science, Mechanical, Electrical, Civil, Electronics, and more. M.Tech and PhD programs are also available.",
    "btech": "B.Tech programs include CSE, ECE, EEE, MECH, CIVIL, and Chemical Engineering.",
    "mtech": "M.Tech programs are offered in various specializations like CSE, ECE, etc.",
    "phd": "PhD programs are available in engineering and sciences.",

    # Course Registration
    "course registration": "Course registration is done through the VITAP portal. Students select courses based on their branch and semester requirements. Deadlines are announced by the academic office.",
    "register courses": "To register for courses, log in to the student portal, select your courses, and submit before the deadline.",
    "electives": "Elective courses can be chosen from a list provided by the department. Consult your advisor for guidance.",

    # Hostel Registration
    "hostel": "VITAP provides on-campus hostels for students. Registration is done during admission or separately for existing students.",
    "hostel registration": "Apply for hostel through the student portal. Provide necessary documents and pay fees. Availability is on first-come-first-served basis.",
    "hostel fees": "Hostel fees vary based on room type. Contact the hostel office for details.",

    # Venues
    "venues": "VITAP has auditoriums, seminar halls, sports grounds, and labs. Check the campus map for locations.",
    "auditorium": "The main auditorium is used for events and lectures. Book through the events committee.",
    "sports": "Sports facilities include basketball court, football ground, gymnasium, and more.",

    # Classes
    "classes": "Classes are held in designated classrooms and labs. Timetables are available on the student portal.",
    "timetable": "Check your semester timetable on the VITAP portal under academics section.",
    "labs": "Labs are equipped for practical sessions. Follow safety guidelines.",

    # Faculty Info
    "faculty": "VITAP has experienced faculty members. Visit the department pages on the website for details.",
    "faculty cabins": "Faculty cabins are located in respective department buildings. Office hours are posted.",
    "department venues": "Each department has its own building with classrooms, labs, and faculty offices.",

    # Upcoming Events
    "events": "Upcoming events include fests, workshops, seminars. Check the events page on VITAP website or student portal.",
    "fest": "Technical and cultural fests are organized annually. Stay tuned for announcements.",
    "workshops": "Workshops on latest technologies are conducted regularly.",

    # Backlog Students
    "backlog": "Backlog students can re-register for failed courses in subsequent semesters.",
    "re register": "To re-register, contact the academic office or advisor. Pay fees and attend classes.",
    "backlog guidance": "Seek guidance from faculty advisors. Attend remedial classes if available.",

    # Default
    "default": "I'm sorry, I didn't understand that. Please ask about VITAP, courses, registration, hostels, venues, classes, faculty, events, or backlog guidance."
}

# Function to get response based on keywords
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return responses["default"]
