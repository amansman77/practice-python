var socket = io.connect('http://localhost:5000/visualize')
socket.on('response', function(data) {
    console.log(data);
    image = 'data:image/png;base64,' + data.rms.image
    document.getElementById('img').src=image
})

window.onload = function() {

    var btn = document.getElementById('btn').onclick = function(ev){
        socket.emit('visualize', {'request_id': 1, 'file_id': 4})
    }
}