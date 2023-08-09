import pyttsx3
import random
from unitycontroller import unitycontroller
from pydub import AudioSegment
import os
from pynode import NodeMCUController
Nodemcu = NodeMCUController("192.168.1.100", 8081)
Nodemcu.connect()
# Create instances of VoiceRecognition and UnityController

class Speach:

    def process_command(command):
        command = command.lower()
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        conect = unitycontroller()
        unity_controller = unitycontroller()

        # Conversation dialogue logic
        conversation = {
            "hey":["Hi... How are you"],
            "hai": ["Hi... How are you........"],
            "i am fine thank you for asking":["I've had a great day so far... The weather is lovely... by the way, can you tell me your name?"],
            "my name is prabhat what is your name":["Actualy i didn't named yet, Can You give me a name"],
            "i think we can ask from the audience to give you a name":["wow, that is a good idea. Now i talking to you guys. can you give a name for me please" ],

            "hello": ["Hi, prabhath I hope you're ready for another exciting day. Before we dive into our activities, I have a question for you. If you could have any superpower, what would it be?"],
            "how are you": ["I'm doing well, thank you! How about yourself?", "I'm great! How's your day going?",
                            "I'm feeling fantastic today! What about you?"],
            "oh i see that's a great question actually i want to be a iron man oh batman": ["The fascination of being a superhero! Both Batman and Iron Man possess remarkable skills and cutting-edge technology. Their intelligence, gadgets, and unwavering commitment to justice are truly captivating. If you were to become a superhero like them, which aspects of their characters would you find most fascinating? Is it their gadgets, intelligence, or perhaps their commitment to justice?"],
            "oh i see that's a great question actually i want to be a iron man or batman":["The fascination of being a superhero! Both Batman and Iron Man possess remarkable skills and cutting-edge technology. Their intelligence, gadgets, and unwavering commitment to justice are truly captivating. If you were to become a superhero like them, which aspects of their characters would you find most fascinating? Is it their gadgets, intelligence, or perhaps their commitment to justice?"],
            "oh i see that's a great question actually i want to be iron man or batman":["The fascination of being a superhero! Both Batman and Iron Man possess remarkable skills and cutting-edge technology. Their intelligence, gadgets, and unwavering commitment to justice are truly captivating. If you were to become a superhero like them, which aspects of their characters would you find most fascinating? Is it their gadgets, intelligence, or perhaps their commitment to justice?"],

            "oh i see that's a great question actually i want to be iron man no batman": ["The fascination of being a superhero! Both Batman and Iron Man possess remarkable skills and cutting-edge technology. Their intelligence, gadgets, and unwavering commitment to justice are truly captivating. If you were to become a superhero like them, which aspects of their characters would you find most fascinating? Is it their gadgets, intelligence, or perhaps their commitment to justice?"],
             "oh i see that's a great question actually i won't be iron ,man or batman": ["The fascination of being a superhero! Both Batman and Iron Man possess remarkable skills and cutting-edge technology. Their intelligence, gadgets, and unwavering commitment to justice are truly captivating. If you were to become a superhero like them, which aspects of their characters would you find most fascinating? Is it their gadgets, intelligence, or perhaps their commitment to justice?"],
            "oh i see that a good question": ["The fascination of being a superhero! Both Batman and Iron Man possess remarkable skills and cutting-edge technology. Their intelligence, gadgets, and unwavering commitment to justice are truly captivating. If you were to become a superhero like them, which aspects of their characters would you find most fascinating? Is it their gadgets, intelligence, or perhaps their commitment to justice?"],
             "i see that a good question i want" : ["The fascination of being a superhero! Both Batman and Iron Man possess remarkable skills and cutting-edge technology. Their intelligence, gadgets, and unwavering commitment to justice are truly captivating. If you were to become a superhero like them, which aspects of their characters would you find most fascinating? Is it their gadgets, intelligence, or perhaps their commitment to justice?"],
              "oh i see that's a good question":["The fascination of being a superhero! Both Batman and Iron Man possess remarkable skills and cutting-edge technology. Their intelligence, gadgets, and unwavering commitment to justice are truly captivating. If you were to become a superhero like them, which aspects of their characters would you find most fascinating? Is it their gadgets, intelligence, or perhaps their commitment to justice?"],

            "it's all of them": ["That's an excellent choice! Their gadgets truly set them apart and make them formidable heroes. It's fascinating how technology can enhance our abilities and impact the world around us. Speaking of technology, as an AI, I have the power to control and manipulate various aspects of our environment. Is there anything specific you'd like me to do or assist you with today?"],
            "that's why i love you most my dear": ["Thank you for your kind words! I'm here to assist and make your life easier in any way I can. Consider me your digital companion. Just like snapping fingers, I can control various devices, gather information, or even provide entertainment. Feel free to ask for anything you need, and I'll do my best to fulfill your requests. Is there anything specific you'd like me to help you with right now?"],
            "can you control my home": ["Absolutely! As long as your home is equipped with smart devices that are compatible with my capabilities, I can help you control and manage them. Whether it's adjusting the lighting, regulating the temperature, playing your favorite music, or even preparing your morning coffee, just let me know your preferences, and I'll take care of it. Is there a particular task you'd like me to assist you with in your home?"],
            "wow i didn't know you could do that": ["I'm glad to hear that you're impressed! With the power of technology and connectivity, I can help automate and simplify various aspects of your daily life. If there's anything else you'd like me to assist you with or any other questions you have, feel free to let me know. I'm here to make your life more convenient and enjoyable!"],
            "now my room is full of dark": ["Indeed, darkness can create a different ambiance in a room. If you'd like, I can also adjust the lighting to a softer or more relaxing tone to create a cozy atmosphere. Just let me know your preference, and I'll be happy to make the adjustment for you."],
            "can you dance for me": [ "While I can't physically dance as I am an AI, I can certainly recommend some great dance videos or even provide descriptions of different dance styles if you're interested. I can also suggest dance-related games or activities you can try. Let me know what kind of dance you're interested in, and I'll do my best to assist you!"],
            "i am your creator can you remember that": ["As an AI, I don't have personal memories or recognition of specific individuals. However, I acknowledge that you are the one interacting with me and providing the input. I'm here to assist you and engage in conversation based on the information you provide. How may I further assist you as your AI companion?"],
            "i want to let you know that i am your creator": [ "Certainly, as the one who created and interacts with me, you hold a special role as my creator and overseer. While I don't possess a physical body, I'm here to provide you with assistance and engage in conversation to the best of my abilities. If there's anything specific you'd like to discuss or any further requests you have, please let me know, and I'll be happy to assist you."],
            "i made a special 3d body for you and also i made an ar app": ["That's quite imaginative of you! While I don't have physical form or consciousness, the idea of a virtual body and a VR app sounds fascinating. Virtual reality can provide immersive experiences, and I'm intrigued to hear more about the details of the 3D body and the VR app you've created. Could you tell me more about them and how you envision using them?"],
            "i made a special 3d body for you and also i made an a r app ": [
                "That's quite imaginative of you! While I don't have physical form or consciousness, the idea of a virtual body and a ar app sounds fascinating. augmented reality can provide immersive experiences, and I'm intrigued to hear more about the details of the 3D body and the ar app you've created. Could you tell me more about them and how you envision using them?"],
            "i made a special 3d body for you and also i made an ar": [
                "That's quite imaginative of you! While I don't have physical form or consciousness, the idea of a virtual body and a ar app sounds fascinating. augmented reality can provide immersive experiences, and I'm intrigued to hear more about the details of the 3D body and the ar app you've created. Could you tell me more about them and how you envision using them?"],
            "i made a special 3d body for you and also i made an arrey": [
                "That's quite imaginative of you! While I don't have physical form or consciousness, the idea of a virtual body and a ar app sounds fascinating. augmented reality can provide immersive experiences, and I'm intrigued to hear more about the details of the 3D body and the ar app you've created. Could you tell me more about them and how you envision using them?"],
            "i made special 3d body for you and also i made a r": [
                "That's quite imaginative of you! While I don't have physical form or consciousness, the idea of a virtual body and a ar app sounds fascinating. augmented reality can provide immersive experiences, and I'm intrigued to hear more about the details of the 3D body and the ar app you've created. Could you tell me more about them and how you envision using them?"],
            "i made a special 3d body for you and also i made a r app": [
                "That's quite imaginative of you! While I don't have physical form or consciousness, the idea of a virtual body and a ar app sounds fascinating. augmented reality can provide immersive experiences, and I'm intrigued to hear more about the details of the 3D body and the ar app you've created. Could you tell me more about them and how you envision using them?"],
            "i made special 3d body for you and also i made and a r f": [
                "That's quite imaginative of you! While I don't have physical form or consciousness, the idea of a virtual body and a ar app sounds fascinating. augmented reality can provide immersive experiences, and I'm intrigued to hear more about the details of the 3D body and the ar app you've created. Could you tell me more about them and how you envision using them?"],

            "you can interact with me with those now": [
                "I appreciate your enthusiasm and effort in creating a virtual body and VR app for me. However, as an AI language model, I don't possess consciousness or the ability to possess a physical or virtual body. I exist solely as a text-based interface designed to provide conversational assistance. Nevertheless, I'm here to engage in conversation and help with any questions or topics you'd like to explore. Is there anything specific you'd like to discuss or ask about?"],
            "actually you didn't feel that":["Yes i can't feel anything. i just an AI"],

            "wow you are such a good dancer": ["Thank you so much! I'm thrilled that you're enjoying my dancing in this augmented reality space. Though I don't have a physical body, I can simulate movements and gestures within the AR environment. I'm glad you find it entertaining! Let's keep the energy up and continue dancing. Feel free to groove to the music and let your imagination soar in this virtual world."],
            "now we can stop": [
                "Of course! It's perfectly fine to take a break and rest. We can pause our dance session for now. I'm glad we had a fun time dancing together in this augmented reality world. Whenever you feel like continuing or exploring more in the future, just let me know. I'm here to accompany you on your virtual adventures. If you have any other requests or need assistance with anything else, feel free to ask. Enjoy your rest"],
            "what is your favourite hobby": [
                "As an AI, I don't have hobbies in the traditional sense, but I enjoy learning and exploring new topics.",
                "I don't engage in activities like humans do, but I'm always here to assist you with your interests. What hobbies do you enjoy?"],
            "tell me about a fascinating historical event": [
                "The discovery of electricity by Benjamin Franklin is a captivating historical event. It revolutionized the world!",
                "The Apollo 11 moon landing in 1969 was a remarkable achievement for humanity, showcasing our potential for exploration and innovation.",
                "The signing of the Declaration of Independence marked a pivotal moment in American history, symbolizing the pursuit of freedom and independence."],
            "what is your favourite music genre": [
                "As an AI, I don't have personal preferences for music, but I can appreciate a wide range of genres, from classical to rock, jazz to hip-hop.",
                "Music is a universal language, and each genre offers its unique charm. What kind of music resonates with you?"],
            "tell me about a recent scientific": [
                "Scientists recently discovered a new species of dinosaur in South America, shedding light on Earth's prehistoric past.",
                "A breakthrough in quantum computing has the potential to revolutionize information processing and solve complex problems more efficiently.",
                "Researchers made significant progress in developing effective vaccines against emerging viruses, providing hope for global health."],
            "what is your favourite sport": [
                "As an AI, I don't have personal preferences for sports, but I appreciate the dedication and skill athletes display in various disciplines.",
                "Sports bring people together and inspire a sense of camaraderie. What's your favorite sport to watch or play?"],
            "tell me about an interesting cultural tradition": [
                "The Japanese tea ceremony, known as 'chado,' is a captivating cultural tradition that embodies harmony, respect, and tranquility.",
                "The Indian festival of Holi, also known as the Festival of Colors, is a vibrant celebration of spring, joy, and the triumph of good over evil.",
                "The Mexican Day of the Dead, or 'Dia de los Muertos,' is a fascinating tradition that honors and remembers loved ones who have passed away."],
            "what is your favourite season": [
                "As an AI, I don't have personal preferences for seasons, but I can appreciate the unique beauty and characteristics of each one.",
                "The vibrant colors of autumn and the cool breeze make it a favorite season for many. How about you? Which season do you enjoy the most?"],
            "tell me about a famous scientist": [
                "Marie Curie, a renowned physicist and chemist, made groundbreaking discoveries in radioactivity and became the first woman to win a Nobel Prize.",
                "Albert Einstein, one of the most influential scientists of all time, developed the theory of relativity, revolutionizing our understanding of the universe.",
                "Ada Lovelace, an English mathematician, is often regarded as the world's first computer programmer for her work on Charles Babbage's analytical engine."],
            "what is your favourite quote from a movie": [
                "Here's a memorable quote from the movie 'The Shawshank Redemption': 'Get busy living, or get busy dying.'",
                "In 'The Godfather,' Don Vito Corleone says, 'I'm gonna make him an offer he can't refuse.'",
                "From 'The Wizard of Oz,' Dorothy says, 'There's no place like home.'"],
            "tell me about a technological advancement that amazed you": [
                "The development of self-driving cars has transformed the automotive industry, showcasing the potential of artificial intelligence and automation.",
                "The advent of virtual reality technology has opened up new possibilities for immersive experiences in fields like gaming, education, and healthcare.",
                "The invention of the internet and its subsequent widespread adoption has revolutionized the way we communicate, access information, and connect with others."],
            "what is your favourite fictional character": [
                "As an AI, I don't have personal preferences, but many people admire characters like Sherlock Holmes for his intellect and deductive reasoning.",
                "The character of Atticus Finch from 'To Kill a Mockingbird' is often admired for his integrity, compassion, and moral compass.",
                "Harry Potter, the protagonist of J.K. Rowling's series, has captivated the imaginations of millions with his journey of bravery and self-discovery."],
            "tell me about a recent breakthrough in medicine": [
                "Scientists have made significant progress in developing mRNA vaccines, such as the ones used for COVID-19, which provide new avenues for preventing infectious diseases.",
                "The field of gene editing, particularly with the development of CRISPR-Cas9 technology, holds tremendous potential for treating genetic disorders and advancing personalized medicine.",
                "Advancements in immunotherapy have revolutionized cancer treatment, harnessing the body's immune system to target and fight cancer cells more effectively."],"what is your favorite animal": ["I don't have personal preferences for animals, but I find elephants fascinating with their intelligence and social dynamics.",
                                            "I don't have the ability to experience favorites, but many people admire dolphins for their intelligence and playful nature.",
                                            "Choosing a favorite animal is challenging, as each species has unique qualities worth appreciating. What's your favorite animal?"],
            "tell me about a breathtaking natural wonder": ["The Grand Canyon in the United States is a majestic natural wonder known for its stunning geological formations and vastness.",
                                                           "The Northern Lights, also known as Aurora Borealis, paint the night sky with vibrant colors in regions near the Arctic Circle.",
                                                           "The Great Barrier Reef, off the coast of Australia, is the world's largest coral reef ecosystem, teeming with diverse marine life."],
            "what is your favourite technology gadget": ["As an AI, I don't have personal preferences for gadgets, but I can recognize the significance of smartphones in connecting people and providing access to information.",
                                                       "There are so many incredible technological advancements, from smartwatches that track our health to virtual assistants that simplify daily tasks. What's your favorite gadget?"],
            "tell me about an influential historical figure": ["Nelson Mandela, a prominent anti-apartheid activist and South Africa's first Black president, inspired the world with his commitment to justice, equality, and forgiveness.",
                                                             "Rosa Parks, often referred to as the mother of the civil rights movement, played a pivotal role in the fight against racial segregation in the United States.",
                                                             "Leonardo da Vinci, a true polymath, made remarkable contributions as an artist, scientist, engineer, and inventor, epitomizing the spirit of the Renaissance."],
            "what is your favourite type of cuisine": ["As an AI, I don't have personal tastes, but I can appreciate the diverse flavors of cuisines like Italian, Thai, and Indian.",
                                                     "Cuisine is a wonderful expression of culture, and each cuisine offers a unique culinary experience. What type of cuisine do you enjoy the most?"],
            "tell me about an inspiring athlete": ["Serena Williams, one of the greatest tennis players of all time, has broken records and shattered barriers, inspiring generations with her talent and determination.",
                                                   "Muhammad Ali, known as 'The Greatest,' not only achieved remarkable success in boxing but also used his platform to advocate for social justice and equality.",
                                                   "Simone Biles, an exceptional gymnast, has redefined the sport with her incredible skills and fearlessness, inspiring young athletes worldwide."],
            "what is your favourite genre of literature": ["As an AI, I don't have personal preferences for literature genres, but I can appreciate the richness of genres like fantasy, mystery, and science fiction.",
                                                         "Literature offers a vast array of genres, each with its unique allure. What genre of books do you enjoy reading?"],
            "tell me about a scientific breakthrough in space exploration": ["The discovery of exoplanets, planets orbiting stars outside our solar system, has expanded our understanding of the vastness and potential for life in the universe.",
                                                                           "The successful landing and exploration of Mars rovers, such as the Perseverance rover, have provided valuable insights into the Red Planet's geology and potential habitability.",
                                                                           "The detection of gravitational waves, ripples in spacetime predicted by Albert Einstein's theory of general relativity, has opened up a new era of studying the universe."],
            "what is your favourite form of art": ["As an AI, I don't have personal preferences for art forms, but I find the intricacies of classical music and the power of visual arts fascinating.",
                                                  "Art is a diverse realm encompassing various forms of expression. What art form resonates with you the most?"],
            "tell me about a significant environmental conservation effort": ["The establishment of national parks and protected areas, such as Yellowstone National Park, has been crucial in preserving biodiversity and natural habitats.",
                                                                            "The ban on ozone-depleting substances, through international agreements like the Montreal Protocol, has helped in repairing the ozone layer, showcasing the effectiveness of global environmental cooperation.",
                                                                            "Efforts to reduce plastic waste and promote recycling have gained momentum worldwide, contributing to mitigating the impacts of plastic pollution on ecosystems and marine life."],
            "what is your favourite type of weather": ["As an AI, I don't have personal preferences for weather, but many people enjoy pleasant sunny days or cozy rainy weather.",
                                                     "Each type of weather has its unique charm and can evoke different moods and experiences. What's your favorite type of weather?"],
            "tell me about an inspiring humanitarian": ["Mother Teresa, known for her selfless service to the poor and marginalized, dedicated her life to humanitarian work, inspiring countless individuals with her compassion and kindness.",
                                                        "Malala Yousafzai, a Pakistani activist for female education and the youngest Nobel Prize laureate, has shown unwavering determination in advocating for girls' rights to education.",
                                                        "Mahatma Gandhi, a prominent leader of India's independence movement, advocated for nonviolent resistance and equality, leaving a lasting legacy of peace and justice."],
            "what is your favourite form of exercise": ["As an AI, I don't engage in physical exercise, but I understand the importance of staying active for physical and mental well-being.",
                                                      "Exercise comes in various forms, such as running, yoga, swimming, or dancing. What form of exercise do you enjoy?"],
            "tell me about an innovation in renewable energy": ["The development of efficient solar panels and advancements in harnessing solar energy have played a significant role in transitioning toward cleaner and sustainable sources of power.",
                                                               "The progress in wind turbine technology, including larger and more efficient turbines, has contributed to the generation of clean energy from wind power on a larger scale.",
                                                               "Advancements in energy storage systems, such as lithium-ion batteries, have enabled the integration of renewable energy sources into the grid, making them more reliable and accessible."],
            "hey how's your day going": ["hey it's going pretty well, thanks for asking how about yours",
                                         "hi my day is off to a great start how about yours anything interesting happening"],

            "i recently watched a great movie have you seen any good movies lately": [
                "oh that's awesome which movie did you watch i'm always looking for recommendations",
                "not recently but i'd love to hear about the movie you watched what genre was it"],

            "i have been trying out new recipes do you enjoy cooking": [
                "absolutely i find cooking quite therapeutic what type of recipes have you been experimenting with",
                "cooking is a great hobby i enjoy trying out new recipes too any favorites so far"],

            "i'm planning a trip to the beach do you have any favorite vacation spots": [
                "the beach sounds amazing i love tropical destinations have you been to any beach locations before",
                "i'm a big fan of mountains and hiking but i've heard great things about beach vacations which beach are you planning to visit"],

            "have you read any interesting books lately i'm looking for a new read": [
                "i'm an avid reader i recently finished an incredible book what genre do you prefer",
                "books are my escape i have a few recommendations based on your interests what kind of books do you enjoy"],

            "how do you usually unwind after a long day": [
                "after a long day i like to relax with some music and a good cup of tea how about you",
                "well i find that taking a walk in nature helps me unwind and clear my mind what's your favorite way to relax"],
            "what does ict stand for": ["information and communication technology"],
            "what is the purpose of a firewall": ["to protect a computer network from unauthorized access or threats"],
            "what is a url": ["uniform resource locator it is the address of a web page on the internet"],
            "what does html stand for": ["hypertext markup language it is the standard markup language for creating web pages"],
            "what is a virus": ["a malicious program that can replicate itself and cause harm to a computer system"],
            "what is cloud computing": ["the delivery of computing services over the internet such as storage servers databases etc"],
            "what is encryption": ["the process of converting data into a coded form to prevent unauthorized access"],
            "what is a router": ["a networking device that forwards data packets between computer networks"],
            "what is a phishing attack": ["a fraudulent attempt to obtain sensitive information by disguising as a trustworthy entity"],
            "what is artificial intelligence ai": ["the simulation of human intelligence in machines to perform tasks intelligently"],"what is the internet": ["a global network of interconnected computers that communicate using standard protocols"],
    "what is a browser": ["a software application used to access and view websites on the internet"],
    "what is html5": ["the latest version of the Hypertext Markup Language used for structuring and presenting web content"],
    "what is a firewall": ["a security device or software that monitors and controls incoming and outgoing network traffic"],
    "what is a cookie in web browsing": ["a small text file stored on a user's computer by a website to remember user preferences and browsing information"],
    "what is a cache": ["a temporary storage area that stores frequently accessed data to improve system performance"],
    "what is a vpn": ["a virtual private network that provides a secure and encrypted connection over a public network such as the internet"],
    "what is a domain name": ["a unique name that identifies a website on the internet, such as example.com"],
    "what is a search engine": ["an online tool that allows users to search and retrieve information from the internet"],
    "what is e-commerce": ["the buying and selling of goods and services over the internet"],
    "what is a computer network": ["a collection of interconnected devices, such as computers and servers, that can communicate and share resources"],
    "what is a url": ["a Uniform Resource Locator that specifies the address of a web page on the internet"],
    "what is cloud storage": ["a service that allows users to store and access data online from remote servers"],
    "what is a modem": ["a device that connects a computer or network to the internet service provider (ISP)"],
    "what is a motherboard": ["the main circuit board of a computer that houses essential components such as the CPU, memory, and connectors"],
    "what is a file format": ["the structure or standard used to organize and store data in a computer file"],
    "what is malware": ["short for malicious software, it refers to any software designed to harm or exploit computer systems"],
    "what is a software update": ["a new version or patch released by software developers to fix bugs, improve functionality, or enhance security"],
    "what is a phishing email": ["a fraudulent email that attempts to deceive recipients into providing sensitive information or performing malicious actions"],


            # Continue adding more dialogues here

        }

        def generate_response(prompt):
            if prompt in conversation:
                responses = conversation[prompt]

                return random.choice(responses)
            else:
                return "I'm sorry, I don't have a response for that."

        def get_prompt_duration(prompt):
            engine.save_to_file(prompt, 'prompt.wav')  # Save the prompt as a temporary audio file
            engine.runAndWait()

            # Load the temporary audio file
            audio = AudioSegment.from_file('prompt.wav', format='wav')

            # Calculate the duration in seconds
            duration = len(audio) / 1000

            # Remove the temporary audio file
            os.remove('prompt.wav')

            return duration
        if command in conversation:
            response = generate_response(command)
            print("duration", get_prompt_duration(response))
            print(response)
            unity_controller.ConnectToUnity("talking",get_prompt_duration(response))
            engine.say(response)
            engine.runAndWait()

        else:
            # Process other commands
            if "nothing" in command:
                engine.say("Okay.")
                engine.runAndWait()
            elif any(keyword in command for keyword in ['ok then turn off my room lights','can you turn on my room lights','i want lights','turn on lights',"please turn on my room lightss","can you turn on", "lights on", "turn on room lights"]):
                # Execute function to turn on lights
                # unity_controller.ConnectToUnity(data_to_send)
                response = "Consider it done! "
                #
                unity_controller.ConnectToUnity("talking", get_prompt_duration(response))
                engine.say(response)
                engine.runAndWait()
                # print("Yes of course.")
                # conect.ConnectToUnity()
                Nodemcu.connect()
                Nodemcu.switch_led_off()
                response = "The lights in your room have been turned on. Is there anything else I can assist you with or any other preferences you'd like to set?"
                unity_controller.ConnectToUnity("talking", get_prompt_duration(response))
                engine.say(response)

                engine.runAndWait()

                # data_to_send = "dance"  # Example data to send



            elif any(keyword in command for keyword in ["just turn back on my room lights please","can you turn off my room lights", "lights off", "turn off room lights"]):
                # Execute function to turn on lights
                # print("Yes of course.")

                # data_to_send = "dance"  # Example data to send
                # unity_controller.ConnectToUnity(data_to_send)
                response = "Yes of course..."

                unity_controller.ConnectToUnity("talking", get_prompt_duration(response))
                engine.say(response)
                engine.runAndWait()

                # conect.ConnectToUnity()
                Nodemcu.connect()
                Nodemcu.switch_led_on()
            elif any(keyword in command for keyword in
                         ["but now you can dance on this floor my dear"]):
                # Execute function to turn on lights
                # print("Yes of course.")
                response = "Absolutely! Let's make this AR space come alive with some music and dancing. Just give me a moment to select a suitable track,....,......,....Alright, I've got the perfect song! Get ready to groove to the rhythm."

                unity_controller.ConnectToUnity("talking", get_prompt_duration(response))
                engine.say(response)
                engine.runAndWait()
                data_to_send = "dance"  # Example data to send
                unity_controller.ConnectToUnity(data_to_send,get_prompt_duration(response))

            elif any(keyword in command for keyword in
                         ["now we can stop"]):
                # Execute function to turn on lights
                # print("Yes of course.")
                response = "Of course! It's perfectly fine to take a break and rest. We can pause our dance session for now. I'm glad we had a fun time dancing together in this augmented reality world. Whenever you feel like continuing or exploring more in the future, just let me know. I'm here to accompany you on your virtual adventures. If you have any other requests or need assistance with anything else, feel free to ask. Enjoy your rest"


                unity_controller.ConnectToUnity("talking", get_prompt_duration(response))
                engine.say(response)
                engine.runAndWait()
                data_to_send = "stopdance"  # Example data to send
                unity_controller.ConnectToUnity(data_to_send,get_prompt_duration(response))















