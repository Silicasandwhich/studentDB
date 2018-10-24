from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class StudentListButton(ListItemButton):
    pass


class StudentDB(BoxLayout):
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_list = ObjectProperty()

    def submit_students(self):
        # Get the student information
        student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
        # Add to ListView
        self.student_list.adapter.data.extend([student_name])
        # Reset the ListView
        # noinspection PyProtectedMember
        self.student_list._trigger_reset_populate()

    def delete_students(self):
        # make sure student is selected
        if self.student_list.adapter.selection:
            # get text from item selected
            selection = self.student_list.adapter.selection[0].text
            # Remove the student
            self.student_list.adapter.data.remove(selection)
            # Reset the ListView
            self.student_list._trigger_reset_populate()
    def replace_students(self):
        # make sure student is selected
        if self.student_list.adapter.selection:
            # get text from item selected
            selection = self.student_list.adapter.selection[0].text
            # Remove the student
            self.student_list.adapter.data.remove(selection)
            # Get student information
            student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
            # Add updated data to listView
            self.student_list.adapter.data.extend([student_name])
            # Reset the ListView
            self.student_list._trigger_reset_populate()


class StudentDBApp(App):
    def build(self):
        return StudentDB()


dbApp = StudentDBApp()
dbApp.run()
