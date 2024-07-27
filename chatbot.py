from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

my_chatbot = Flask(__name__)

@my_chatbot.route("/whatsapp", methods=['POST'])
def chatbot():
    incoming_message = request.values.get('Body', '').lower()
    response = MessagingResponse()

    if incoming_message in ['hi', 'hello', 'start']:
        # main menu welcome message
        welcomemessage1 = response.message('Welcome to the House On The Rock unofficial chatbot! How can we assist you today?')
        # main menu options
        welcomemessage2 = response.message(
            'Option 1: Service Times\n'
            'Option 2: Events\n'
            'Option 3: Sermons\n'
            'Option 4: Contact Us\n'
            'Option 5: About Us'
        )


    elif incoming_message in ['1', 'service times', 'service']:
        servicemessage = response.message('Here are our service times:')
        servicemessage1 = response.message(
            'Sunday Services\n'
            'First Service: 6:00AM to 8:00AM\n'
            'Second Service: 8:30AM to 10:30AM\n'
            'Third Service: 11:00AM to 12:00AM\n'
            'Evening Service: 5:00PM to 7:00PM'
        )
        servicemessage2 = response.message(
            'Weekday Services\n'
            'Wednesday Mid-Week Service: 7:00PM - 9:00PM\n'
            'Friday Praise Service: 6:00PM - 7:00PM'
        )
        servicemessage3 = response.message(
            'You can also check our calender for special services and upcoming events at: \n'
            'https://theexperiencelagos.com'
        )
        servicemessage4 = response.message(
             'For donations, offering, tithes and special seed:\n'
             'https://pay.squadco.com/link/2DX44H'
        )


    elif incoming_message in ['2', 'upcoming events', 'upcoming', 'events']:
        eventmessage = response.message(
            'Upcoming Events at House On The Rock\n'
            'Option 2.1: Community Events\n'
            'Option 2.2: Bible Study Groups\n'
            'Option 2.3: Youth Activities'
        )
    elif incoming_message in ['2.1', 'community events', 'community']:
            communitymessage = response.message(
                 'Our Community Events Include:\n'
            )
            communitymessage1 = response.message(
                 'Fundraisers\n'
                 'Outreach Programs'
            )
    elif incoming_message in ['2.2', 'bible study groups', 'bible study']:
            biblestudymessage1 = response.message('Bible study groups are held on:\n')
            biblestudymessage2 = response.message(
                 'Tuesdays at 6:00PM - 7:00 PM\n'
                 'Thursdays at 10:00AM - 11:00AM'
            )
    elif incoming_message in ['2.3', 'youth activities', 'youth']:
            youthactivitiesmessage = response.message('Our youth ativities include:\n')
            youthactivitiesmessage1 = response.message(
                 'Youth Group Meetings\n'
                 'Retreat and Camps'
            )

    
    elif incoming_message in ['3', 'sermon', 'message']:
         sermonmessage = response.message('Listen to our lastest sermons:')
         sermonmessage1 = response.message(
              'Sermon Series\n'
              'Series Title 1\n'
              'Series Title 2'
              )
         sermonmessage2 = response.message(
              'Browse our past sermons at'
              'https://www.youtube.com/@hotrlagos'
              )


    elif incoming_message in ['4', 'contact us', 'conact', 'contacts']:
         contactmessage = response.message('Get in touch with us:')
         contactmessage1 = response.message(
              'Our contact information is:\n'
              'Phone Number: +234(0)201-461 4120\n'
              'Email Address: info@houseontherock.org.ng\n'
              'Office Hours: 12:00PM to 6:00PM (Monday to Saturday)'
         )
         contactmessage2 = response.message(
              'Our Social Media Pages\n'
              'Facebook: https://www.facebook.com/houseontherock\n'
              'Instagram: https://www.instagram.com/houseontherockchurch\n'
              'YouTube: https://www.instagram.com/houseontherockchurch'
              )
         contactmessage3 = response.message(
              'Find directions to our church here.'
              'Rock Cathedral Drive, Lekki-Epe Expressway Lekki, Lagos'
              'https://www.google.com/maps/dir/6.425514,3.422592/House+On+The+Rock,+The+Rock+Cathedral,+Lekki+-+Epe+Expy,+Lekki+105102/@6.4363656,3.416743,13z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x103bf5d31b87fb33:0xff74f3497b20d13f!2m2!1d3.493709!2d6.4366922?entry=ttu'
              )


    elif incoming_message in ['5', 'about us', 'about']:
         aboutmessage = response.message(
              'Learn more about House On The Rock:\n'
              'Shop at Our MP3 store\n'
              'https://houseontherock.org.ng/shop/'
              'Download our App\n'
              'Apple: https://apps.apple.com/ng/app/house-on-the-rock/id819457115 \n'
              'Android: https://play.google.com/store/apps/details?id=com.subsplash.thechurchapp.s_G2QFHM'
              )


    else:
        response.message("I don't understand your request. Please choose a number from the options provided.")

    return str(response)

if __name__ == "__main__":
    my_chatbot.run(debug = True)
