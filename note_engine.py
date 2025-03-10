from llama_index.tools import FunctionTool
import os

note_file = os.path.join("data", "notes.txt")

def save_note(note):
    if not os.path.exists(note_file):
        open(note_file, "w") #w for writing mode

    with open(note_file, "a") as f:
        f.writelines([note + "\n"]) #a for append mode -> adding new note at the end of the file

    return "note saved"

#putting the note function into a tool (?)
note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="this tool can save a text based note to a file for the user"
)