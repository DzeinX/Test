let not_paused = false

    async function play_song(name, id) {
        await eel.play_song(name)();
        not_paused = false;
        document.getElementById('p_s').src = '../pause.png';
    }

    async function play_stop() {
        if (not_paused) {
            await eel.play_stop(not_paused)();
            not_paused = false;
            document.getElementById('p_s').src = '../pause.png';
        }
        else{
            await eel.play_stop(not_paused)();
            not_paused = true;
            document.getElementById('p_s').src = '../play.png';
        }
    }

    async function after() {
        await eel.after()();
    }

    async function before() {
        await eel.before()();
    }

    async function volume_song(value) {
        await eel.volume_song(value)();
    }

    $("input[class='music_btn']").bind('click', function () {
        const name = document.getElementById(this.id).value
        const id = document.getElementById(this.id)
        play_song(name, id);
    })

    $("#p_s").bind('click', function () {
        play_stop();
    })

    $("#afr").bind('click', function () {
        after();
    })

    $("#bfr").bind('click', function () {
        before();
    })

    $("#volume_song").bind('click', function () {
        const value = this.value
        volume_song(value);
    })