from xml.etree.ElementTree import fromstring
import xmltodict
import json
import os
import tempfile


class Soundpad:
    def __init__(self):
        self.pipe = None
        self.pipe_name = "sp_remote_control"
        self.tmp_file = os.path.join(tempfile.gettempdir(), "soundpad_query.txt")

    def _init_connection(self):
        if not self.pipe:
            try:
                self.pipe = open(rf"\\.\pipe\{self.pipe_name}", "r+b", buffering=0)
            except Exception as e:
                print(f"Error opening pipe: {e}")
                self.pipe = None

    def _close_connection(self):
        if self.pipe:
            try:
                self.pipe.close()
            except Exception:
                pass
            finally:
                self.pipe = None

    def send_command(self, command):
        self._init_connection()
        try:
            self.pipe.write(command.encode())
            self.pipe.seek(0)
            data = self.pipe.read(16384)
            self.pipe.seek(0)
            return data
        except Exception as e:
            print(f"Error sending command: {e}")
            return None

    def categories(self):
        data = self.send_command("GetCategories(false, false)")
        if not data:
            return json.dumps([])
        cat_dict = {}
        myxml = fromstring(data)
        for cat in myxml:
            if "All sounds" not in cat.attrib["name"]:
                cat_dict[cat.attrib["index"]] = cat.attrib["name"]
        return cat_dict

    def category_sounds(self, category_id):
        data = self.send_command(f"GetCategory({category_id},true,false)")
        if not data:
            return json.dumps([])
        my_xml = data.decode("utf-8")
        my_dict = xmltodict.parse(my_xml)
        sound_dict = {}
        for sound in my_dict["Categories"]["Category"]["Sound"]:
            sound_dict[sound["@index"]] = sound["@title"]
        return sound_dict

    def sound_play(self, sound_id):
        self.send_command(f"DoPlaySound({sound_id})")

    def sound_stop(self):
        self.send_command("DoStopSound()")

    def query_sounds(self, search_string: str) -> dict:
        all_sounds = {
            sid: sname
            for cat_id in self.categories()
            for sid, sname in self.category_sounds(cat_id).items()
        }

        search_results = {
            sid: sname
            for sid, sname in all_sounds.items()
            if search_string.lower() in sname.lower()
        }

        return search_results

    def query_id_set(self, sound_id: str) -> None:
        # write the id to a temp file (windows)
        with open(self.tmp_file, "w") as file:
            file.write(sound_id)

    def query_id_get(self) -> str:
        # read the id from a temp file (windows)
        with open(self.tmp_file, "r") as file:
            return file.read().strip()

    def query_play(self, id: str) -> None:
        self.sound_play(id)
