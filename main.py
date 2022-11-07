import eel
from jinja2 import Template
import os
from pygame import mixer

eel.init("web", (".html", ".js"))
mixer.init()


def Jinja_templates(base_file, file_name, musics):
    with open(f'web/templates/{base_file}', 'r+') as html:
        html = html.read()
        template = Template(html)
        html = template.render(musics=musics)  # Изменить

    try:
        os.remove(f'web/templates/{file_name}')
    except:
        print('Error in Jinja_templates')

    with open(f'web/templates/{file_name}', 'w+') as new:
        new.write(html)


if __name__ == "__main__":

    musics = os.listdir('music')
    name_music = ''

    Jinja_templates('base.html', 'music.html', musics=musics)  # Изменить


    @eel.expose(name_or_function='play_song')
    def play_song(name):
        mixer.music.load(f'music/{name}')
        mixer.music.play()

        global name_music
        name_music = name

        return print(f'{name} запущен')


    @eel.expose(name_or_function='play_stop')
    def play_stop(not_paused):
        if not not_paused:
            mixer.music.pause()
        else:
            mixer.music.unpause()


    @eel.expose(name_or_function='after')
    def after():
        global name_music
        counter = 0

        for index in musics:
            if index == name_music:
                break
            else:
                counter += 1

        if len(musics) - 1 <= counter:
            counter = counter - len(musics)

        mixer.music.load(f'music/{musics[counter + 1]}')
        mixer.music.play()

        name_music = musics[counter + 1]

        return print(f'{musics[counter + 1]} запущен')


    @eel.expose(name_or_function='before')
    def before():
        global name_music
        counter = 0

        for index in musics:
            if index == name_music:
                break
            else:
                counter += 1

        if counter <= 0:
            counter = counter + len(musics)

        mixer.music.load(f'music/{musics[counter - 1]}')
        mixer.music.play()

        name_music = musics[counter - 1]

        return print(f'{musics[counter - 1]} запущен')


    @eel.expose(name_or_function='volume_song')
    def volume_song(value):
        mixer.music.set_volume(float(value) / 100)


    eel.start("templates/music.html", size=(400, 600), mode="edge")
