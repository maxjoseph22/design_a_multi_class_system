import re

class Diary():

    def __init__(self):
        self.diary_entries = []
        self.to_do_list = []

    def add_to_diary(self, entry):
        self.diary_entries.append(entry)

    def all_diary_entries(self):
        return self.diary_entries
    
    def add_to_do(self, todo):
        self.to_do_list.append(todo)

    def incomplete(self):
        incomplete_list =[]
        for todo in self.to_do_list:
            if todo.complete == False:
                incomplete_list.append(todo)
        return incomplete_list
    
    def complete(self):
        complete_list =[]
        for todo in self.to_do_list:
            if todo.complete == True:
                complete_list.append(todo)
        return complete_list

    def give_up(self):
        for todo in self.to_do_list:
                todo.complete = True

    def find_best_entry_for_reading_time(self, wpm, minutes):
        readable_entry_list = []
        max_number_of_words = wpm * minutes

        for entry in self.diary_entries:
            if len(entry.entry.split()) <= max_number_of_words:
                readable_entry_list.append(entry)
        if len(readable_entry_list) == 0:
            return None        
        if len(readable_entry_list) > 0:
            sorted_list = sorted(readable_entry_list, key=lambda x: len(x.entry.split()))
        return sorted_list[-1]
    
    def phone_numbers(self):
        phone_number_list = []
        for entry in self.diary_entries:
            phone_number_list += re.findall(r'[0-9]+', entry.entry)
        return phone_number_list
        

class DiaryEntry:

    def __init__(self, entry):
        self.entry = entry
        self.words_read_count = 0
    

    def count_words(self):
        return len(self.entry.split())

    def reading_time(self, wpm):
        number_of_words = len(self.entry.split())
        number_of_minutes = (number_of_words // wpm)
        number_of_seconds = int((number_of_words / wpm) * 60)
        if number_of_minutes == 1:
            return str(number_of_minutes) + " minute " + str((number_of_seconds) - number_of_minutes * 60) + " seconds"
        elif number_of_minutes == 0:
            return str(number_of_seconds) + " seconds"
        elif number_of_minutes > 1:
            return str(number_of_minutes) + " minutes " + str((number_of_seconds) - number_of_minutes * 60) + " seconds"


    def reading_chunk(self, wpm, minutes):
        words_to_read = wpm * minutes
        passage = " ".join((self.entry.split()[self.words_read_count:words_to_read + self.words_read_count]))
        self.words_read_count += words_to_read
        if self.words_read_count >= len(self.entry.split()):
            self.words_read_count = 0
        return passage

class Todo:

    def __init__(self, task):
        self.task = task
        self.complete = False

    def mark_complete(self):
        self.complete = True


