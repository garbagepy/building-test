import os
import random
from flet import *

# Constants for colors
BG = '#041955'
FWG = '#97b4ff'
FG = '#3450a1'
PINK = '#eb06ff'

# Global variable to keep track of the selected village / switch
selected_village = None
active_switch_index = 0

# Main UI Function
def main(page: Page):
    global selected_village, switches

    if not os.path.exists("vocabulary_database"):
        os.makedirs("vocabulary_database")

    # Circular Avatar
    circle = Stack(
        controls=[
            Container(width=100, height=100, border_radius=50, bgcolor='white12'),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=['#00000000', PINK],
                ),
                width=100,
                height=100,
                border_radius=50,
                content=Container(
                    padding=padding.all(5),
                    bgcolor=BG,
                    width=90,
                    height=90,
                    border_radius=50,
                    content=CircleAvatar(
                        opacity=0.8,
                        foreground_image_url=""
                    )
                )
            ),
        ]
    )

    # Initialize switches
    switches = []

    def switch_changed(e, idx):
        global active_switch_index
        for i, switch in enumerate(switches):
            switch.value = (i == idx)
        active_switch_index = idx
        page.update()

    # Create switches with explicit labels
    switches.append(Switch(
        value=(active_switch_index == 0),
        label="In Order (OG -> Trans)",
        label_style=TextStyle(color=colors.WHITE),
        active_color="#757575",
        thumb_color="#BDBDBD",
        on_change=lambda e: switch_changed(e, 0)
    ))
    switches.append(Switch(
        value=(active_switch_index == 1),
        label="Reverse Order (OG -> Trans)",
        label_style=TextStyle(color=colors.WHITE),
        active_color="#757575",
        thumb_color="#BDBDBD",
        on_change=lambda e: switch_changed(e, 1)
    ))
    switches.append(Switch(
        value=(active_switch_index == 2),
        label="Random (OG -> Trans)",
        label_style=TextStyle(color=colors.WHITE),
        active_color="#757575",
        thumb_color="#BDBDBD",
        on_change=lambda e: switch_changed(e, 2)
    ))
    switches.append(Switch(
        value=(active_switch_index == 3),
        label="In Order (Trans -> OG)",
        label_style=TextStyle(color=colors.WHITE),
        active_color="#757575",
        thumb_color="#BDBDBD",
        on_change=lambda e: switch_changed(e, 3)
    ))
    switches.append(Switch(
        value=(active_switch_index == 4),
        label="Reverse Order (Trans -> OG)",
        label_style=TextStyle(color=colors.WHITE),
        active_color="#757575",
        thumb_color="#BDBDBD",
        on_change=lambda e: switch_changed(e, 4)
    ))
    switches.append(Switch(
        value=(active_switch_index == 5),
        label="Random (Trans -> OG)",
        label_style=TextStyle(color=colors.WHITE),
        active_color="#757575",
        thumb_color="#BDBDBD",
        on_change=lambda e: switch_changed(e, 5)
    ))
    switches.append(Switch(
        value=(active_switch_index == 6),
        label="Random (Both Languages)",
        label_style=TextStyle(color=colors.WHITE),
        active_color="#757575",
        thumb_color="#BDBDBD",
        on_change=lambda e: switch_changed(e, 6)
    ))



    # Function to load villages from files
    def load_villages():
        villages = []
        for filename in os.listdir("vocabulary_database"):
            if filename.endswith(".txt"):
                file_path = os.path.join("vocabulary_database", filename)
                with open(file_path, "r") as file:
                    lines = file.readlines()

                    # Ensure we have at least 3 lines (village details)
                    if len(lines) >= 3:
                        try:
                            village_name = lines[0].split("Village Name: ")[1].strip()
                            original_language = lines[1].split("Original Language: ")[1].strip()
                            goal_language = lines[2].split("Goal Language: ")[1].strip()
                            villages.append((village_name, original_language, goal_language))
                        except IndexError:
                            print(f"Error parsing file {filename}. Ensure it follows the correct format.")
                    else:
                        print(f"File {filename} does not have enough lines to parse.")
        return villages

    def load_vocabulary_mode_0():  # Original Order
        global active_switch_index
        if active_switch_index == 0:
            file_path = os.path.join("vocabulary_database", f"{selected_village}.txt")
            vocab_list = []
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    lines = file.readlines()
                    for line in lines[3:]:  # Skip the first 3 lines (village details)
                        if ':' in line:
                            try:
                                vocab, translation, count = line.strip().split(":", 2)
                                vocab_list.append({"vocab": vocab, "translation": translation, "count": count})
                            except ValueError:
                                print(f"Error parsing line: {line.strip()}")
            # Print the success message
            print("vocab mode 0 successfully loaded")
            return vocab_list
        else:
            return []

    def load_vocabulary_mode_1():  # Reverse Order
        global active_switch_index
        if active_switch_index == 1:
            file_path = os.path.join("vocabulary_database", f"{selected_village}.txt")
            vocab_list = []
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    lines = file.readlines()
                    for line in lines[3:]:  # Skip the first 3 lines (village details)
                        if ':' in line:
                            try:
                                vocab, translation, count = line.strip().split(":", 2)
                                vocab_list.append({"vocab": vocab, "translation": translation, "count": count})
                            except ValueError:
                                print(f"Error parsing line: {line.strip()}")
                # Reverse the vocab_list to have last vocabulary pair first
                vocab_list.reverse()
            # Print the success message
            print("vocab mode 1 successfully loaded")
            return vocab_list
        else:
            return []

    def load_vocabulary_mode_2():  # Random Order
        global active_switch_index
        if active_switch_index == 2:
            file_path = os.path.join("vocabulary_database", f"{selected_village}.txt")
            vocab_list = []
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    lines = file.readlines()
                    for line in lines[3:]:
                        if ':' in line:
                            try:
                                vocab, translation, count = line.strip().split(":", 2)
                                vocab_list.append({"vocab": vocab, "translation": translation, "count": count})
                            except ValueError:
                                print(f"Error parsing line: {line.strip()}")
                # Shuffle the vocab_list to randomize the order
                random.shuffle(vocab_list)
            # Print the success message
            print("vocab mode 2 successfully loaded")
            return vocab_list
        else:
            return []

    def load_vocabulary_mode_3():  # Swapped Order (translation - vocabulary)
        global active_switch_index
        if active_switch_index == 3:
            file_path = os.path.join("vocabulary_database", f"{selected_village}.txt")
            vocab_list = []
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    lines = file.readlines()
                    for line in lines[3:]:
                        if ':' in line:
                            try:
                                vocab, translation, count = line.strip().split(":", 2)
                                # Swap vocab and translation for this mode
                                vocab_list.append({"vocab": translation, "translation": vocab, "count": count})
                            except ValueError:
                                print(f"Error parsing line: {line.strip()}")
                # Shuffle the vocab_list to randomize the order
                random.shuffle(vocab_list)
            # Print the success message
            print("vocab mode 3 successfully loaded")
            return vocab_list
        else:
            return []

    def load_vocabulary_mode_4():   #Reverse Order (Trans -> OG)
        global active_switch_index
        if active_switch_index == 4:  # Adjust this condition to match the mode
            file_path = os.path.join("vocabulary_database", f"{selected_village}.txt")
            vocab_list = []
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    lines = file.readlines()
                    for line in lines[3:]:  # Skip the first 3 lines (village details)
                        if ':' in line:
                            try:
                                vocab, translation, count = line.strip().split(":", 2)
                                # Swap vocab and translation
                                vocab_list.append({"vocab": translation, "translation": vocab, "count": count})
                            except ValueError:
                                print(f"Error parsing line: {line.strip()}")
                # Reverse the vocab_list to have the last vocabulary pair first
                vocab_list.reverse()
            # Print the success message
            print("vocab mode 4 successfully loaded")
            return vocab_list
        else:
            return []

    def load_vocabulary_mode_5():   #Random (Trans -> OG)
        global active_switch_index
        if active_switch_index == 5:  # Adjust this condition to match the mode
            file_path = os.path.join("vocabulary_database", f"{selected_village}.txt")
            vocab_list = []
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    lines = file.readlines()
                    for line in lines[3:]:  # Skip the first 3 lines (village details)
                        if ':' in line:
                            try:
                                vocab, translation, count = line.strip().split(":", 2)
                                # Swap vocab and translation
                                vocab_list.append({"vocab": translation, "translation": vocab, "count": count})
                            except ValueError:
                                print(f"Error parsing line: {line.strip()}")
                # Shuffle the vocab_list to randomize the order
                random.shuffle(vocab_list)
            # Print the success message
            print("vocab mode 5 successfully loaded")
            return vocab_list
        else:
            return []

    def load_vocabulary_mode_6():   # Completly Random (Anarchy!)
        global active_switch_index
        if active_switch_index == 6:
            file_path = os.path.join("vocabulary_database", f"{selected_village}.txt")
            vocab_list = []
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    lines = file.readlines()
                    for line in lines[3:]:
                        if ':' in line:
                            try:
                                vocab, translation, count = line.strip().split(":", 2)
                                if random.choice([True, False]):
                                    vocab_list.append({"vocab": vocab, "translation": translation, "count": count})
                                else:
                                    vocab_list.append({"vocab": translation, "translation": vocab, "count": count})
                            except ValueError:
                                print(f"Error parsing line: {line.strip()}")
                # Shuffle the vocab_list to randomize the order
                random.shuffle(vocab_list)
            # Print the success message
            print("vocab mode 6 successfully loaded")
            return vocab_list
        else:
            return []

    # Function to update categories card
    def update_categories_card():
        categories_card.controls.clear()
        villages = load_villages()
        for village_name, original_language, goal_language in villages:
            categories_card.controls.append(
                Container(
                    border_radius=20,
                    bgcolor=BG,
                    width=200,
                    height=160,
                    padding=15,
                    content=Column(
                        controls=[
                            Text(village_name, size=22, weight="bold",color="white"),
                            Text(f"{original_language}\n-\n{goal_language}",color="white"),
                            Container(
                                width=160,
                                height=5,
                                bgcolor="white12",
                                border_radius=20,
                                content=Container(bgcolor=PINK)
                            )
                        ]
                    ),
                    on_click=lambda e, vn=village_name: village_clicked(vn)  # Pass village_name to the click handler
                )
            )
        page.update()

    # Function to handle clicking on a village
    def village_clicked(village_name):
        global selected_village
        selected_village = village_name
        print(f"Currently active switch index: {active_switch_index}")  # Print the index of the active switch
        page.go("/village_options")

    # Function to handle deleting a village
    def delete_village(village_name):
        file_path = os.path.join("vocabulary_database", f"{village_name}.txt")
        if os.path.exists(file_path):
            os.remove(file_path)
            update_categories_card()
            page.go("/")
        else:
            print("Village not found!")

    # Function to display village options
    def village_options_page():
        if selected_village:
            villages = load_villages()
            village_details = next((v for v in villages if v[0] == selected_village), None)
            if village_details:
                village_name, original_language, goal_language = village_details
            else:
                village_name = "Unknown"
                original_language = "Unknown"
                goal_language = "Unknown"
        else:
            village_name = "No Village Selected"
            original_language = "N/A"
            goal_language = "N/A"

        return Container(
            padding=padding.all(20),
            width=400,
            height=900,
            bgcolor=FG,
            border_radius=20,
            content=Column(
                controls=[
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            Container(on_click=lambda _: page.go("/"), content=Text("Back",color="white", size=20)),
                            Container(padding=padding.only(top=20), content=Text("Village Options",color="white", size=32, weight="bold"))
                        ]
                    ),
                    Container(height=20,),
                    Text(f"Village Name: {village_name}",color="white", size=24),
                    Text(f"Original Language: {original_language}",color="white", size=20),
                    Text(f"Goal Language: {goal_language}",color="white", size=20),
                    Container(height=30),
                    ElevatedButton(text="Learn",bgcolor="black",color="white", on_click=lambda _: page.go("/learning_page")),
                    ElevatedButton(text="Add Vocabulary",bgcolor="black",color="white", on_click=lambda _: page.go("/add_vocab")),
                    ElevatedButton(text="Edit Vocabulary",bgcolor="black",color="white", on_click=lambda _: page.go("/vocabulary_database")),
                    ElevatedButton(text="Delete Village",bgcolor="black",color="white", on_click=lambda _: delete_village(selected_village))
                ]
            )
        )

    # Inputs for add_vocab_page
    original_vocab_input = TextField(label="V1", border_color=PINK)
    goal_vocab_input = TextField(label="V2", border_color=PINK)

    def add_vocab_page():
        vocab_vocab_input = TextField(label="Vocabulary",color="white", border_color=PINK)
        goal_vocab_input = TextField(label="Translation",color="white", border_color=PINK)

        def save_vocabulary(e):
            vocabulary_word = vocab_vocab_input.value
            translation_word = goal_vocab_input.value

            if vocabulary_word and translation_word and selected_village:
                file_path = os.path.join("vocabulary_database", f"{selected_village}.txt")

                # Append the new vocabulary, translation, and the number 5 to the village's file
                with open(file_path, "a") as file:
                    file.write(f"{vocabulary_word}:{translation_word}:5\n")

                # Clear the input fields after saving
                vocab_vocab_input.value = ""
                goal_vocab_input.value = ""
                page.update()

                # Optionally, navigate back to the village options page
                page.go("/village_options")
            else:
                print("Please enter both vocabulary and translation.")

        return Container(
            padding=padding.all(20),
            width=400,
            height=900,
            bgcolor=FG,
            border_radius=20,
            content=Column(
                controls=[
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            Container(on_click=lambda _: page.go("/village_options"), content=Text("Back",color="white", size=20)),
                            Container(padding=padding.only(top=20),
                                      content=Text("Add Vocabulary",color="white", size=32, weight="bold"))
                        ]
                    ),
                    Container(height=20),
                    Text("Add new vocabulary to your village",color="white", size=24),
                    Container(height=20),
                    vocab_vocab_input,  # Input for vocabulary word
                    Container(height=20),
                    goal_vocab_input,  # Input for translation
                    Container(height=30),
                    ElevatedButton(text="Save Vocabulary",bgcolor="black",color="white", on_click=save_vocabulary)  # Save button with functionality
                ]
            )
        )

    def learning_page():
        # Create a Text control to display the vocabulary word to translate
        learning_page_text_control = Text("Loading Failed!", size=30, weight="bold", color="white")

        # Create a TextField for user input
        answer_input = TextField(label="Translation", border_color=PINK, width=400)

        # Create a Text control for feedback
        feedback_text_control = Text("", size=20, weight="bold", color="white")

        # Load vocabulary for learning
        vocab_list = []
        if active_switch_index == 0:
            vocab_list = load_vocabulary_mode_0()
        elif active_switch_index == 1:
            vocab_list = load_vocabulary_mode_1()
        elif active_switch_index == 2:
            vocab_list = load_vocabulary_mode_2()
        elif active_switch_index == 3:
            vocab_list = load_vocabulary_mode_3()
        elif active_switch_index == 4:
            vocab_list = load_vocabulary_mode_4()
        elif active_switch_index == 5:
            vocab_list = load_vocabulary_mode_5()
        elif active_switch_index == 6:
            vocab_list = load_vocabulary_mode_6()

        current_vocab_index = 0

        if vocab_list:
            first_vocab = vocab_list[current_vocab_index]['vocab']
            learning_page_text_control.value = first_vocab

        # Function to handle the Confirm button click
        def confirm_answer(e):
            nonlocal current_vocab_index
            answer = answer_input.value
            if answer:
                correct_translation = vocab_list[current_vocab_index]['translation']
                if answer.lower().strip() == correct_translation.lower().strip():
                    feedback_text_control.value = "Correct :)"
                    current_vocab_index += 1
                    if current_vocab_index < len(vocab_list):
                        # Load the next vocab word
                        next_vocab = vocab_list[current_vocab_index]['vocab']
                        learning_page_text_control.value = next_vocab
                        answer_input.value = ""  # Clear the input field
                    else:
                        feedback_text_control.value = "You've completed all words!"
                        learning_page_text_control.value = ""
                        answer_input.visible = False  # Hide the input field after finishing
                else:
                    feedback_text_control.value = vocab_list[current_vocab_index]['translation']

                page.update()  # Refresh the page to reflect the changes
            else:
                print("Please enter an answer.")

        return Container(
            padding=padding.all(20),
            width=400,
            height=900,
            bgcolor=FG,
            border_radius=20,
            content=Column(
                controls=[
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            Container(on_click=lambda _: page.go("/village_options"),
                                      content=Text("Back", color="white", size=20)),
                            Container(padding=padding.only(top=20),
                                      content=Text("Learning Page", color="white", size=32, weight="bold"))
                        ]
                    ),
                    Container(
                        height=150,
                        width=400,
                        bgcolor=BG,
                        border_radius=15,
                        padding=padding.all(10),
                        content=learning_page_text_control  # Display the vocabulary word here
                    ),
                    Container(content=answer_input),
                    Container(
                        height=75,
                        width=400,
                        bgcolor=BG,
                        border_radius=15,
                        padding=padding.all(10),
                        content=feedback_text_control  # Display the feedback here
                    ),
                    Container(height=30),
                    ElevatedButton(
                        text="Confirm",
                        on_click=confirm_answer,
                        bgcolor="black",
                        color="white",
                        width=200
                    )
                ]
            )
        )

    def vocabulary_database_page():
        # Function to load the vocabulary data from the file
        def load_vocabulary():
            global original_language, goal_language  # Ensure these are global
            vocab_list = []
            original_language = ""
            goal_language = ""
            if selected_village:
                file_path = os.path.join("vocabulary_database", f"{selected_village}.txt")
                if os.path.exists(file_path):
                    with open(file_path, "r") as file:
                        lines = file.readlines()
                        original_language = lines[1].split(":")[1].strip()  # Extract original language
                        goal_language = lines[2].split(":")[1].strip()  # Extract goal language
                        for line in lines[3:]:  # Skip the first 3 lines (village details)
                            if ':' in line:
                                try:
                                    vocab, translation, count = line.strip().split(":", 2)
                                    vocab_list.append({"vocab": vocab, "translation": translation, "count": count})
                                except ValueError:
                                    print(f"Error parsing line: {line.strip()}")
            return vocab_list, original_language, goal_language

        vocab_list, original_language, goal_language = load_vocabulary()

        def add_empty_vocab(e):
            vocab_list.append({"vocab": "", "translation": "", "count": "5"})
            update_vocabulary_table()

        # Function to update the vocabulary list with current values from the TextField controls
        def update_vocab_list():
            for i, row in enumerate(vocab_table.controls):
                vocab_list[i]["vocab"] = row.controls[0].value
                vocab_list[i]["translation"] = row.controls[1].value
                vocab_list[i]["count"] = row.controls[2].value

        # Function to delete a vocabulary entry
        def delete_vocab(index):
            if 0 <= index < len(vocab_list):
                del vocab_list[index]
                update_vocabulary_table()
                save_changes(None)  # Save changes to the file after deletion

        # Function to update the vocabulary table display
        def update_vocabulary_table():
            vocab_table.controls.clear()
            for i, item in enumerate(vocab_list):
                vocab_table.controls.append(
                    Row(
                        controls=[
                            TextField(value=item["vocab"], label="Vocabulary", expand=True),
                            TextField(value=item["translation"], label="Translation", expand=True),
                            TextField(value=item["count"], label="+", width=45),
                            ElevatedButton(text="Delete",bgcolor="black",color="white", on_click=lambda e, idx=i: delete_vocab(idx))
                        ]
                    )
                )
            page.update()

        # Function to save changes to the vocabulary file
        def save_changes(e):
            update_vocab_list()  # Ensure the vocab_list is updated with current TextField values

            # Update the original and goal languages based on the current inputs
            global original_language, goal_language  # Ensure these are the global variables
            original_language = original_language_input.value
            goal_language = goal_language_input.value

            if selected_village:
                file_path = os.path.join("vocabulary_database", f"{selected_village}.txt")
                with open(file_path, "w") as file:
                    # Write the village details (assuming these are the first 3 lines)
                    file.write(f"Village Name: {selected_village}\n")
                    file.write(f"Original Language: {original_language}\n")
                    file.write(f"Goal Language: {goal_language}\n")
                    # Write the vocabulary items with their updated values
                    for item in vocab_list:
                        file.write(f"{item['vocab']}:{item['translation']}:{item['count']}\n")

            # After saving, reload the language fields to ensure UI shows the latest data
            original_language_input.value = original_language
            goal_language_input.value = goal_language

            page.update()  # Refresh the page to reflect the changes

        # Initialize the vocab_table with the existing vocabulary list
        vocab_table = Column(
            controls=[
                Row(
                    controls=[
                        TextField(value=item["vocab"], label="Vocabulary", expand=True),
                        TextField(value=item["translation"], label="Translation", expand=True),
                        TextField(value=item["count"], label="Count", expand=True),
                        ElevatedButton(text="Delete",bgcolor="black",color="white", on_click=lambda e, idx=i: delete_vocab(idx))
                    ]
                )
                for i, item in enumerate(vocab_list)
            ],
            spacing=10,
            scroll="auto",
            height=265
        )

        # UI for original and goal languages
        original_language_input = TextField(value=original_language, label="Original Language")
        goal_language_input = TextField(value=goal_language, label="Goal Language")

        # Initial update of the vocabulary table
        update_vocabulary_table()

        return Container(
            padding=padding.all(20),
            width=400,
            height=900,
            bgcolor=FG,
            border_radius=20,
            content=Column(
                controls=[
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            Container(on_click=lambda _: page.go("/village_options"), content=Text("Back",color="white", size=20)),
                            Container(padding=padding.only(top=20),
                                      content=Text("Vocabulary Database",color="white", size=32, weight="bold")),
                        ]
                    ),
                    original_language_input,
                    goal_language_input,
                    Container(height=20),
                    vocab_table,  # Display the vocabulary list as an editable table
                    Container(height=40),
                    ElevatedButton(text="Add New Vocabulary",bgcolor="black",color="white", on_click=add_empty_vocab),  # Button to add new vocab
                    ElevatedButton(text="Save Changes",bgcolor="black",color="white", on_click=save_changes)  # Button to save changes
                ]
            )
        )

        # Function to handle editing a village
    def edit_village_page(village_name):
        # Define the input fields for editing
        edit_village_name_input = TextField(label="New Village Name", border_color=PINK, value=village_name)
        edit_original_language_input = TextField(label="Original Language",color="white", border_color=PINK)
        edit_goal_language_input = TextField(label="Goal Language",color="white", border_color=PINK)

        # Function to handle saving the edited village details
        def save_edits(e):
            new_name = edit_village_name_input.value
            new_original_language = edit_original_language_input.value
            new_goal_language = edit_goal_language_input.value

            if new_name and new_original_language and new_goal_language:
                old_file_path = os.path.join("vocabulary_database", f"{village_name}.txt")
                new_file_path = os.path.join("vocabulary_database", f"{new_name}.txt")

                if village_name != new_name and os.path.exists(new_file_path):
                    print("A village with this name already exists!")
                    return

                # Save the new details
                with open(new_file_path, "w") as file:
                    file.write(f"Village Name: {new_name}\n")
                    file.write(f"Original Language: {new_original_language}\n")
                    file.write(f"Goal Language: {new_goal_language}\n")

                if village_name != new_name:
                    os.remove(old_file_path)

                page.go("/")
                page.update()

        return Container(
            padding=padding.all(20),
            width=400,
            height=900,
            bgcolor=FG,
            border_radius=20,
            content=Column(
                controls=[
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            Container(on_click=lambda _: page.go("/"), content=Text("Back",color="white", size=20)),
                            Container(padding=padding.only(top=20),
                                      content=Text(f"Edit Village: {village_name}", size=32, weight="bold"))
                        ]
                    ),
                    Container(height=20),
                    edit_village_name_input,
                    Container(height=20),
                    edit_original_language_input,
                    Container(height=20),
                    edit_goal_language_input,
                    Container(height=30),
                    ElevatedButton(text="Save Changes",bgcolor="black",color="white", on_click=save_edits)
                ]
            )
        )
    # Sidebar shrink/maximize functions
    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(0.8, alignment=alignment.center_right)
        page_2.controls[0].border_radius = border_radius.only(top_left=35, top_right=0, bottom_left=35, bottom_right=0)
        page_2.update()

    def maximize(e):
        page_2.controls[0].width = 400
        page_2.controls[0].scale = transform.Scale(1, alignment=alignment.center_right)
        page_2.update()

    # Category card container
    categories_card = Row(scroll="auto")
    update_categories_card()

    # Inputs for creating a new village
    village_name_input = TextField(label="Village Name",color="white", border_color=PINK)
    original_language_input = TextField(label="Original Language",color="white", border_color=PINK)
    goal_language_input = TextField(label="Goal Language",color="white", border_color=PINK)

    # Function to create a new village
    def create_village(e):
        village_name = village_name_input.value
        original_language = original_language_input.value
        goal_language = goal_language_input.value

        if village_name and original_language and goal_language:
            file_path = os.path.join("vocabulary_database", f"{village_name}.txt")
            counter = 1
            while os.path.exists(file_path):
                file_path = os.path.join("vocabulary_database", f"{village_name}_{counter}.txt")
                counter += 1

            with open(file_path, "w") as file:
                file.write(f"Village Name: {village_name}\n")
                file.write(f"Original Language: {original_language}\n")
                file.write(f"Goal Language: {goal_language}\n")

            village_name_input.value = ""
            original_language_input.value = ""
            goal_language_input.value = ""

            update_categories_card()
            page.go("/")
        else:
            print("Please fill in all fields!")

    # Create village view
    create_village_view = Container(
        content=Column(
            controls=[
                Row(
                    alignment="spaceBetween",
                    controls=[
                        Container(on_click=lambda _: page.go("/"), content=Text("X",bgcolor="black",color="white", size=60)),
                        Container(padding=padding.only(top=20), content=Text("Create a Village", size=32, weight="bold",color="white"))
                    ]
                ),
                Container(height=20),
                village_name_input,
                Container(height=20),
                original_language_input,
                Container(height=20),
                goal_language_input,
                Container(height=30),
                ElevatedButton(text="Create",bgcolor="black",color="white", on_click=create_village)
            ]
        ),
        padding=padding.all(20),
        width=400,
        height=900,
        bgcolor=FG,
        border_radius=20
    )

    # First page content
    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment='spaceBetween',
                    controls=[
                        Container(on_click=shrink, content=Icon(icons.MENU, color="white")),
                        Row(controls=[Icon(icons.SEARCH, color="white"),
                                      Icon(icons.NOTIFICATIONS_OUTLINED, color="white")])
                    ]
                ),
                Text("Hey, what's up?",color="white"),
                Text("Your Villages",color="white"),
                Container(padding=padding.only(top=10, bottom=20), content=categories_card),
                Text("LEARNING MODE",color="white"),
                Column(controls=switches),
                Stack(
                    controls=[
                        FloatingActionButton(
                            bottom=20,  # Adjusted to 20 for better visibility
                            left=20,  # Adjusted to left for bottom-left positioning
                            content=Icon(icons.ADD, color="white"),
                            bgcolor="#32a8a6",
                            on_click=lambda _: page.go('/create_village'))
                    ]
                )
            ]
        )
    )
    # Sidebar (Page 1)
    page_1 = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(left=50, top=60, right=200),
        content=Column(
            controls=[
                Row(
                    alignment="end",
                    controls=[
                        Container(
                            border_radius=25,
                            padding=padding.only(top=13, left=13),
                            height=50,
                            width=50,
                            border=border.all(color="white", width=1),
                            on_click=maximize,
                            content=Text("<",color="white")
                        )
                    ]
                ),
                Container(height=20),
                circle,
                Text("Username",color="white", size=24, weight="bold"),
                Container(height=20),
                Row(controls=[Icon(icons.FAVORITE_BORDER_SHARP, color="white"), Text("Heart1",color="white", size=15)]),
                Row(controls=[Icon(icons.CARD_TRAVEL, color="white"), Text("Heart2",color="white", size=15)]),
                Row(controls=[Icon(icons.CALCULATE_OUTLINED, color="white"), Text("Heart3",color="white", size=15)])
            ]
        )
    )

    # Main content area (Page 2)
    page_2 = Row(
        alignment="end",
        controls=[
            Container(
                width=400,
                height=853,
                bgcolor=FG,
                border_radius=35,
                animate=animation.Animation(600, AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400, curve="decelerate"),
                padding=padding.only(top=40, left=20, right=20, bottom=10),
                content=Stack(
                    controls=[
                        Column(controls=[first_page_contents]),  # Main content
                        FloatingActionButton(
                            bottom=20,  # Position from the bottom
                            right=20,  # Position from the left
                            icon=icons.ADD,
                            on_click=lambda _: page.go('/create_village')
                        )
                    ]
                )
            )
        ]
    )

    # Main container combining Page 1 and Page 2
    container = Container(
        width=400,
        height=900,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(top=25, bottom=10),
        content=Stack(controls=[page_1, page_2])
    )

    # Define the app's routing system
    pages = {
        "/": View("/", [container]),
        "/create_village": View("/create_village", [create_village_view]),
        "/village_options": lambda: View("/village_options", [village_options_page()]),
        "/edit_village/{village_name}": lambda: View(f"/edit_village/{selected_village}",
                                                     [edit_village_page(selected_village)]),
        "/add_vocab": lambda: View("/add_vocab", [add_vocab_page()]),
        "/vocabulary_database": lambda: View("/vocabulary_database", [vocabulary_database_page()]),
        "/learning_page": lambda: View("/learning_page", [learning_page()]),  # Added route for the learning page
    }

    # Function to handle route changes
    def route_change(event):
        route = event.route
        page.views.clear()
        if route in pages:
            if callable(pages[route]):
                page.views.append(pages[route]())  # Call the function to generate the View
            else:
                page.views.append(pages[route])
        else:
            page.views.append(pages["/"])

        if route == "/":
            update_categories_card()  # Ensure the categories card is updated each time "/' is opened

        page.update()

    # Bind the route change function and navigate to the current route
    page.on_route_change = route_change
    page.go(page.route)

# Run the app
app(target=main)
