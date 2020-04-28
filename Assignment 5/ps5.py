# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Daniel Guillermo
# Collaborators: Daniel Guilermo
# Time: about 10 hours

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        
        # Had to add error handling because yahoo news doesn't give 
        # descriptions anymore
        try:
            description = translate_html(entry.description)
            
        except AttributeError:
            description = ''
            
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        
        except ValueError:
            #added error handling because date format in google page changed
            try: 
                pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")
                
            except ValueError: #added new date-time format that google outputs
                   pubdate = datetime.strptime(pubdate, "%Y-%m-%dT%H:%M:%S%z")  
                    
                    
        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1
# TODO: NewsStory
class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        '''
        Initializes a NewsStory object
                
        guid (string): globally unique identifier, A globally unique identifier for this news story
        title (string): The news story's headline
        description (string): A paragraph or so summarizing the news story.
        link (string): A link to a website with the entire story.
        pubDate (datetime): Date the news was published
        
        a NewsStory object has 5 attributes.
            
        self.guid (string)
        self.title (string)
        self.description (string)
        self.link (string)
        self.pubdate (datetime)
        '''
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        '''
        Used to safely access self.guid outside of the class
        
        Returns: self.guid
        '''
        return self.guid
    
    def get_title(self):
        '''
        Used to safely access self.title outside of the class
        
        Returns: self.title
        '''
        return self.title
    
    def get_description(self):
        '''
        Used to safely access self.description outside of the class
        
        Returns: self.description
        '''
        return self.description
    
    def get_link(self):
        '''
        Used to safely access self.link outside of the class
        
        Returns: self.link
        '''
        return self.link
    
    def get_pubdate(self):
        '''
        Used to safely access self.pubdate outside of the class
        
        Returns: self.pubdate
        '''
        return self.pubdate
    
#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger

class PhraseTrigger(Trigger):
    def __init__(self, Phrase): #dont think this is right
        '''
        Initializes a PhraseTrigger object
                
        Phrase (string): trigger phrase not case sensitive
        '''
        for word in Phrase.split():
            if not word.isalpha() or '  ' in Phrase:
                    raise TypeError('No a valid phrase')
        self.Phrase = str(Phrase).lower()
    
    def is_phrase_in(self, text):
        '''
        It returns True if the whole self.Phrase is present in text, False otherwise.
        The trigger should fire only when each word in the phrase is present in its 
        entirety and appears consecutively in the text, separated only by spaces 
        or punctuation. The trigger is not case sensitive.
        
        text (string): text, not case sensitive
        '''
        if not text.isalnum(): #if the text has symbols in it
            for s in string.punctuation: #loop over every punctuation
                text = text.replace(s,' ') #replace every punctuation wirh a space
        
        text_li = text.lower().split() #making text a lsit and all lower
        Phrase_li = self.Phrase.split() #making phrase a list
        F = 0; #flag counter
        for word in text_li: #looping for every word in text
            for w in Phrase_li: #looping for every word in phrase
                if word == w: #if the word in text appaers exactly in phrase
                    F += 1 #increase counter for every word in text that matches perfectly a wrod in phrase
                    
        text_lower = ' '.join(text_li) #joining the cleaned out text
                              
        return self.Phrase in text_lower and F == len(Phrase_li) #retrun boolean if the phrase is in the text AND if the flag 
                                                                 #counter ecuals the number of words in phrase 
        
    
# Problem 3
# TODO: TitleTrigger

class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.is_phrase_in(story.get_title())

# Problem 4
# TODO: DescriptionTrigger

class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.is_phrase_in(story.get_description())
    
# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    """
    subclass of Trigger. The class's constructor should take in time in EST as a string in the format of "3 Oct 2016 17:00:10 ". Make sure to convert time from string to a datetime before saving it as an attribute.
    """
    def __init__(self, time_trigger):
        """
        Initializes the TimeTrigger object.
        
        time_trigger (string): in the format of "3 Oct 2016 17:00:10 " in EST
            
        Takes in time in EST as a string in the format of "3 Oct 2016 17:00:10 ".
        Converts time from string to a datetime and saves it as an attribute.
        """
        Time_format = datetime.strptime(time_trigger,"%d %b %Y %H:%M:%S")
        Time_format = Time_format.replace(tzinfo=pytz.timezone("EST"))
        self.Time = Time_format
        
# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.get_pubdate().tzinfo == None:
            self.Time = self.Time.replace(tzinfo = None)
        return  story.get_pubdate() < self.Time
    
class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        if story.get_pubdate().tzinfo == None:
            self.Time = self.Time.replace(tzinfo = None)
        return story.get_pubdate() > self.Time

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        """
        Initializes the NotTrigger object.
        
        trigger (Trigger): Trigger with its required phrase input
        """
        self.trigger = trigger
    def evaluate(self, story):
        """
        Produces its output by inverting the output of another trigger
        """
        return not self.trigger.evaluate(story)
        

# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        """
        Initializes the AndTrigger object.
        
        trigger1 (Trigger): Trigger with its required phrase input
        trigger2 (Trigger): Trigger with its required phrase input
        """
        self.tr1 = trigger1
        self.tr2 = trigger2
        
    def evaluate(self, story):
        """
        True on a news story only if both of the inputted triggers would fire on that item.
        """
        return self.tr1.evaluate(story) and self.tr2.evaluate(story)
        
# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        """
        Initializes the OrTrigger object.
        
        trigger1 (Trigger): Trigger with its required phrase input
        trigger2 (Trigger): Trigger with its required phrase input
        """
        self.tr1 = trigger1
        self.tr2 = trigger2
        
    def evaluate(self, story):
        """
        True on a news story only if either or both of the inputted triggers 
        would fire on that item.
        """
        return self.tr1.evaluate(story) or self.tr2.evaluate(story)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    
    stories_filtered = [] #empty list
    for News in stories: #loops accross stories
        for trigger in triggerlist: #loops across triggers
            if trigger.evaluate(News): #if trigger is true
                stories_filtered += [News] #add the news to stories_filtered
    return stories_filtered



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
             file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    # print(lines) # for now, print it so you see what it contains!
    
    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    
    Dict = {'TITLE':TitleTrigger,'DESCRIPTION':DescriptionTrigger,
            'AFTER':AfterTrigger, 'BEFORE':BeforeTrigger, 'NOT':NotTrigger,
            'AND':AndTrigger, 'OR':OrTrigger} #Dictionary of functions that 
    # contains the key-word as key and the function name as value
    lines = []
    for line in lines: #for each line in list of lines
        WORDS = line.split(',') #slpiting each line into WORDS
        if WORDS[0] == 'ADD': #if the first WORD of a line is ADD
            trigger_list =  [] #create empty list
            for trig in WORDS[1:]: #for every trigger after the first WORD in line
                trigger_list += [vars()[trig]] # add to the list the varible 
                                               # with the name [trigger]
        elif len(WORDS) == 3: # else if if the line has 3 WORDS
            vars()[WORDS[0]] = Dict[WORDS[1]](WORDS[-1]) # Create a variable 
            # with the name [first word of line] that equals the desirded function 
            # using the last WORD of line as input 
        elif len(WORDS) == 4: # else if if the line has 4 WORDS
            vars()[WORDS[0]] = Dict[WORDS[1]](vars()[WORDS[-2]],vars()[WORDS[-1]])
            # Create a variable with the name [first word of line] that equals
            # the desirded function, using the variable names that equal 
            # the last two WORDS of line as input 
    return trigger_list 

    


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        # t1 = TitleTrigger("quarantine")
        # t2 = DescriptionTrigger("Trump")
        # t3 = DescriptionTrigger("Coronavirus")
        # t4 = AndTrigger(t2, t3)
        # triggerlist = [t1, t2, t3, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            #stories = process("http://news.google.com/news?output=rss")
            
            # Above link did't exist so this had to be modified to a link 
            # with an alert in google news
            
            stories = process("https://www.google.com/alerts/feeds/13733568432893098323/179015996560301352")
            

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

# MAKE SURE TO RESTART KERNELL EVERY TIME YOU RUN THE CODE!!!!!!