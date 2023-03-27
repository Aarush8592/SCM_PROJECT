lt="https://youtu.be/9OeznAkyQz4"
                                     webbrowser.open(lt)
                                     speak("please type y after completing the video:")
                                     u=input("enter y if completed the video:")
                                     city="Y"
                                     if (city.upper()=='Y'):
                                        speak("please attempt these questions now")
                                        l = "https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/"
                                        webbrowser.open(l)
                                                                               
                    elif (jasoos=='1'):
                        speak("you have done very well.")
                        speak("just need a bit of practice")
                        speak("please see this video")
                        vid2="https://www.youtube.com/watch?v=vLqTf2b6GZw"
                        webbrowser.open(vid2)
                        state = "Y"
                        if(state.upper() == "Y"):
                            speak("if complete the video please enter y")
                            s = input("enter y if completed watching the video:")
                            speak("please attempt these questions now.")
                            li="https://www.codingninjas.com/"
                            webbrowser.open(li)
                        
                    else:
                        speak("congratulations! you are very hard working")
                        speak("to polish your skills please attempt these questions")
                        hr="https://www.hackerrank.com/domains/python"
                        webbrowser.open(hr)
            s=pth()
            s.intro()
            
        elif("hello" in query):
            reply = random.choice(hello)
            speak(reply)
            
        elif ("go to sleep" in query):
             reply = random.choice(reply_bye)
             speak(reply)
             break
